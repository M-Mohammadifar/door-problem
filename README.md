# Apartment Door Placement Engine

## 1. Project Overview

This project is a computational design prototype developed for a fun Software Engineer challenge. It addresses the "Door Problem": given a set of rectangular spaces representing an apartment layout, the engine automatically identifies valid shared boundaries and determines the most **natural and efficient** locations for internal connections.

The solution utilizes **Computational Geometry** for boundary detection and **Weighted Graph Theory** (Dual-Graphs) to simulate architectural flow and privacy hierarchies.

---

## 2. Core Assumptions & Constraints

### Geometric Logic

- **Orthogonal Geometry:** All spaces are axis-aligned rectangles defined by $(x, y, w, h)$.
- **Zero-Thickness Walls:** Adjacency is defined by co-linear edges.
- **Precision Tolerance:** Uses an epsilon-based comparison ($1e-5$) to handle floating-point coordinate math, ensuring stability in a CAD-like environment.
- **Minimum Clearance:** A "door" requires a minimum shared wall length of **0.8m**. Shared boundaries smaller than this are ignored to prevent non-functional or physically impossible openings.

### "Natural & Efficient" Flow

Architectural flow is not merely a shortest-path problem; it is a balance of reachability and privacy.

1.  **Fixed Entrance Assumption:** The algorithm focuses on **internal circulation only**. It assumes the exterior entrance is a fixed architectural constraint and does not attempt to "invent" doors to the outside.
2.  **The Privacy Hierarchy:** We use a cost matrix to prioritize connections. Linking a `Corridor` to a `Living Room` has a low cost, while linking a `Bedroom` directly to another `Bedroom` is heavily penalized.
3.  **Hybrid Graph Strategy:** \* **Reachability:** A Minimum Spanning Tree (MST) ensures every room is reachable from the designated entrance.
    - **Utility Loops:** To avoid "maze-like" layouts, the engine adds secondary doors for highly natural adjacencies (e.g., Kitchen to Dining) even if they aren't strictly required for connectivity.

---

## 3. Local Setup & Execution

### Prerequisites

- **Python 3.9+**
- `matplotlib` (for visualization)
- `networkx` (for graph processing and MST calculations)

### Installation

```bash
pip install matplotlib networkx
```
