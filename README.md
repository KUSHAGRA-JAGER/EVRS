# 🚑 Emergency Vehicle Routing System using Dijkstra’s Algorithm

This project implements an Emergency Vehicle Routing System using **Dijkstra’s Algorithm** to find the shortest path between the current location of an emergency vehicle (like an ambulance or police car) and the incident site.

---

## 📌 Features

- Graph-based simulation of a city road network
- Uses **Dijkstra’s Algorithm** to compute the shortest path
- User-friendly input prompts for source and destination
- Efficient pathfinding using a priority queue
- Simple and extendable code structure

---

## 🛠️ Technologies Used

- **Python 3**
- Standard Python libraries (`heapq`, `input`, `print`)

---

## 🧠 How It Works

- The city is represented as a **graph**, where:
  - Nodes = locations (e.g., Hospital, Junctions, Accident Site)
  - Edges = roads with associated distances
- The user provides:
  - The current location of the emergency vehicle
  - The destination (accident site)
- The program calculates and displays:
  - The shortest path
  - The total distance

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/emergency-routing-dijkstra.git
cd emergency-routing-dijkstra
