
# Es3

$$DP(i, j) = \min_{k=i}^{j-1} \{ DP(i, k) + DP(k+1, j) + \text{max-leaf}(i, k) \times \text{max-leaf}(k+1, j)\}$$
