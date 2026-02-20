class Space:
    """
    Represents a rectangular room in the apartment.
    """
    def __init__(self, uid, name, x, y, w, h, room_type="general", is_entrance=False):
        self.uid = uid            # Unique ID (integer or string)
        self.name = name          # Display name (e.g., "Kitchen")
        self.x = x                # Bottom-left X coordinate
        self.y = y                # Bottom-left Y coordinate
        self.w = w                # Width
        self.h = h                # Height
        self.room_type = room_type # Used for weighting (e.g., 'corridor', 'private')
        self.is_entrance = is_entrance

    @property
    def bounds(self):
        """Returns (xmin, ymin, xmax, ymax) for easy overlap checking."""
        return (self.x, self.y, self.x + self.w, self.y + self.h)

    def __repr__(self):
        return f"<Space {self.name} ({self.room_type})>"