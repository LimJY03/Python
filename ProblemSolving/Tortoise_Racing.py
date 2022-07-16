'''
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second).

If v1 >= v2 then return None.

Examples:

race(720, 850, 70) => [0, 32, 18]
race(80, 91, 37)   => [3, 21, 49]

src: "https://www.codewars.com/kata/55e2adece53b4cdcb900006c/ruby"
'''

def race(speedA, speedB, distance):
    '''
    We know that [distance = speed * time].

    To let B catch up to A, in the given [time] their [total_distance] travelled must be same.

    > total_distance = speedA * time + distance
    > total_distance = speedB * time

    Also, speedA must < speedB.

    So we can arrange the equation to get the following equation.

    > speedA * time + distance = speedB * time

    We can then rearrange the equation to get [time] as our subject.

    [1] > time * speedB - time * speedA = distance
    [2] > time * (speedB - speedA) = distance
    [3] > time = distance / (speedB - speedA)

    Now we get our [time] in hours (3600 seconds). 
    '''

    # To let B catch up to A, speedA must < speedB
    if (speedA >= speedB): return None

    # Get the catch up time (float) in hours
    time = distance / (speedB - speedA)
    
    # Get the number of hours, convert into integer using int()
    num_of_hours = int((time * 3600) // 3600)

    # Get the number of minutes, convert into integer using int()
    num_of_minutes = int((time - num_of_hours) * 3600 // 60)

    # Get the number of seconds, rounding down to integer using int()
    num_of_seconds = int((time - num_of_hours) * 3600 - num_of_minutes * 60)

    return [num_of_hours, num_of_minutes, num_of_seconds]

print(
    race(720, 850, 70),
    race(80, 91, 37)
)