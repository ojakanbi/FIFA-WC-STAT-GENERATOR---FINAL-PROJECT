import time

'''
Name: OJ AKANBI
Course: IST 140
Assignment:LM8 Final CODING Assignment
'''


def menu():
    global menu_num
    menu_num = ['1', '2', '3', '4', '5', '6', '7']
    menus = [
        'Add Country Name', 'Add Starting 11', 'Add Subs', 'Add Fouls',
        'Add Final Score', 'Final Stat Display',
        'Exit'
    ]  # menu option list
    for menu_num, menu in enumerate(menus, start=1):
        print(menu_num, menu, "\n")


def add_teams():  # create the add team menu funtion
    global country_1  # set a global variable to call outside the function
    global country_2
    country_1 = input("Country 1 Name: ")
    country_2 = input("Country 2 Name: ")
    country_1 = country_1.title()
    country_2 = country_2.title()
    return country_1, country_2


def team1_11(first_name, last_name, number, pos):  # input the starting 11 for team 1
    global counter1, country1_str11
    counter1 += 1
    pos = pos.capitalize()
    full_name = last_name.title() + " " + first_name
    country1_str11["Player" + str(counter1)] = {
        "Name": full_name,
        "Position": pos,
        "ShirtNumber": number
    }


def team2_11(first_name, last_name, number, pos):  # input the starting 11 for team1
    global counter2, country2_str11
    counter2 += 1
    pos = pos.capitalize()
    full_name = last_name.title() + " " + first_name
    country2_str11["Player" + str(counter2)] = {
        "Name": full_name,
        "Position": pos,
        "ShirtNumber": number
    }


def display_starting11(team_dict):  # to display the starting 11 of a country
    for playerID, info in team_dict.items():
        for info, details in info.items():
            if info == 'Name':
                print(details, end=" ")
            if info == 'ShirtNumber':
                print(f"#{details}")


def add_fouls1():
    global foul_commit1
    for playerID, info in country1_str11.items():
        for info, details in info.items():
            if info == 'Name':
                full_squad1.append(details)  # list to add all the names of the players
    for _, infos in subs_team1.items():
        for infos, details in infos.items():
            if infos == 'Name':
                full_squad1.append(details)

    print(f"\t All players that were in the game for {country_1}")
    for players in full_squad1:
        print(players)

    name = input(f"what player from {country_1} commited a foul: ")
    card_color = input("Yellow or red card: ")
    name = name.title()
    card_color = card_color.title()
    foul_commit1.append(name + " " + card_color)
    print(foul_commit1)


def add_fouls2():
    global foul_commit2
    for playerID, info in country2_str11.items():
        for info, details in info.items():
            if info == 'Name':
                full_squad2.append(details)  # list to add all the names of the players
    for _, infos in subs_team2.items():
        for infos, details in infos.items():
            if infos == 'Name':
                full_squad2.append(details)

    print(f"\t All players that were in the game for {country_2}")
    for players in full_squad2:
        print(players)

    name = input(f"what player from {country_2} commited a foul: ")
    card_color = input("Yellow or red card: ")
    name = name.title()
    card_color = card_color.title()
    foul_commit2.append(name + " " + card_color)
    print(foul_commit2)


counter_sub1 = 0
counter_sub2 = 0
counter1 = 0
counter2 = 0
country1_str11 = {}
# country1_str11 = {'Player1': {'Name': 'Ronaldo', 'Position':'RB', 'ShirtNumber': '8'}, 'Player2' : {'Name': 'love', 'Position':'RB', 'ShirtNumber': '9'}}
country2_str11 = {}

subs_team1 = {}
subs_team2 = {}

full_squad1 = []
full_squad2 = []
foul_commit1 = []
foul_commit2 = []

# Application start

print("\t Welcome to FIFA World Cup Games Stats Generator")  # welcome message 
time.sleep(2)
print("\n  MENU OPTIONS - Start from option 1 through option 6 to generate Final Stat Display")
menu()  # introducing the menu option

user_input = input("Input an option # '1': ")  # user input of option

while user_input != '7':
    if user_input == '1':  # when user wants to enter country names
        add_teams()
        print(f"\nThis Final Stat generator is for: {country_1} VS {country_2} ")
        user_input = input("Input 2, to Add Starting 11: ")
    elif user_input == '2':  # when user wants to add starting 11
        print(f"\tEnter Starting 11 for Both Country")
        time.sleep(1)
        print(f"\nEnter Starting 11 for {country_1}")
        counting = 1
        for i in range(2):  # change range for how many players that should be entered
            first_name = input(f"what is player{counting} first name: ")
            last_name = input(f"what is player{counting} last name: ")
            number = input(f"what is player{counting} shirt #: ")
            pos = input(f"What is player{counting} position: ")
            print(" ")
            team1_11(first_name, last_name, number, pos)
            counting += 1

        print(f"\nEnter starting 11 for {country_2}")
        counting = 1
        for i in range(2):  # change range for how many players that should be entered
            first_name = input(f"what is player{counting} first name: ")
            last_name = input(f"what is player{counting} last name: ")
            number = input(f"what is player{counting} shirt #: ")
            pos = input(f"What is player{counting} position: ")
            print(" ")
            team2_11(first_name, last_name, number, pos)
            counting += 1
        print(f"\n\tStarting 11 for {country_1}")  # display the starting 11 after inputed
        display_starting11(country1_str11)
        print(f"\n\tStarting 11 for {country_2}")
        display_starting11(country2_str11)
        user_input = input("\nInput 3, to Add SUBS: ")
    elif user_input == '3':  # for when user wants to sub in players
        while user_input == '3':
            print(f"{country_1} = 1\n{country_2} = 2")
            who_sub = int(input("Which country is subbing 1 or 2:"))  # to see which team wants to sub
            if who_sub == 1:  # if team 1 wants to sub
                # counter_sub1 = 0
                print(f"\n\t\t{country_1} is subbing\n\t Current players ")
                display_starting11(country1_str11)  # display the starting 11
                print("\nWhat player do you want to sub out, input their first name")
                random_var = 0

                while random_var != 1:
                    sub_out = input("Enter here: ")
                    sub_out = sub_out.title()
                    for playerID, info in country1_str11.items():
                        for info, details in info.items():
                            if info == 'Name':
                                if sub_out not in details:  # finds to see if what user inputs is in the starting 11
                                    print("Player not in the starting 11")
                                else:
                                    random_var = 1

                                    print(f"Who do you want to sub {sub_out} with?")
                                    sub_in = input("Input name: ")
                                    sub_in = sub_in.title()
                                    sub_in_pos = input(f"What position does {sub_in} play? ")
                                    sub_in_pos = sub_in_pos.capitalize()
                                    print(f"{sub_in} in for {sub_out}")
                                    subs_team1["Sub" + str(counter_sub1)] = {"In": [sub_in, sub_in_pos],
                                                                             "Out": [sub_out]}  ##
                                    counter_sub1 += 1
                                    user_input = input("\nInput 3 to Add  another SUB or 4 to ADD Fouls: ")

            elif who_sub == 2:  # if team 2 wants to sub
                print(f"\n\t{country_2} is subbing\n\t Current players")
                display_starting11(country2_str11)
                print("\nWhat player do you want to sub out, input their first name")
                random_var = 0
                while random_var != 1:
                    sub_out = input("Enter here: ")
                    sub_out = sub_out.title()
                    for playerID, info in country2_str11.items():
                        for info, details in info.items():
                            if info == 'Name':
                                if sub_out not in details:  # finds to see if what user inputs is in the starting 11
                                    print("Player not in the starting 11")
                                else:
                                    random_var = 1

                                    print(f"Who do you want to sub {sub_out} with?")
                                    sub_in = input("Input name: ")
                                    sub_in = sub_in.title()
                                    sub_in_pos = input(f"What position does {sub_in} play? ")
                                    sub_in_pos = sub_in_pos.capitalize()
                                    print(f"{sub_in} in for {sub_out}")
                                    subs_team2["Sub" + str(counter_sub2)] = {"In": [sub_in, sub_in_pos],
                                                                             "Out": [sub_out]}
                                    counter_sub2 += 1
                                    user_input = input("\nInput 3 to Add  another SUB or 4 to ADD Fouls: ")
    elif user_input == '4':  # when user wants to add fouls
        while user_input == '4':
            print(f"{country_1} = 1\n{country_2} = 2")
            who_sub = int(input("Fouls input for which country 1 or 2:"))  # to see which team wants to sub

            if who_sub == 1:
                print(f"\tADD FOULS FOR {country_1}")
                add_fouls1()
                user_input = input("\nInput 4 to Add  another Foul or 5 to ADD final score: ")

            elif who_sub == 2:
                print(f"\tADD FOULS for {country_2}")
                add_fouls2()
                user_input = input("\nInput 4 to Add  another Foul or 5 to ADD final score: ")

    elif user_input == '5':  # when user wants to input final score
        print(f"\n\t Input the final Score of the game")
        country1_finalscore = input(f"What is {country_1} final score: ")
        country2_finalscore = input(f"what is {country_2} final score: ")
        print(f"\n\t {country_1} {country1_finalscore} - {country2_finalscore} {country_2}")
        user_input = input("\nInput 6 to reveal the final display: ")

    elif user_input == '6': # showing the final display
        dash = "-" * 10000
        print(dash)
        print(f"\n\t\tFIFA WORLD CUP FINAL STAT DISPLAY")
        print(f"\t\t     {country_1} VS {country_2}")

        print(f"\n\t {country_1} {country1_finalscore} - {country2_finalscore} {country_2}")

        print(f"\n\t\t STARTING 11 AND SUBS")
        print(f"\t\t{country_1}")
        display_starting11(country1_str11)
        print(f"\n\t SUBS")
        for playerID, info in subs_team1.items():
            for info, details in info.items():
                if info == 'In':
                    print(details[0], end=" ")
                if info == 'Out':
                    print(details[0])

        print(dash)

        print(f"\t\t{country_2}")
        display_starting11(country2_str11)
        print(f"\n\t SUBS")
        for playerID, info in subs_team2.items():
            for info, details in info.items():
                if info == 'In':
                    print(details[0], end=" ")
                if info == 'Out':
                    print(details[0])

        print(f"\n\t Fouls committed ")
        foul_commit1 = ",".join(foul_commit1)
        print(f"{country_1}: {foul_commit1}")

        foul_commit2 = ",".join(foul_commit2)
        print(f"{country_2}: {foul_commit2}")

        print("\n\t\tFIFA WORLD CUP STAT GENERATOR")

        user_input = input("Enter 7 to exit application: ")
