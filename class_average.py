"""
Input the test scotes
Initiate an iterator (counter) and accumulator (sum) and set it to zero
Loop through the list test scores
Add all the test scores
Increment the counter by one
Once the loop ends, there are no more scores to add
Divide the accumulator (sum) by counter
Display the output to the user
Print the average of the class
"""

def calculate_average(scores):
    iterator = 0
    accumulator = 0
    scores_count = len(scores)

    while iterator < scores_count:
        accumulator = accumulator + scores[iterator]
        iterator = iterator + 1

    return accumulator / scores_count

def main():
    average = calculate_average([100, 80, 90, 70, 50, 95])
    print("The average of the class is:", round(average, 2))

main()