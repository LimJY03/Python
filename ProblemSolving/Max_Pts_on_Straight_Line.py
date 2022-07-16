'''
Given N point on a 2D plane as pair of (x, y) coordinates, write a program to find the maximum number of point which lie on the same line.

Example 1:
Input: A[][] = [[1,1],[2,2],[1,2],[3,3],[2,3]]
Output: 3
Explanation: The maximum number of point which lie on same line are 3, those points are [1,1], [2, 2] and [3, 3].

Example 2:
Input: A[][] = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation: The maximum number of point which lie on same line are 4, those points are [3,2], [4,1], [2,3] and [1, 4].

src: "https://afteracademy.com/blog/max-points-on-the-straight-line"
'''

def get_gradient(xy1, xy2):

    x1, y1 = tuple(xy1)
    x2, y2 = tuple(xy2)

    if x2 != x1:
        return (y2 - y1) / (x2 - x1)
    else:
        return 999999999999999999   # This needs to be fixed for denominator == 0 or gradient == infinity

def count_maxpoints(coords):

    gradient_list = []
    mode_gradient_list = []
    mode_gradient_count_list = []
    count = 0

    for i in range(len(coords) - 1):

        # Get gradient for each points and the (initial point based on i)
        for j in range((i + 1), (len(coords))):
            gradient_list.append(get_gradient(coords[i], coords[j]))
        
        # Create list of modes of gradients from each iterations
        mode_gradient_list.append(max(set(gradient_list), key = gradient_list.count))

        # Create list of number of (radients equal to modes) from each iterations
        mode_gradient_count_list.append(gradient_list.count(max(set(gradient_list), key = gradient_list.count)))

        # Clear gradient_list for reuse purpose
        gradient_list = []

    # Determines index of the initial point has mode gradient
    initial_point_index = mode_gradient_count_list.index(max(mode_gradient_count_list))

    # Determine the mode gradient found for that initial point
    gradient = mode_gradient_list[initial_point_index]

    # Determine number of gradients for each points and the set initial point equals to the mode gradient
    for k in range((initial_point_index + 1), len(coords)):
        if (get_gradient(coords[initial_point_index], coords[k]) == gradient):
            count += 1

    # Since 1 gradient represents 2 points, and 2 gradient represents 3 points etc., number of collinear points = number of similar gradient + 1
    return count + 1

# Validation Test
print(
    count_maxpoints([[1, 1], [2, 2], [2, 3], [3, 3], [3, 5]]), 
    count_maxpoints([[1, 1], [2, 2], [1, 2], [3, 3], [2, 3]]), 
    count_maxpoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
)