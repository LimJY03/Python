'''
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

> The first line contains X, the number of shoes.
> The second line contains the space separated list of all the shoe sizes in the shop.
> The third line contains N, the number of customers.
> The next N lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.

Constraints

> 0 < X < 10^3
> 0 < N <= 10^3
> 20 < x < 100
> 2 < shoe size < 20

Output Format

> Print the amount of money earned by Raghu.

Sample Input

> 10
> 2 3 4 5 6 8 7 6 5 18
> 6
> 6 55
> 6 45
> 6 55
> 4 40
> 18 60
> 10 50

Sample Output

> 200

Explanation

> Customer 1: Purchased size 6 shoe for $55.
> Customer 2: Purchased size 6 shoe for $45.
> Customer 3: Size 6 no longer available, so no purchase.
> Customer 4: Purchased size 4 shoe for $40.
> Customer 5: Purchased size 18 shoe for $60.
> Customer 6: Size 10 not available, so no purchase.
>
> Total money earned = 55 + 45 + 40 + 60 = $200

src: "https://www.hackerrank.com/challenges/collections-counter/problem"
'''

from collections import Counter

# Store Shoe Sizes
_ = input()
all_shoe_size = Counter(input().split())

# User Purchase
purchase_count = int(input())
sum = 0

for i in range(purchase_count):

    transaction = input().split()

    if (transaction[0] in all_shoe_size.keys()) and (all_shoe_size[transaction[0]] > 0):
        sum += int(transaction[1])
        all_shoe_size[transaction[0]] -= 1

print(sum)