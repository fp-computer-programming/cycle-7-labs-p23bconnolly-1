def maximum(num_sum1):
    num_sum1.sort()
    return num_sum1[-1]
#function finds the maximum of the variable num_sum1

def minimum(num_sum1):
    num_sum1.sort()
    return num_sum1[0]
#funtion that finds the minimum from num_sum1

def difference(num_sum1):
    max = maximum(num_sum1) 
    min = minimum(num_sum1) 
    return (max-min) 
#creates a variable that subtracts the maximum by the minimum 
print(difference([1,5,3]))
#subtracts the max - the min and prints the answer 