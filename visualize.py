import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_apartment(spaces, door_plan):
    """
    Renders the apartment layout and the calculated doors.
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 1. Draw the Rooms (Spaces)
    for s in spaces:
        # Create a rectangle patch
        rect = patches.Rectangle(
            (s.x, s.y), s.w, s.h, 
            linewidth=2, edgecolor='black', facecolor='#ecf0f1', alpha=0.5
        )
        ax.add_patch(rect)
        
        # Add the room label in the center
        plt.text(
            s.x + s.w/2, s.y + s.h/2, 
            f"{s.name}\n({s.room_type})", 
            ha='center', va='center', fontsize=9, fontweight='bold'
        )

    # 2. Draw the Doors
    # We iterate through the edges chosen by our Solver
    for u, v, data in door_plan.edges(data=True):
        wall = data['wall_info']
        orientation, coord, (start, end) = wall
        
        # Calculate the midpoint of the shared wall for door placement
        mid_point = (start + end) / 2
        
        if orientation == "vertical":
            # Door is a red dot on a vertical wall
            ax.plot(coord, mid_point, 'ro', markersize=10, label="Door")
            # Optional: Draw a small line to represent the door opening
            ax.plot([coord, coord], [mid_point-0.4, mid_point+0.4], color='red', linewidth=4)
        else:
            # Door is a red dot on a horizontal wall
            ax.plot(mid_point, coord, 'ro', markersize=10)
            ax.plot([mid_point-0.4, mid_point+0.4], [coord, coord], color='red', linewidth=4)

    # Formatting the plot
    ax.set_aspect('equal')
    plt.title("Generated Door Plan: 'Natural & Efficient' Connections", fontsize=14)
    plt.xlabel("Meters (X)")
    plt.ylabel("Meters (Y)")
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Adjust limits based on room coordinates
    all_x = [s.x + s.w for s in spaces] + [s.x for s in spaces]
    all_y = [s.y + s.h for s in spaces] + [s.y for s in spaces]
    plt.xlim(min(all_x)-1, max(all_x)+1)
    plt.ylim(min(all_y)-1, max(all_y)+1)
    
    print("Displaying floor plan... Close the window to exit.")
    plt.show()