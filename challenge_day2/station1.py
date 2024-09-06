# The algorithmn is the Fibonacci sequenc
def solution_station_1(input):
    # Fibonacci sequence
    n = int(input)
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print(solution_station_1(47))



    
