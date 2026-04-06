# This function computes maximum value of a common subsequence of A and B.
# It expectes 3 parameters:
#   - values: a dictionary where keys are characters and the values are the values of those characters.
#   - A: a string
#   - B: a string
#
# The function returns the maximum value and the subsequence itself as a tuple (max_value, subsequence),
# where max_value is a number and subsequence is a string.
def HVLCS(values, A, B):
    m, n = len(A), len(B)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = max(values.get(A[i], 0) + dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                
    max_value = dp[0][0]
    subsequence = ""
    
    i, j = 0, 0
    while i < m and j < n:
        down = dp[i + 1][j]
        right = dp[i][j + 1]
        diagonal = dp[i + 1][j + 1]
        
        if A[i] == B[j] and diagonal + values.get(A[i], 0) == dp[i][j]:
            subsequence += A[i]
            i += 1
            j += 1
        elif down >= right:
            i += 1
        else:
            j += 1
            
    return max_value, subsequence