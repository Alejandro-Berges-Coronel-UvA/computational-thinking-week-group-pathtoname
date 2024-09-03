# The algorithmn is the Fibonacci sequence

def solution_station_1(input_1):
    if input_1 <= 0:
        return 0
    if input_1 == 1:
        return 1
    else:
        return solution_station_1(input_1-1) + solution_station_1(input_1-2)
    
