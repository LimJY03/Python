'''
Maverick is playing a jet survival game in which the stage lasts T seconds. The stage is divided into N segments, each segment is described as a positive 
integer in seconds, ranging from 1 to T. The summation of the total time of all segments is equal to T.

The challenge in the game is that the altitude limit for each segment is different and Maverick should not exceed the limit. For example, when T = 100 seconds, 
for the first 40 seconds the altitude limit is set at 75,000m and moving forward for the next 50 seconds the limit is 35,000m and for the final 10 seconds, 
the limit is 45,000m.

Maverick’s game journey is described in M segments of total T seconds (total time taken for the stage). During each segment, he travels at certain altitudes 
in meters. For example, when T = 100 seconds, for the first 40 seconds, the altitude he maintains is 76,000m, and for the next 20 seconds, he maintains an 
altitude of 30,000m, and lastly, for the final 40 seconds, he maintains an altitude of 40,000m.

You are given with the altitude limits of N segments of T seconds, and also Maverick's reaching altitudes for M segements of T seconds. Determine the maximum number of altitudes exceeded by Maverick while playing the game.

Input Format

> The first line of the input contains T, N and M, is separated by a space.
> The next N lines each contain two positive integers describing a game segment, mentioning the time and altitude limit.
> The next N lines each contain two integers describing each segment in Maverick's journey, mentioning the time and the altitude that Maverick was maintaining 
  at each segment.

Constraints

> 1 <= T <= 2 * 10^4
> 1 <= N, M <= 1 * 10^3
> 1 <= Ni, Mi <= 2 * 10^10

Please keep note, N, M will always be smaller than T.

Output Format

A single line containing the maximum amount of altitude limit exceeded by Maverick during any part of his journey. If he never exceeds the altitude limit, 
the output should be 0.

Sample Input 0

> 100 3 3
> 40 75000
> 50 35000
> 10 45000
> 40 76000
> 20 30000
> 40 40000

Sample Output 0

> 5000
'''

T, N, M = map(int, input().split())

time_N, alt_N = [0] * N, [0] * N
time_M, alt_M = [0] * M, [0] * M
max_diff = 0

for i in range(N):
    time_N[i], alt_N[i] = map(int, input().split())

for i in range(M):
    time_M[i], alt_M[i] = map(int, input().split())

i, j = 0, 0
timeframe_N, timeframe_M = time_N[i], time_M[j]

while (timeframe_N < T) or (timeframe_M < T):

    if (timeframe_M == timeframe_N):

        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if i < len(time_N) - 1: i += 1; timeframe_N += time_N[i]
        if j < len(time_M) - 1: j += 1; timeframe_M += time_M[j]

    elif (timeframe_M > timeframe_N):

        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if i < len(time_N) - 1: i += 1; timeframe_N += time_N[i]

    else:

        max_diff = max(max_diff, alt_M[j] - alt_N[i])
        if j < len(time_M) - 1: j += 1; timeframe_M += time_M[j]
    
print(max_diff)