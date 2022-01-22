def fibo(number):
    ones = [0,1]
    zeros = [1,0]
    for i in range(2,number+1):
        ones.append(ones[i-1] + ones[i-2])
        zeros.append(zeros[i-1] + zeros[i-2])
    return str(zeros[number])+" "+str(ones[number])    



Number = int(input())

for i in range(Number):
    data = int(input())
    print(fibo(data))