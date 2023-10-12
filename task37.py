#Define a variable called "month" and get its value from user input.
#Check if the month is "January", "February", "March", "April", or "May", display "Spring".
#f the month is "June", "July", "August", display "Summer".
#If the month is "September", "October", "November", display "Fall".
#If the month is "December", display "Winter".
#for any other input, display "Invalid month".

month = str(input("enter the month: "))
if month in ["January","February","March","April","May"]:
    print("Spring")
elif month in ["June","July","August"]:
    print("Summer")
elif month in ["September","October","November"]:
    print("Fall")
elif month in ["December"]:
    print("Winter")
else:
    print("Invalid month")