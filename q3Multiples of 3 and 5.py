def getMultiples(below_number, num1, num2):
    temp = 0

    for i in range(1, below_number):
        if i % num1 == 0 or i % num2 == 0:
            temp += i
    return temp
    
    
if __name__ == '__main__':
    print(getMultiples(1000, 3, 5))
    