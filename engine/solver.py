import networkx as nx
from .geometry import find_shared_boundary

class DoorSolver:
    def __init__(self):
        # The 'Hierarchy of Adjacency'
        # Lower score = High priority / Natural connection
        self.type_weights = {
            ("corridor", "public"): 1.0,  # e.g., Hallway to Living Room
            ("corridor", "private"): 1.5, # e.g., Hallway to Bedroom
            ("public", "public"): 2.0,    # e.g., Living to Dining
            ("service", "public"): 2.5,   # e.g., Kitchen to Dining
            ("private", "private"): 10.0, # e.g., Bedroom to Bedroom (Unnatural)
        }

    def _get_weight(self, s1, s2, boundary_len):
        """Calculates how 'natural' a connection is."""
        # Sort types to match the dictionary keys
        pair = tuple(sorted([s1.room_type, s2.room_type]))
        base_weight = self.type_weights.get(pair, 5.0)

        # Geometry Heuristic: 
        # 1. We prefer longer walls (more flexible for placement)
        # 2. We penalize extremely narrow connections
        geometry_bonus = 1.0 / (boundary_len / 2.0)
        
        return base_weight * geometry_bonus

    def solve(self, spaces):
        """
        Generates a graph where edges represent optimal door locations.
        """
        # Create the 'Full Adjacency' graph
        full_graph = nx.Graph()
        
        for i, s1 in enumerate(spaces):
            for j, s2 in enumerate(spaces[i+1:], i+1):
                boundary = find_shared_boundary(s1, s2)
                
                if boundary:
                    b_len = boundary[2][1] - boundary[2][0]
                    weight = self._get_weight(s1, s2, b_len)
                    
                    full_graph.add_edge(
                        s1.uid, s2.uid, 
                        weight=weight, 
                        wall_info=boundary
                    )

        # 1. Start with a Minimum Spanning Tree (MST)
        # This guarantees every room is reachable from the entrance.
        final_doors = nx.minimum_spanning_tree(full_graph, weight='weight')

        # 2. Add 'Utility Loops' (The Natural Flow)
        # If a connection is 'cheap' enough (e.g. Kitchen to Dining), 
        # add it even if the room is already connected via a hallway.
        threshold = 2.5
        for u, v, data in full_graph.edges(data=True):
            if data['weight'] < threshold:
                final_doors.add_edge(u, v, **data)

        return final_doors

# Helper for main.py
def generate_door_plan(spaces):
    solver = DoorSolver()
    return solver.solve(spaces)