def fibonacci(n):
    if n<0:  # base condition if the number is less than zero the code will terminate on the base condition
        print("Invalid arguments!!!")
    if (n==0): 
        return 0
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # return the values

if __name__ == "__main__":
    n = 5
    for i in range(n):
        print(fibonacci(i), end=' ')
