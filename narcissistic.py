def narcissistic(value):
    sum=0
    for n in str(value):
        x= int(n)**len(str(value))
        sum=sum+x
    if sum== int(value):
        return True
    else:
        return False
narcissistic(153)




