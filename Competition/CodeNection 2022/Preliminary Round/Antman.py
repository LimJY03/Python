'''
MMU has recently conducted research on the ants and made all of its students and staff aware of the effectiveness and the significance of this tiny little creature in the ecosystem, 
based on the outcome of the research, they are selecting one person in charge for the task to save the ants who’ll be called as Antman.

Being loyal about the duty, you’re trying to be an extra-caregiver for the ants now, as you have noticed N number of anthills on your roof. Recently, your area has been forecasted 
to have heavy rainfall. Hence, you would like to make a rectangular shed for them, but you are having a tight budget for it.

To position each of the anthills, you’re drawing a cartesian coordinate (XY plane) system on your roof. Now, you know the position, in terms of (x, y), of each of your anthills. 
Consider each anthill as a point.

As you have a tight budget, you are willing to make the shed as small as possible, so it can accommodate at least N-1 anthills. Write a program that can calculate the most efficient 
way to make the shed that has the least area.

Please consider the shed as a rectangle, with four lines, and the anthill as a point. The output could be 0 if all the anthills are aligned in a single line, as the width is 0 there.

Input Format

> The first line of the input contains N, which represents the number of anthills on the roof. The next N lines each contain two positive integers defining the location of an anthill 
  which are in the range of (1 <= N <= 4 * 10^4).

Constraints

> (1 <= N <= 4 * 10^4)

Output Format

> A single line containing the least area you can enclose with the rectangular shed after removing up to 1 wisely-chosen anthill from your roof.

Sample Input 0

> 4
> 2 4
> 1 1
> 5 2
> 17 25

Sample Output 0

> 12

Explanation 0

> Moving the anthills at position (17, 25), we find the least area of the shed having all of our requirements fulfilled: area = (5 - 1) * (4 - 1) = 12.

src: "https://www.hackerrank.com/contests/codenection-2022-open-category-preliminary-cp/challenges/antman"
'''

N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

min_x, min_y = min(coords, key=lambda row: row[0]), min(coords, key=lambda row: row[1])
max_x, max_y = max(coords, key=lambda row: row[0]), max(coords, key=lambda row: row[1])

# min_x
temp = list(coords)
temp.remove(min_x)
min_x, min_y = min(temp, key=lambda row: row[0]), min(temp, key=lambda row: row[1])
max_x, max_y = max(temp, key=lambda row: row[0]), max(temp, key=lambda row: row[1])
area = (max_x[0] - min_x[0]) * (max_y[1] - min_y[1])

# min_y
temp = list(coords)
temp.remove(min_y)
min_x, min_y = min(temp, key=lambda row: row[0]), min(temp, key=lambda row: row[1])
max_x, max_y = max(temp, key=lambda row: row[0]), max(temp, key=lambda row: row[1])
area = min((max_x[0] - min_x[0]) * (max_y[1] - min_y[1]), area)

# max_x
temp = list(coords)
temp.remove(max_x)
min_x, min_y = min(temp, key=lambda row: row[0]), min(temp, key=lambda row: row[1])
max_x, max_y = max(temp, key=lambda row: row[0]), max(temp, key=lambda row: row[1])
area = min((max_x[0] - min_x[0]) * (max_y[1] - min_y[1]), area)

# max_y
temp = list(coords)
temp.remove(max_y)
min_x, min_y = min(temp, key=lambda row: row[0]), min(temp, key=lambda row: row[1])
max_x, max_y = max(temp, key=lambda row: row[0]), max(temp, key=lambda row: row[1])
area = min((max_x[0] - min_x[0]) * (max_y[1] - min_y[1]), area)

print(area)