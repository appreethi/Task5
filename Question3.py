'''Using python lambda function  create a Fibonacci series fro 1 to 50'''

#Generate fibonacci series upto 50
def fibonacci_series(n):
    #Initializing fib with 0 and 1
    fib = [0,1]
    while fib[-1] < n:
        fib.append(fib[-1]+fib[-2])
    return list(filter(lambda x: x<=n ,fib)) # will be getting results which are filteres as per the condition given

#calling function   
fib_series=fibonacci_series(50)
fib_series=fib_series[1:] # using slicing as we need to exclude 0 from the list
#Printing the results
print("Fibonacci series from 1 to 50 :",fib_series)