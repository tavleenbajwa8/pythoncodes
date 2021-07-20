print("Welcome to the Fibonacci Calculator App")
x = int(input("\nHow many digits of the Fibonacci sequence you would like to compute: "))
print("\nThe first " + str(x) + " numbers of the Fibonacci sequence are: ")
fib = [1,1]
for i in range(x-2):
    new_fib = (fib[i] + fib[i+1])
    fib.append(new_fib)
print("\nThe first " + str(x) + " numbers of the Fibonacci sequence are:")
for x in fib:
    print(x)
    
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
    print(ratio)
print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618..")
