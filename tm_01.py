import math

cp = int(input("input the Car price ------- : "))
ir = int(input("input Installment rate ---- : "))
af = int(input("input Annual fee ---------- : "))
ti = int(input("input Total of installments : "))
payment = (cp - ir) / ti
print(f"payment : {payment}")