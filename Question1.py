'''What is the expected output of the following python code given below'''
data = [10,501,22,37,100,999,87,351]
result=filter(lambda x:x>4,data)
print(list(result))

'''output:
[10,501,22,37,100,999,87,351]

as the expression in the lambda function is given as x>4. so it will filter out all the values which are greater than 4
'''