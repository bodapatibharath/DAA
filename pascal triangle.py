def generate_pascals_triangle(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(" ", end="")
        C = 1
        for j in range(1, i + 1):
            print(" ", C, sep="", end="")
            C = C * (i - j) // j
        print()


n = int(input())
generate_pascals_triangle(n)
