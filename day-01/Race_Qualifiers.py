
qualified = 0
total = 0

winner_name = ""
winner_time = 0
winning_time = ""

while True:
    name = input("Enter Athlete name (or x to finish): ")

    if name.lower() == "x":
        break

    time = input("Enter time (mm:ss): ")

    valid = True

    # time format
    if len(time) != 5:
        valid = False

    elif time[2] != ":":
        valid = False

    elif not time[0:2].isdigit() or not time[3:5].isdigit():
        valid = False

    else:
        minutes = int(time[0:2])
        seconds = int(time[3:5])

        if minutes < 0 or seconds > 59:
            valid = False

    # valid time
    if valid == False:
        print("Invalid time. Please enter mm:ss.")

    else:
        total_seconds = minutes * 60 + seconds

        total = total + 1

        # qualification (25 minutes or less)
        if total_seconds <= 1500:
            qualified = qualified + 1

        #  winner
        if winner_name == "" or total_seconds < winner_time:
            winner_name = name
            winner_time = total_seconds
            winning_time = time


# results
print("\n---- RACE RESULTS ----")

if total == 0:
    print("Nobody entered the race")

else:
    print("Winner:", winner_name, "(", winning_time, ")")
    print("Qualified:", qualified, "of", total)

    