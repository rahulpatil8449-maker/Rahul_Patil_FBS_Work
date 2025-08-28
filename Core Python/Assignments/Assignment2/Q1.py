hrs = int(input("Enter the time in hours: "))
mins = int(input("Enter the time in minutes: "))
secs = int(input("Enter the time in seconds: "))

hours = hrs * 3600
minutes = mins * 60

seconds = hours + minutes + secs

print("The time after conversion into seconds will be: ", seconds)