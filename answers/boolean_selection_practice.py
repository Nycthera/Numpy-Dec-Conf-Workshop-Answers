
import numpy as np

scores = np.array([35, 48, 67, 82, 91])

# 1. Select scores greater than 60
print(scores[scores > 60])
# [67 82 91]

# 2. Select scores between 40 and 80 (inclusive)
print(scores[(scores >= 40) & (scores <= 80)])
# [48 67]

# 3. Replace scores below 50 with 50
scores[scores < 50] = 50
print(scores)
# [50 50 67 82 91]

# 4. Bonus: Count how many scores are above 70
print(np.sum(scores > 70))
# 2
