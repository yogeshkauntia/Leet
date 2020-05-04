def maxArea(height):
    '''
    Input will be an array which is the height of wall on each position: https://leetcode.com/problems/container-with-most-water/
    '''
    head = 0
    tail = len(height) - 1
    area = 0
    while tail > head:
        area = max(area, min(height[head], height[tail]) * (tail - head))
        if height[head] > height[tail]:
            tail = tail - 1
        else:
            head = head + 1
    return area


print(maxArea([1, 2, 1, 2]))
