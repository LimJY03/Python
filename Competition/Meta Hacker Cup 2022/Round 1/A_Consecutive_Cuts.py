if __name__ == '__main__':

    with open('./consecutive_cuts_chapter_1_validation_input.txt', 'r') as f:

        T = int(f.readline())
        output = []

        for Ti in range(T):

            step = list(map(int, f.readline().split()))[1]

            A = f.readline().split()
            B = f.readline().split()

            possible = 'NO' if (step == 0) else ('YES' if ((A[A.index(B[0]):] + A[0:A.index(B[0])]) == B) else 'NO')

            output.append('Case #{}: {}'.format((Ti + 1), possible))

    with open('./consecutive_cuts_chapter_1_validation_output.txt', 'w') as f:

        f.write('\n'.join(output))

    print('\n'.join(output))