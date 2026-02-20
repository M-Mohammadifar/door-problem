"""
Geometry Engine for Door Placement.
Handles precision boundary detection between axis-aligned rectangles.
"""

# Standard architectural door width in meters
MIN_DOOR_WIDTH = 0.8 
# Floating point tolerance for coordinate comparison
EPSILON = 1e-5 

def find_shared_boundary(s1, s2):
    """
    Identifies if two spaces share a valid wall segment for a door.
    
    Returns:
        tuple: (orientation, coordinate, (start, end)) if a valid boundary exists.
        None: If spaces do not touch or the overlap is too small.
    """
    b1 = s1.bounds # (xmin, ymin, xmax, ymax)
    b2 = s2.bounds

    # 1. VERTICAL WALL CHECK (s1 is left/right of s2)
    # Check if s1.right == s2.left OR s1.left == s2.right
    is_adjacent_v = abs(b1[2] - b2[0]) < EPSILON or abs(b1[0] - b2[2]) < EPSILON
    
    if is_adjacent_v:
        # Find the overlapping interval on the Y-axis
        overlap_start = max(b1[1], b2[1])
        overlap_end = min(b1[3], b2[3])
        overlap_len = overlap_end - overlap_start
        
        if overlap_len >= MIN_DOOR_WIDTH:
            # Determine the exact X coordinate of the shared wall
            x_coord = b1[2] if abs(b1[2] - b2[0]) < EPSILON else b1[0]
            return ("vertical", x_coord, (overlap_start, overlap_end))

    # 2. HORIZONTAL WALL CHECK (s1 is top/bottom of s2)
    # Check if s1.top == s2.bottom OR s1.bottom == s2.top
    is_adjacent_h = abs(b1[3] - b2[1]) < EPSILON or abs(b1[1] - b2[3]) < EPSILON
    
    if is_adjacent_h:
        # Find the overlapping interval on the X-axis
        overlap_start = max(b1[0], b2[0])
        overlap_end = min(b1[2], b2[2])
        overlap_len = overlap_end - overlap_start
        
        if overlap_len >= MIN_DOOR_WIDTH:
            # Determine the exact Y coordinate of the shared wall
            y_coord = b1[3] if abs(b1[3] - b2[1]) < EPSILON else b1[1]
            return ("horizontal", y_coord, (overlap_start, overlap_end))

    return None