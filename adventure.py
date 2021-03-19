def level_1():
    print("\n\tWhat do you want to do?")
    print("\t1. Check your family whatsapp group.")
    print("\t2. Read up on it from advertiser-backed news media.")
    print("\t3. Read up on it from independent news media.")
    print("\t4. Do not give a shit. It's not like voting makes a difference. Who cares who's in power, right?")
    print("\n\tEnter a number between 1-4.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            whatsapp()
            level_1()
        elif choice == "2":
            ad_news()
            break
        elif choice == "3":
            indie_news()
            break
        elif choice == "4":
            game_over()
        else:
            print("\n\tPlease enter a valid number between 1-4.")

def whatsapp():
    print("\nHere are the last few messages from the group:")
    print("\n* UNESCO has declared Indian national anthem as the best in the world.")
    print("* Look at this picture of India taken by NASA scientists during Diwali.")
    print("* And some relative posting 72 pictures of their baby.")
            
    print("\n\tWhat do you want to type in the group?")
    print("\t1. You type awwwww.")
    print("\t2. You post your own childhood pictures.")
    print("\t3. You mute the group.")
    print("\n\tEnter a number between 1-3.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            print("\nYou type awwwww, and then you close whatsapp.")
            break
        elif choice == "2":
            print("\nYou post your own childhood pictures, and then you close whatsapp.")
            break
        elif choice == "3":
            print("\nYou mute the group, and then you close whatsapp.")
            break
        else:
            print("\n\tPlease enter a valid number between 1-3.")

def ad_news():
    print("\nRecent headlines:")
    print("\n* Political spokesman saying if you don't like our country, then go to the neighbouring one.")
    print("* Some moral policing.")
    print("* Blaming a community.")
    print("* Changing a city name.")
    print("* Development of a religious building.")

    print("\n\tWhat do you want to do now?")
    print("\t1. I am ready to vote.")
    print("\t2. Read independent news media.")
    print("\n\tEnter a number between 1-2.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            game_over()
        elif choice == "2":
            print("Indie news")
            break
        else:
            print("\n\tPlease enter a valid number between 1-2.")

def indie_news():
    print("\nRecent headlines:")
    print("\n* Farmer's protests.")
    print("* Unemployment at an all time high.")
    print("* Judicial independence in danger.")
    print("* The country spent only 3% of its GDP on education in the past year.")
    print("\nThe independent news media runs a column debunking fake news.")

    print("\n\tWhat do you want to do now?")
    print("\t1. Read advertiser-backed news media.")
    print("\t2. Go ahead to Level 2.")
    print("\n\tEnter a number between 1-2.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            print("Ad news")
            break
        elif choice == "2":
            print("Level 2")
            break
        else:
            print("\n\tPlease enter a valid number between 1-2.")

def game_over():
    print("\nGame over.")
    exit(0)

print("Just because a country has problems, you don't elect the first dictator you see.")
print("\nYou belong to a minority community in your country.")
print("Elections are coming up. And you need to decide who are you going to vote for.")

level_1()
