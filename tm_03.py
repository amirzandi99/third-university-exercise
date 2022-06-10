def cases(x):
    r = 0
    for i in range(1,x+1):
        f = 1
        s = 0
        for j in range(1,i+1):
            f = f * j
            s = s + (1 / f)
        a = x // (i * s)
        r = r + a
    print(f"result : {r}")
# 
def main():
    n = int(input("input number of days : "))
    cases(n)
# 
if __name__ == "__main__":
    main()