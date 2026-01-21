# Complexity Report

| Ticks | Naive Time | Optimized Time | Naive Mem | Optimized Mem |
|---|---|---|---|---|
| 1000 | 0.0108s | 0.0007s | 0.01MB | 0.00MB |
| 10000 | 0.9776s | 0.0029s | 0.00MB | 0.00MB |
| 100000 | 95.1473s | 0.1143s | 0.84MB | 0.00MB |
## Summary of Findings

### 1. Runtime Complexity
* **Naive Strategy ($O(N^2)$):**
  * Processing 100,000 ticks took **~95.15 seconds**.
  * The time increased exponentially as data grew (100x slower for 10x more data).
  * This is too slow for real-time trading.

* **Windowed Strategy ($O(N)$):**
  * Processing 100,000 ticks took only **0.11 seconds**.
  * This is roughly **860x faster** than the naive approach.
  * The time scales linearly (it stays fast even with more data).

### 2. Conclusion
For high-frequency trading systems processing millions of ticks, the $O(N)$ Windowed Strategy is required. The Naive approach creates unacceptable lag.