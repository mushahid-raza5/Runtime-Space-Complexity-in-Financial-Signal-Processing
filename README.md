# Financial Signal Processing: Runtime & Space Complexity

## Project Overview
This project compares two strategies for calculating moving averages:
1.  **Naive Strategy ($O(N^2)$):** Slow. Recalculates everything every time.
2.  **Windowed Strategy ($O(N)$):** Fast. Updates the sum incrementally.

## Setup Instructions
1.  **Install Requirements:**
    ```bash
    pip install matplotlib memory-profiler
    ```
2.  **Run the Project:**
    ```bash
    python main.py
    ```
3.  **Run Tests:**
    ```bash
    python -m unittest discover -s tests -t .
    ```

## Module Descriptions
* **`main.py`**: Runs the assignment and generates the graphs.
* **`strategies.py`**: Contains the Naive and Windowed algorithms.
* **`reporting.py`**: Creates the PNG charts and this report.