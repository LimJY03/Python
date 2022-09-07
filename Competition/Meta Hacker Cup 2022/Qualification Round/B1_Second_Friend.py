def tree_exist(arr: list[str]) -> bool:
    return '^' in ''.join(arr)

def draw(type: str) -> str:
    return 'Possible\n{}'.format('\n'.join([type * C] * R))

if __name__ == '__main__':

    with open('./B1_io/second_friend_input.txt', 'r') as f:

        T = int(f.readline())
        output = []

        for Ti in range(T):

            R, C = map(int, f.readline().split())
            diagram = [f.readline() for _ in range(R)]

            output.append('Case #{}: {}'.format((Ti + 1), ('Impossible' if tree_exist(diagram) else draw('.')) if (R < 2 or C < 2) else draw('^')))

    with open('./B1_io/second_friend_output.txt', 'w') as f:

        f.write('\n'.join(output))