
<a id="readme-top"></a>

<h3 align="center">Applied Algorithms (D795)</h3>

  <p align="center">
    Course D795 – Ambulance Dispatch Simulation using Dijkstra’s and Uniform Cost Search  
    <br /><br />
</div>

## About the Project

This project was completed for **WGU’s D795 – Applied Algorithms**, demonstrating algorithm design, analysis, and optimization through a **Python-based ambulance dispatch simulation**. The program models emergency response operations by applying and comparing **Dijkstra’s Algorithm** and **Uniform Cost Search (UCS)** for route optimization.

The project highlights algorithmic thinking, computational efficiency, and real-world application of pathfinding techniques in graph-based systems—showcasing both theoretical and practical algorithm implementation and analysis.

## Course Information

**Course:** D795 – Applied Algorithms
**Focus:** Implementing, analyzing, and comparing algorithmic efficiency and performance using Big O notation and empirical testing.

### Competencies

**Algorithmic Design and Implementation**
The graduate designs and implements algorithms to solve complex computational problems.

**Complexity Analysis**
The graduate evaluates algorithm performance using Big O time and space complexity measures.

**Empirical Performance Testing**
The graduate measures and compares execution performance of multiple algorithms on the same problem set.

## Project Overview

The **Ambulance Dispatch Simulation** processes input data from several CSV files to model a city-wide emergency response system. It determines the most efficient ambulance to assign to each call based on travel times calculated by the implemented algorithms.

### Input Data

* `location_network.csv` – Defines the road network graph (nodes and weighted edges).
* `ambulance.csv` – Lists available ambulances and staging locations.
* `call_priority.csv` – Maps emergency priority levels to response thresholds.
* `calls.csv` – Contains timestamped emergency call records.

### Application Workflow

1. **Initialization**

   * Loads all input files.
   * Builds graph structures and priority queues.

2. **Dispatch Simulation**

   * Prioritizes calls by urgency and arrival order.
   * Calculates the fastest route for each ambulance to the call site.
   * Selects and logs the dispatch with route details.

3. **Completion**

   * Continues until all calls are resolved and outputs `ambulance_call_log.csv`.

## Algorithm Implementations

### Dijkstra’s Algorithm

**Purpose:** Finds the shortest path from a source node to all reachable nodes in a weighted graph with non-negative edges.
**Usage in Simulation:** Calculates the fastest routes from each ambulance’s location to the call site and selects the minimal total time.
**Complexity:**

* Time: O((V + E) log V)
* Space: O(V)
  **Performance:** Average runtime of **0.00471 seconds** across ten test runs.
  **Optimization Suggestion:** Use a custom priority queue via `heapq` for lower overhead.

### Uniform Cost Search (UCS)

**Purpose:** A goal-oriented variant of Dijkstra’s that stops when the destination node is reached.
**Usage in Simulation:** Computes the minimal-cost path from each ambulance to a specific call location.
**Complexity:**

* Time: O((V + E) log V)
* Space: O(V)
  **Performance:** Average runtime of **0.00234 seconds**, approximately **50% faster** than Dijkstra’s under identical conditions.
  **Optimization Suggestion:** Use a dictionary to store the lowest known cost per node to avoid redundant path expansions.

## Results Summary

| Algorithm  | Avg Time (sec) | Complexity     | Optimal Path Guarantee | Recommended Use                |
| ---------- | -------------- | -------------- | ---------------------- | ------------------------------ |
| Dijkstra’s | 0.00471        | O((V+E) log V) | Yes                    | Full-graph exploration         |
| UCS        | 0.00234        | O((V+E) log V) | Yes                    | Single-destination pathfinding |

Both algorithms produced correct shortest paths, with UCS demonstrating superior efficiency due to its early termination on goal discovery.

## Learning Summary

This course strengthened understanding of **algorithmic efficiency**, **pathfinding optimization**, and **empirical testing**. By applying Big O analysis and real-world simulation, I gained deeper insight into how algorithm choice impacts performance, scalability, and computational cost in system design.

## References

Goldwasser, M., Goodrich, M. T., & Tamassia, R. (2024). *Algorithm Design and Applications.* zyBooks.
Western Governors University. (2025). *D795 – Applied Algorithms Course Material.*

## Contact

**Silver Alcid**
[Website](https://silveralcid.com) • [Outlook](mailto:silveralcid@outlook.com)

