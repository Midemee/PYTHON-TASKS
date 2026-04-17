phone_working = True
while phone_working:
    print("MAIN MENU\n0. Exit\n1. Phonebook\n2. Messages\n3. Chat\n4. Call Register\n5. Tones\n6. Settings\n7. Call Divert\n8. Games\n9. Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM Services")
    user_choice = int(input("Choose from the menu 0-13: "))
    match user_choice:
        case 0:
            phone_working = False
            print("Exiting the Phone Menu")

        case 1:
            inphonebook = True
            while inphonebook:
                print("Phone Book\n0. Back to Main Menu\n1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b'card\n8. Options\n9. Speed Dials\n9. Speed Dials")
                user_choice = int(input("Choose from the menu 0-13: "))
                match user_choice:
                    case 0:
                        inphonebook = False
                        print("Back to Main Menu")
                    case 1:
                        print("1. Search")
                    case 2:
                        print("2. Service Nos")
                    case 3:
                        print("3. Add name")
                    case 4:
                        print("4. Erase")
                    case 5:
                        print("5. Edit")
                    case 6:
                        print("6. Assign tone")
                    case 7:
                        print("7. Send b'card")

                    case 8:
                        inoptions = True
                        while inoptions:
                            print("Options\n0. Back to PhoneBook\n1. Type of view\n2. Memory Status")
                            user_choice = int(input("Enter your choice 0-2: "))
                            match user_choice:
                                case 0:
                                    inoptions = False
                                    print("0. Back to PhoneBook Menu")
                                case 1:
                                    print("1. Type of view")
                                case 2:
                                    print("2. Memory Status")
                                case _:
                                    print("Invalid Choice, Please choose from 0-2")

                    case 9:
                        print("9. Speed Dials")
                    case 10:
                        print("9. Speed Dials")
                    case _:
                        print("Invalid Choice, Please choose from 0-10") 

        case 2:
            print("2. Messages")

        case 3:
            print("3. Chat")

        case 4:
            print("4. Call Register")

        case 5:
            print("5. Tones")

        case 6:
            print("6. Settings")

        case 7:
            print("7. Call Divert")

        case 8:
            print("8. Games")

        case 9:
            print("9. Calculator")

        case 10:
            print("10. Reminders")

        case 11:
            print("11. Clock")

        case 12:
            print("12. Profiles")

        case 13:
            print("13. SIM Services")

        case _:
            print("Invalid Choice, Please choose from 0-13")







