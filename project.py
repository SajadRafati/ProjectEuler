for i in range(999,900,-1):
    for j in range(999,900,-1):
        x=str(i*j)
        y=x[::-1]
        if x == y:
            print(f"I= {i} and J= {j} and X= {x}" )