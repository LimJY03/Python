if __name__ == '__main__':

    with open('./watering_well_chapter_1_input.txt', 'r') as f:

        T = int(f.readline())
        output = []

        for Ti in range(T):

            N = int(f.readline())
            tree, total = [], 0

            for Ni in range(N):

                tree.append(tuple(map(int, f.readline().split())))

            Q = int(f.readline())

            for _ in range(Q):

                Qx, Qy = map(int, f.readline().split())

                total += sum([(Qx - x) ** 2 + (Qy - y) ** 2 for x, y in tree])

            output.append('Case #{}: {}'.format((Ti + 1), total % 1000000007))

    with open('./watering_well_chapter_1_output.txt', 'w') as f:

        f.write('\n'.join(output))