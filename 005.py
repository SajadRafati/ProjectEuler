def main():
    for i in range(1000000):
        i += 1
        c = 1
        for j in range(1, 10):
            j += 1
            if i % j != 0:
                c = 0
                break
        if c == 1:
            print(i)
main()