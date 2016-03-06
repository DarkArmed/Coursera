"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = []
    mergeable = False
    for num in line:
        if num == 0:
            continue
        if mergeable == True and num == result[-1]:
            result[-1] += num
            mergeable = False
        else:
            result.append(num)
            mergeable = True
    while len(result) < len(line):
        result.append(0)
    return result
