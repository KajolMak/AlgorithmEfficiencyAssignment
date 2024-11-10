# Algorithm Efficiency Assignment

This repository contains implementations for the Randomized Quicksort algorithm and a Hash Table with Chaining for collision resolution.This assignment explores the efficiency and scalability of two fundamental algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The goal is to understand how each algorithm performs under various conditions and to analyze the theoretical and empirical performance.


## Instructions for Running the Code

1. **Clone the Repository**:
   If you haven't cloned the repository yet, use the following command:
   ```bash
   git clone https://github.com/your-username/AlgorithmEfficiencyAssignment.git

Randomized Quicksort:

Copy code 
python3 randomized_quicksort.py
This will display the sorted array and showcase its handling of different cases.

Hashing with Chaining:

Copy code
python3 hashing_with_chaining.py
This will demonstrate hash table insertions, searches, and deletions, with output on load factor management.

Summary of Findings
Randomized Quicksort: The algorithm achieves consistent performance across different array types. Random pivot selection prevents worst-case performance even with sorted inputs.
Hashing with Chaining: Maintains 
𝑂
(
1
)
O(1) efficiency for insert, search, and delete operations with a low load factor. Dynamic resizing and universal hashing minimize collisions and maintain performance.
