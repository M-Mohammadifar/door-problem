from engine.models import Space
from engine.solver import generate_door_plan
from visualize import draw_apartment

def run_prototype():
    # 1. DEFINE THE APARTMENT LAYOUT
    # Format: Space(uid, name, x, y, width, height, type)
    # We are building a simple L-shaped corridor layout
    apartment_spaces = [
        # Public Hub
        Space(1, "Hallway",    4, 4, 2, 6, "corridor"),
        
        # Living Area
        Space(2, "Living Room", 0, 4, 4, 6, "public"),
        Space(3, "Kitchen",     0, 0, 4, 4, "service"),
        
        # Private Area
        Space(4, "Bedroom 1",   6, 7, 4, 3, "private"),
        Space(5, "Bathroom",    6, 4, 3, 3, "private"),
        
        # Dining (attached to kitchen and hallway)
        Space(6, "Dining",      4, 0, 5, 4, "public")
    ]


    print("--- Branch Door Placement Engine ---")
    print(f"Processing {len(apartment_spaces)} spaces...")

    try:
        # 2. RUN THE SOLVER
        # This calculates the adjacencies and selects the best doors
        door_plan = generate_door_plan(apartment_spaces)

        # 3. REPORT RESULTS
        print(f"Success! Found {door_plan.number_of_edges()} optimal connections.")
        for u, v, data in door_plan.edges(data=True):
            room_a = next(s.name for s in apartment_spaces if s.uid == u)
            room_b = next(s.name for s in apartment_spaces if s.uid == v)
            print(f"  [Door] Created between: {room_a} <-> {room_b}")

        # 4. VISUALIZE
        draw_apartment(apartment_spaces, door_plan)

    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    run_prototype()