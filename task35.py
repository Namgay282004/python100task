#Define a variable called "day" and get its value from user input.
#Check if the day is "Monday", "Tuesday", "Wednesday", or "Thursday", display "Weekday".
#If the day is "Friday", display "TGIF".
#If the day is "Saturday" or "Sunday", display "Weekend".
#For any other input, display "Invalid input".

day = str(input("Day: "))

if day in ["Monday", "Tuesday", "Wednesday", "Thrusday"]:
    print("Weekday")
if day == "Friday":
    print("TGIT")
if day in ["Saturday", "Sunday"]:
    print("Weekends")
else:
    print("Invalid input")