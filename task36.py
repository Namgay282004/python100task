#Define a variable called "score" and get its value from user input.
#Check if the score is greater than or equal to 90, display "A".
#If the score is between 80 and 89 (inclusive), display "B".
#If the score is between 70 and 79 (inclusive), display "C".
#If the score is between 60 and 69 (inclusive), display "D".
#If the score is less than 60, display "F".
#for any other input, display "Invalid score".

score = int(input("enter your score: "))

if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif score < 60:
    print("F")
else:
    print("Invalid score")