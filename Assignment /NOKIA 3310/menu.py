phone_working = True
while phone_working:
    print("\nMAIN MENU\n0. Exit\n1. Phonebook\n2. Messages\n3. Chat\n4. Call Register\n5. Tones\n6. Settings\n7. Call Divert\n8. Games\n9. Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM Services\n")
    user_choice = int(input("Choose from the menu 0-13: "))
    match user_choice:
        case 0:
            phone_working = False
            print("Exiting the Phone Menu")

        case 1:
            inphonebook = True
            while inphonebook:
                print("\nPHONE BOOK\n0. Back to Main Menu\n1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b'card\n8. Options\n9. Speed Dials\n10. Voice tags\n")
                user_choice = int(input("Choose from the menu 0-10: "))
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
                            print("\nOPTIONS\n0. Back to PhoneBook\n1. Type of view\n2. Memory Status\n")
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
                                    print("Invalid Choice, Please choose from 0-2: ")

                    case 9:
                        print("9. Speed Dials")
                    case 10:
                        print("10. Voice tags")
                    case _:
                        print("Invalid Choice, Please choose from 0-10: ") 

        case 2:
            inmessages = True
            while inmessages:
                print("\nMESSAGE\n0. Back to Main Menu\n1. Write Messages\n2. Inbox\n3. Outbox\n4. Picture Messages\n5. Templates\n6. Smileys\n7. Message Settings\n8. Info Service\n9. Speed Dials\n10. Service Command Editor\n")
                user_choice = int(input("Enter your choice 0-10: "))
                match user_choice:
                    case 0:
                        inmessages = False
                        print("Back to Main Menu")
                    case 1:
                        print("1. Write Messages")
                    case 2:
                        print("2. Inbox")
                    case 3:
                        print("3. Outbox")
                    case 4:
                        print("4. Picture Messages")
                    case 5:
                        print("5. Templates")
                    case 6:
                        print("6. Smileys")

                    case 7:
                        inmessage_setting = True
                        while inmessage_setting:
                            print("\nMESSAGE SETTINGS\n0. Back to Messages\n1. Set\n2. Common\n")
                            user_choice = int(input("Enter the choice 0-2: "))
                            match user_choice:
                                case 0:
                                    inmessage_setting = False
                                    print("0. Back to Messages")
                                case 1:
                                    inset = True
                                    while inset:
                                        print("\nSET\n0. Back to Message Settings\n1. Message Center\n2. Messages sent as\n3. Message Validity\n")
                                        user_choice = int(input("Enter the choice 0-3: "))
                                        match user_choice:
                                            case 0:
                                                inset = False
                                                print("0. Back to Messages")
                                            case 1:
                                                print("1. Message Center")
                                            case 2:
                                                print("2. Messages sent as")
                                            case 3:
                                                print("3. Message Validity")
                                            case _:
                                                print("Invalid Choice, Please choose from 0-3: ")

                                case 2:
                                    incommon = True
                                    while incommon:
                                        print("\nCOMMON\n0. Back to Message Settings\n1. Delivery Reports\n2. Reply via same center\n3. Character Support\n")
                                        user_choice = int(input("Enter the choice 0-2: "))
                                        match user_choice:
                                            case 0:
                                                incommon = False
                                                print("0. Back to Messages")
                                            case 1:
                                                print("1. Delivery Reports")
                                            case 2:
                                                print("2. Reply via same center")
                                            case 3:
                                                print("3. Character Support")
                                            case _:
                                                print("Invalid Choice, Please choose from 0-3: ")

                                case _:
                                    print("Invalid Choice, Please choose from 0-2: ")
                                     
                    case 8:
                        print("8. Info Service") 
                    case 9:
                        print("9. Speed Dials") 
                    case 10:
                        print("10. Service Command Editor") 
                    case _:
                        print("Invalid Choice, Please choose from 0-10: ") 

        case 3:
            print("3. Chat")

        case 4:
            incall_register = True
            while incall_register:
                print("\nCALL REGISTER\n0. Back to Main Menu\n1. Missed Calls\n2. Received Calls\n3. Dialled Calls\n4. Erase Recent Call Lists\n5. Show Call Duration\n6. Show Call Costs\n7. Call Cost Settings\n8. Prepaid Credit\n")
                user_choice = int(input("Enter the choice 0-8: "))
                match user_choice:
                    case 0:
                        incall_register = False
                        print("Back to Main Menu")
                    case 1:
                        print("1. Missed Calls")
                    case 2:
                        print("2. Received Calls")
                    case 3:
                        print("3. Dialled Calls")
                    case 4:
                        print("4. Erase Recent Call Lists")
                    case 5:
                        show_call_duration = True
                        while show_call_duration:
                            print("\nSHOW CALL DURATION\n0. Back to Call register\n1. Last Call Duration\n2. All Calls' Duration\n3. Received Calls' Duration\n4. Dialled Calls' Duration\n5. Clear Timers\n")
                            user_choice = int(input("Enter the choice 0-5: "))
                            match user_choice:
                                case 0:
                                    show_call_duration = False
                                    print("Back to Call Register")
                                case 1:
                                    print("1. Last Call Duration")
                                case 2:
                                    print("2. All Calls' Duration")
                                case 3:
                                    print("3. Received Calls")
                                case 4:
                                    print("4. Dialled Calls' Duration")
                                case 5:
                                    print("5. Clear Timers")
                                case _:
                                    print("Invalid Choice, Please choose from 0-5: ")

                    case 6:
                        show_call_cost = True
                        while show_call_cost:
                            print("\nSHOW CALL COSTS\n0. Back to Call register\n1. Last Call Cost\n2. All Calls' Cost\n3. Clear Counters\n")
                            user_choice = int(input("Enter the choice 0-3: "))
                            match user_choice:
                                case 0:
                                    show_call_cost = False
                                    print("Back to Call Register")
                                case 1:
                                    print("1. Last Call Cost")
                                case 2:
                                    print("2. All Calls' Cost")
                                case 3:
                                    print("3. Clear Counters")
                                case _:
                                    print("Invalid Choice, Please choose from 0-3: ")

                    case 7:
                        incallcost_settings = True
                        while incallcost_settings:
                            print("\nCALL COST SETTINGS\n0. Back to Call register\n1. Call Cost Limit\n2. Show costs in\n")
                            user_choice = int(input("Enter the choice 0-2: "))
                            match user_choice:
                                case 0:
                                    incallcost_settings = False
                                    print("Back to Call Register")
                                case 1:
                                    print("1. Call Cost Limit")
                                case 2:
                                    print("2. Show costs in")
                                case _:
                                    print("Invalid Choice, Please choose from 0-2: ")

                    case 8:
                        print("8. Prepaid Credit") 
                    case _:
                        print("Invalid Choice, Please choose from 0-10: ")                    

        case 5:
            intones = True
            while intones:
                print("\nTONES\n0. Back to Main Menu\n1. Ringing Tone\n2. Ringing Volume\n3. Incoming Call Alert\n4. Composer\n5. Message Alert Tone\n6. Keypad Tones\n7. Warning and Game Tones\n8. Vibrating Alert\n9. Screen Saver\n")
                user_choice = int(input("Enter the choice 0-9: "))
                match user_choice:
                    case 0:
                        intones = False
                        print("Back to Call Main Menu")
                    case 1:
                        print("1. Ringing Tone")
                    case 2:
                        print("2. Ringing Volume")
                    case 3:
                        print("3. Incoming Call Alert")
                    case 4:
                        print("4. Composer")
                    case 5:
                        print("5. Message Alert Tone")
                    case 6:
                        print("6. Keypad Tones")
                    case 7:
                        print("7. Warning and Game Tones")
                    case 8:
                        print("8. Vibrating Alert")
                    case 9:
                        print("9. Screen Saver")
                    case _:
                        print("Invalid Choice, Please choose from 0-9: ")

        case 6:
            insettings = True
            while insettings:
                print("\nSETTINGS\n0. Back to Call Main Menu\n1. Call Settings\n2. Phone Settings\n3. Security Settings\n4. Restore Factory Settings\n")
                user_choice = int(input("Enter the choice 0-4: "))
                match user_choice:
                    case 0:
                        insettings = False
                        print("Back to Call Main Menu")

                    case 1:
                        incall_settings = True
                        while incall_settings:
                            print("\nCALL SETTINGS\n0. Back to Settings\n1. Automatic Redial\n2. Speed Dialing\n3. Call Waiting Options\n4. Own Number Sending\n5. Phone line in Use\n6. Automatic Answer\n")
                            user_choice = int(input("Enter the choice 0-6: "))
                            match user_choice:
                                case 0:
                                    incall_settings = False
                                    print("Back to Settings")
                                case 1:
                                    print("1. Automatic Redial")
                                case 2:
                                    print("2. Speed Dialing")
                                case 3:
                                    print("3. Call Waiting Options")
                                case 4:
                                    print("4. Own Number Sending")
                                case 5:
                                    print("5. Phone line in Use")
                                case 6:
                                    print("6. Automatic Answer")
                                case _:
                                    print("Invalid Choice, Please choose from 0-6: ")

                    case 2:
                        inphone_settings = True
                        while inphone_settings:
                            print("\nPHONE SETTINGS\n0. Back to Settings\n1. Language\n2. Cell Info Display\n3. Welcome Note\n4. Network Selection\n5. Lights\n6. Confirm SIM Service Actions\n")
                            user_choice = int(input("Enter the choice 0-6: "))
                            match user_choice:
                                case 0:
                                    inphone_settings = False
                                    print("Back to Settings")
                                case 1:
                                    print("1. Language")
                                case 2:
                                    print("2. Cell Info Display")
                                case 3:
                                    print("3. Welcome Note")
                                case 4:
                                    print("4. Network Selection")
                                case 5:
                                    print("5. Lights")
                                case 6:
                                    print("6. Confirm SIM Service Actions")
                                case _:
                                    print("Invalid Choice, Please choose from 0-6: ")

                    case 3:
                        insecurity_settings = True
                        while insecurity_settings:
                            print("\nSECURITY SETTINGS\n0. Back to Settings\n1. PIN Code Request\n2. Call Barring Service\n3. Fixed Dialing\n4. Closed User Group\n5. Phone Security\n6. Change Access Codes\n")
                            user_choice = int(input("Enter the choice 0-6: "))
                            match user_choice:
                                case 0:
                                    insecurity_settings = False
                                    print("Back to Settings")
                                case 1:
                                    print("1. PIN Code Request")
                                case 2:
                                    print("2. Call Barring Service")
                                case 3:
                                    print("3. Fixed Dialing")
                                case 4:
                                    print("4. Closed User Group")
                                case 5:
                                    print("5. Phone Security")
                                case 6:
                                    print("6. Change Access Codes")
                                case _:
                                    print("Invalid Choice, Please choose from 0-6: ")

                    case 4:
                        print("4. Restore Factory Settings")
                    case _:
                        print("Invalid Choice, Please choose from 0-4: ")
        case 7:
            print("7. Call Divert")

        case 8:
            print("8. Games")

        case 9:
            print("9. Calculator")

        case 10:
            print("10. Reminders")

        case 11:
            inclock = True
            while inclock:
                print("\nCLOCK\n0. Back to Main Menu\n1. Alarm Clock\n2. Clock Settings\n3. Date Setting\n4. Stopwatch\n5. Countdown Timer\n6. Auto Update of Date and Time\n")
                user_choice = int(input("Enter the choice 0-6: "))
                match user_choice:
                    case 0:
                        inclock = False
                        print("Back to Call Main Menu")
                    case 1:
                        print("1. Alarm Clock")
                    case 2:
                        print("2. Clock Settings")
                    case 3:
                        print("3. Date Setting")
                    case 4:
                        print("4. Stopwatch")
                    case 5:
                        print("5. Countdown Timer")
                    case 6:
                        print("6. Auto Update of Date and Time")
                    case _:
                        print("Invalid Choice, Please choose from 0-6: ")

        case 12:
            print("12. Profiles")

        case 13:
            print("13. SIM Services")

        case _:
            print("Invalid Choice, Please choose from 0-13")
