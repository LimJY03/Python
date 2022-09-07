from collections import Counter

if __name__ == '__main__':

    with open('./A_io/second_hands_input.txt', 'r') as f:

        T = int(f.readline())
        output = []

        for Ti in range(T):

            N, K = map(int, f.readline().split())
            all_style = Counter(f.readline().split())

            # output.append('Case #{}: {}'.format((Ti + 1), 'NO' if (all_style.most_common(1)[0][1] > 2) or (N / K > 2) or (all_style.most_common()[::-1][0][1] == 2) else 'YES'))
            output.append('Case #{}: {}'.format((Ti + 1), 'NO' if (all_style.most_common(1)[0][1] > 2) or (N / K > 2) else 'YES'))

    with open('./A_io/second_hands_output.txt', 'w') as f:

        f.write('\n'.join(output))