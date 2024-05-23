num = int(input("Enter a number: "))
sum = 0

if (num <= 0):
    print("Please enter just positive numbers!")

else:
    for i in range(1, num):
        if ((num % i) == 0):
            sum += i

    if (sum == num):
        print(f"{num} is a perfect number!")

    else:
        print(f"{num} isn't a perfect number!")