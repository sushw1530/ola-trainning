def check_as(n):
    fact = len(str(n))
    
    temp = n
    sum = 0
    while temp > 0:
        t1 = temp % 10
        sum += t1
        temp = temp / 10
    
    if sum == n:
        print(n," is an Armstrong")
    else:
        print(n," is not an Armstrong")

    