def level_1():
    print("Just because a country has problems, you don't elect the first dictator you see.")
    print("\nYou belong to a minority community in your country.")
    print("Elections are coming up. And you need to decide who are you going to vote for.")

    while True:
        choice = input("""
        What do you want to do?
        1. Check your family whatsapp group.
        2. Read up on it from advertiser-backed news media.
        3. Read up on it from independent news media.
        4. Do not give a shit. It's not like voting makes a difference. Who cares who's in power, right?
        
        Enter a number between 1-4.
        > """)

        if choice == "1":
            print("\nHere are the last few messages from the group:")
            print("\nUNESCO has declared Indian national anthem as the best in the world.")
            print("Look at this picture of India taken by NASA scientists during Diwali.")
            print("And some relative posting 72 pictures of their baby.")

            
            print("\n\tWhat do you want to type in the group?")
            print("\t1. You type awwwww.")
            print("\t2. You post your own childhood pictures.")
            print("\t3. You mute the group.")
            print("\n\tEnter a number between 1-3.")

            while True:
                whatsapp = input("\t> ")

                if whatsapp == "1":
                    print("\nYou type awwwww, and then you close whatsapp.")
                    break
                elif whatsapp == "2":
                    print("\nYou post your own childhood pictures, and then you close whatsapp.")
                    break
                elif whatsapp == "3":
                    print("\nYou mute the group, and then you close whatsapp.")
                    break
                else:
                    print("\nPlease enter a valid number between 1-3.")

        break

level_1()
