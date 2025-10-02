#LEVEL2-T4
#Task: Fibonacci Sequence
#Write a Python function that generates the Fibonacci sequence up to a givenmber of terms. The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.

def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

n = int(input("Enter the number of terms: "))
print(fibonacci(n))
