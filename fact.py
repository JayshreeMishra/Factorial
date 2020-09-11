# This program calculates the factorial of given number by both itrative and recursive method.
# Itrative method
def fact_i(n):
    fact=1
    for i in range(n):
        fact= fact*(i+1)
    return fact  
n=int(input("Enter the number\n"))    
print("Factorial using itrative method is", fact_i(n))      

# Recursive method
def fact_r(m):
    if m==1:
        return 1
    else:
        return m*fact_r(m-1)
m= int(input("Enter the number\n"))
print("Factorial using recursive method is", fact_r(m))        



