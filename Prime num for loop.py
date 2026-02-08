a=int(input("Enter a num:"))
if a<=1:
    print(f"{a}is not a prime number")
else:
    for i in range(2,a):
        if a % i ==0:
            print(f"{a}is not a prime number")
            break
        else:
            print(f'{a}is a prime number')