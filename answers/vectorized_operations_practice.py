import numpy as np

# Define array
scores = np.array([35, 48, 67, 82, 91])
# 1. Add 5 to all scores
print(scores + 5)
# [40 53 72 87 96]
# 2. Find the passing scores (>50)
passing = scores[scores > 50]
print(passing)
# [67 82 91]
# 3. Multiply every score by 2
print(scores * 2)
# [ 70  96 134 164 182]
# 4. Bonus: Percentage of passing scores
percentage = np.sum(scores > 50) / len(scores) * 100
print(f"{percentage}%")
# 60.0%
