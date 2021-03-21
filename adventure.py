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
    global fake_news
    fake_news = True

    if real_news == True:
        print("\nReferring to the column from the independent news media, you realise that the advertiser-backed news media is spreading a bunch of fake news.")
        print("Alright, enough with the news.")
        level_2()
    else:
        print("\n\tWhat do you want to do now?")
        print("\t1. I am ready to vote.")
        print("\t2. Read independent news media.")
        print("\n\tEnter a number between 1-2.")

        while True:
            choice = input("\t> ")

            if choice == "1":
                game_over()
            elif choice == "2":
                indie_news()
                break
            else:
                print("\n\tPlease enter a valid number between 1-2.")

def indie_news():
    print("\nRecent headlines:")
    print("\n* Farmer's protests.")
    print("* Unemployment at an all time high.")
    print("* Judicial independence in danger.")
    print("* The country spent only 3% of its GDP on education in the past year.")
    print("\nThe independent news media also runs a column debunking fake news.")
    global real_news
    real_news = True

    if fake_news == True:
        print("\nReferring to this column, you realise that the advertiser-backed news media is spreading a bunch of fake news.")
        print("Alright, enough with the news.")
        level_2()
    else:
        print("\n\tWhat do you want to do now?")
        print("\t1. Read advertiser-backed news media.")
        print("\t2. I'm done reading the news.")
        print("\n\tEnter a number between 1-2.")

        while True:
            choice = input("\t> ")

            if choice == "1":
                ad_news()
                break
            elif choice == "2":
                level_2()
                break
            else:
                print("\n\tPlease enter a valid number between 1-2.")

def level_2():
    print("\nA few days go by.")
    print("You are walking in the neighbourhood and you notice a politician campaigning in a nearby park.")

    print("\n\tWhat do you want to do?")
    print("\t1. Go and listen to the politician's speech.")
    print("\t2. Just take the biryani and bottle of whiskey and say you're going to vote for them.")
    print("\n\tEnter a number between 1-2.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            politician()
            break
        elif choice == "2":
            game_over()
        else:
            print("\n\tPlease enter a valid number between 1-2.")

def politician():
    print("\nPolitician's speech:")
    speech = "\n* The previous government didn't do shit.\n* We took revenge on our neighbouring country.\n* Some promises about development."
    print(speech)

    print("\n\tWhat do you want to do now?")
    print("\t1. Get on a motorcycle and join the rally. Screw traffic.")
    print("\t2. Ask the politician - What are the problems in this constituency and how are you going to solve them?")
    print("\n\tEnter a number between 1-2.")

    while True:
        choice = input("\t> ")

        if choice == "1":
            level_3()
            break
        elif choice == "2":
            print("\nPolitician's reply:")
            print(speech)
            print("\nRight.")
            level_3()
            break
        else:
            print("\n\tPlease enter a valid number between 1-2.")
     
def level_3():
    print("\nOnce the rally gets over, you leave.")
    print("\nYou are now hungry, so you get some food and you proceed home.")
    print("As you're walking home, some people start chasing you.")
    print("They shout at you – How dare you eat our holy animal?! And then they beat you up.")
    print("You go to the hospital to get yourself fixed.")

    print("\n\tNow, what do you want to do?")
    print("\t1. Go to the police and file a complaint.")
    print("\t2. Cry, and then go to the police and file a complaint.")
    print("\t3. Lose all hope.")
    print("\t4. Change your religion.")
    print("\t5. Move to a different country.")
    print("\t6. Become a vegan.")
    print("\n\tEnter a number between 1-6.")

    while True:
        choice = input("\t> ")

        if choice == "1" or choice == "2":
            police()
            break
        elif choice == "3" or choice == "4" or choice == "5" or choice == "6":
            game_over()
        else:
            print("\n\tPlease enter a valid number between 1-6.")
    
def police():
    print("""\nYou tell the police everything.
        \rThe police says – why did you have to eat the holy animal? You called this upon yourself.
        \rYou explain that you did not eat that animal. It's a misunderstanding. 
        \rThe police doesn't believe you. 
        \rYou are on your own.""")

    print("""\n\tNow, what do you want to do?
        1. Bribe the police to file a complaint.
        2. Move to the courts.
        3. Hire a bunch of goons to beat the guys who beat you up.
        \n\tEnter a number between 1-3.""")

    while True:
        choice = input("\t> ")

        if choice == "1" or choice == "3":
            game_over()
        elif choice == "2":
            print("""\nThe court rules in your favour, saying you are allowed to eat what you want to eat.
                \rAlso directs the police to arrest the people who beat you up.
                \nThe elections are here. And finally you vote, as if your life depends on it. Because it does.
                \rJust because a country has problems, you don't elect the first dictator you see.
                \nYou completed the game. Well done.
                """)
            break
        else:
            print("\n\tPlease enter a valid number between 1-3.")       

def game_over():
    print("\nGame over.")
    exit(0)

print("\nYou belong to a minority community in your country.")
print("Elections are coming up. And you need to decide who are you going to vote for.")

fake_news = False
real_news = False

level_1()
