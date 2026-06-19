# Graph-Theoretic Action-Sequence Optimization for Overcooked! 2 (Level Kevin 1)

This repository contains the deterministic state-event simulator used for the research paper: 
**"Graph-Theoretic Pathfinding and Action-Sequence Optimization for Single-Player Workflows in Overcooked! 2"** 
submitted for IF1220 Discrete Mathematics at Institut Teknologi Bandung.

## 📌 Overview
This Python-based simulator evaluates the efficiency of a single-player workflow in Level Kevin 1. It models the kitchen as a **Weighted Grid Graph** and utilizes a **Hybrid Dijkstra-Poset Algorithm** to synchronize spatial navigation with task precedence.

## 🛠 Core Mathematical Structures
- **Weighted Grid Graph:** A 10x17 coordinate system with dash-weighted edges (0.14s/tile) and walk-weighted edges (0.2s/tile).
- **Partially Ordered Sets (Poset):** Recipe dependencies (e.g., Chopping ≺ Steaming ≺ Serving) modeled as precedence relations.
- **Dijkstra’s Algorithm:** Used for optimal pathfinding between interaction nodes.
- **Resource Synchronization:** Implements "Plate Starvation" logic with an 11-second respawn constant.

## 🚀 Simulation Results
The simulator evaluates a deterministic queue of 16 orders (SF, SF, D, D, ...).
- **Total Makespan:** 347.11 Seconds
- **Average Completion Rate:** 21.69 Seconds/Dish
- **Predicted Throughput (240s Limit):** 11.06 Orders

The simulation identifies the **11-second plate respawn** as the absolute physical bottleneck for reactive systems, mirroring high-level human performance (~12 orders).

## 📂 Files
- `simulator.py`: The main simulation engine.
- `KOORDINAT.txt`: Mapping of kitchen workstations to (x, y) tuples.
- `LAYOUT.csv`: Structural map of the Kevin 1 environment.

## 📝 Academic Context
- **Author:** Fathar Atandra Denaya (13525067)
- **Course:** IF1220 Discrete Mathematics
- **Institution:** Institut Teknologi Bandung
- **Year:** 2026

## 📜 References
This project builds upon the "Greedy Approach" research by Chokyi Ozer (2020) and lecture materials by Dr. Ir. Rinaldi Munir, MT.
