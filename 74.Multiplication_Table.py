def multiplication_table(n):
    n += 1
    for i in range(1, n):
        if i == 1:  # header
            header = [f"{str(_):>4}" for _ in range(1, n)]
            print(f"{'':>4}{''.join(header)}")

        row = [f"{str(_ * i):>4}" for _ in range(1, n)]
        print(f"{i:>4}{''.join(row)}")


multiplication_table(15)
