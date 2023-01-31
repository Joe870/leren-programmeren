def fibonacci_recursion(n):
    if n <= 1: 
        return n
    else:
        return(fibonacci_recursion(n-1) + fibonacci_recursion(n-2))

nterms = 10

if nterms <= 0:
    print('please enter a positive integer')
else:
    print('fibonacci reeks')
    for i in range(nterms):
        print(fibonacci_recursion(i))