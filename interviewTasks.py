import random

Monday = ("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN")
Tuesday = ("ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE")
Wednesday = ("GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE")
Thursday = ("BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN")
Friday = ("GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE")

totalOccurrences = Monday + Tuesday + Wednesday + Thursday + Friday

#distinct colors all through the week
uniqueColors = len(set(totalOccurrences))
#print(set(totalOccurrences))

#print(mondayColors, "\n", tuesdayColors, "\n", wednesdayColors, "\n", thursdayColors, "\n", fridayColors)
#Monday.count("GREEN") + Monday.count("")

'''computing the frequency mean'''

mean = len(totalOccurrences)/uniqueColors
print("1) the frequency mean is :", mean, "closest colors are red and orange")
# mean for the entire week is 7.91 and the closest colors are red and orange

'''computing the mode (mostly worn color)'''
# to get the most worn color through out the week:

frequency_dict = {i:totalOccurrences.count(i) for i in set(totalOccurrences)}
frequency_values = [frequency_dict[m] for m in frequency_dict.keys()]
print(frequency_dict)


for m,n in frequency_dict.items():
    if max(frequency_values) == n:
        print("2) the mostly worn color is :", m)
    #if totalOccurrences.count(i) == max()
    # #print(i, totalOccurrences.count(i))


'''computing the median'''
def compute_median(data: list):
    sorted_data = sorted(data)
    
    if (len(sorted_data) % 2 != 0):
        #print(sorted_data, ((len(sorted_data) - 1) // 2))
        print("3) the median color is:", sorted_data[(len(sorted_data) - 1) // 2]) 

compute_median(totalOccurrences)

'''   BONUS Get the variance of the colors '''
variance = (sum([(frequency_dict[i] - mean)**2 for i in set(totalOccurrences)])) / uniqueColors
print("4) the variance is :", variance)
    
'''    BONUS if a colour is chosen at random, what is the probability that the color is red?'''

pr_red = frequency_dict["RED"] / len(totalOccurrences)
print ("5) the probability that color is red is:", pr_red) #Ans = 0.094

'''write a recursive searching algorithm to search for a number entered by user in a list of numbers.
'''
print("7) the chosen recursive search algorithim is Binary search. Implementation is written below:")
def rec_search(list, target, left, right):
    if left > right:
        return -1  # Base case: Target not found
    
    mid = left + (right - left) // 2  # Avoids potential overflow
    
    if list[mid] == target:
        return mid  # Base case: Target found
    elif list[mid] < target:
        return rec_search(list, target, mid + 1, right)  # Search in right half
    else:
        return rec_search(list, target, left, mid - 1)  # Search in left half

'''8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.'''

import random

binaryNum = "".join([str(random.randint(0,1)) for i in range(4)])

# converting binary literal to decimal
decimalNum = int(binaryNum,2)
print("8) the randomly generated Binary Number in Decimal is:", decimalNum)

'''9.Write a program to sum the first 50 fibonacci sequence.'''
fib = []
def fibonacci_sum(n):
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        start = [0,1]
        for i in range(2,n):
            start.append(start[i-1] + start[i-2])
        return start[n-1]
    
print("9) The sum of the first 50 Fibonacci sequence is: ", fibonacci_sum(50))