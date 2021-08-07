# v0.01 combat calendar, by adam roddick

# introduction to combat calendar
print("Welcome to Combat Calendar. Your one stop hub for seeing all your favorite upcoming events in your favorite combat sports!")
print("\nWould you like to see this week's events or last week's events? (this or last)")
print("Note: To exit at any time, type 'exit'")

# loop, will probs become functions soon
while True: 
    # take user input for loading events
    user_answer = input()
    if user_answer == "this":
        print("\nThis week's events:")
        tweek_file = open('this_week_event.txt')
        tweek_lines = tweek_file.readlines()
        count = 0
        for tw_line in tweek_lines:
            count += 1
            print(f"\t{count}. {tw_line.strip()}")
        continue
    # print this week's events
    elif user_answer == "last":
        print("Last week's events:")
        lweek_file = open('last_week_event.txt')
        lweek_lines = lweek_file.readlines()
        count = 0
        for lw_line in lweek_lines:
            count += 1
            print(f"\t{count}. {lw_line.strip()}")

        continue
    elif user_answer == "exit":
        break
    else:
        print("Please type either 'this' or 'last' please! To exit, type 'exit'")
