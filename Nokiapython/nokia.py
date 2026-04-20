print('Welcome to your Nokiaphone')

print('Your Nokia menu map \nLet us help you learn about your new Nokia phone.\nThe menu map you see on the next two pages will take you through\n the main menu functions in the order that they appear on your phone. \nWe’ve included visuals of the 12 menu functions and they are numbered 1 - 13 so\n you can see the sequence at a glance. And right next to each menu function\n screen we’ve listed the special features in your Nokiaphone, also in order\n of appearance so they’ll be easyto find')


menu_list = input('Enter any number to view menu function list:')
print('List of menu functions')
print('1. Phone book\n2. Messages\n3. Chat \n4. Call register\n5. Tones')
print('6. Settings\n7. Call divert  ')     
print('8. SGames\n9. Calculator \n10.Reminders \n11. Clock \n12. Profiles \n13. SIM services' )

for choice in range(1, 11):
    choice = int(input('Enter number to select from the menu list:'))
    if choice ==1:
        print('Phone book\n1. Search\n2. Service Nos.\n3. Add name\n4. Erase\n5. Edit\n6. Assign tone\n7. Send b’card')
        print('8. Options \n1. Type of view\n2. Memory status \n9. Speed dials \n10. Voice tags')
        sub_menu = 0
        while sub_menu in range(11) :
            sub_menu = int(input('Enter 1 to 10:'))
            if sub_menu ==1:
                print('1. Search')
            elif sub_menu ==2 :
                print('2. Service Nos')
            elif sub_menu ==3:
                print('3. Add name')
            elif sub_menu ==4 :       
                print('4. Erase')
            elif sub_menu ==5 :
                print('5. Edit')
            elif sub_menu ==6:
                print('6. Assign tone')
            elif sub_menu ==7 :       
                print('7. Send b’card')
            elif sub_menu ==8 :
                print('8. Options\n1. Type of view\n2. Memory status')
                sub_menu = 0
                while sub_menu in range(3) :
                    sub_menu = int(input('Enter 1 or 2 to view option or 0 to go back :'))
                    if sub_menu ==1:
                        print('1. Type of view')
                    elif sub_menu ==2 :
                        print('2. Memory status')
                    elif sub_menu == 0:
                        break
                       
            '''elif sub_menu == 9:
                print('9. Speed dials')
            elif sub_menu ==10:       
                print('10. Voice tags')
            else:
                print('invalid selection')'''
    
    
    
    
    
    
    elif choice  ==2:
        print('Messages\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys')
        print('7. Message settings\n1. Set 12 \n1. Message centre number \n2. Messages sent as \n3. Message validity')
        print('2. Common \n1. Delivery reports\n2. Reply via same centre \n3. Character support\n8. Info service\n9. Voice mailbox number \n10.Service command editor')
        sub_menu = 0
        while sub_menu in range(8) :
            sub_menu = int(input('Enter 1 to 7:'))
            if sub_menu ==1:
                print('1. Write messages')
            elif sub_menu ==2 :
                print('2. Inbox')
            elif sub_menu ==3:
                print('3. Outbox')
            elif sub_menu ==4 :       
                print('4. Picture messages')
            elif sub_menu ==5 :
                print('5. Templates')
            elif sub_menu ==6:
                print('6. Smileys')
            elif sub_menu ==7 :       
                print('7. Message settings \n1. Set \n2. Common')
                sub_menu = 0
                while sub_menu in range(1, 3) :
                    sub_menu = int(input('Enter 1 or 2:'))
                    if sub_menu ==1:
                        print('1. Set \n1. Message centre number\n2. Messages sent as\n3. Message validity')
                        sub_menu = 0
                        while sub_menu in range(1, 4) :
                            sub_menu = int(input('Enter 1 to 3:'))
                            if sub_menu ==1:
                                print('1. Message centre number')
                            elif sub_menu ==2 :
                                print('2. Messages sent as')
                            elif sub_menu ==3:
                                print('3. Message validity')
                    elif sub_menu ==2 :
                            print('2. Common\n1. Delivery reports\n2. Reply via same centre\n3. Character support')
                    sub_menu = 0
                while sub_menu in range(1, 4) :
                    sub_menu = int(input('Enter 1 to 3:'))
                    if sub_menu ==1:
                        print('1. Delivery reports')
                    elif sub_menu ==2 :
                        print('2. Reply via same centre')
                    elif sub_menu ==3:
                        print('3. Character support')
                else:
                    break
    
    elif choice  ==3 :
        print('Chat')
    
    elif(choice==4):
        print('Call register\n1. Missed calls\n2. Received calls\n3. Dialled numbers \n4. Erase recent call lists \n5. Show call duration \n1. Last call duration\n2. All calls’ duration')
        print('3. Rec6eived calls’ duration\n4. Dialled calls’ duration \n 5. Clear timers\n6. Show call costs\n1. Last call cost \n2. All calls’ cost \n3. Clear counters')
        print('7. Call cost settings\n1. Call cost limit\n2. Show costs in\n8. Prepaid credit')
    elif choice ==5 :
        print('Tones\n1. Ringing tone \n2. Ringing volume \n3. Incoming call alert \n4. Composer \n5. Message alert tone \n6. Keypad tones \n7. Warning and game tones \n8. Vibrating alert \n9. Screen saver')
    elif choice ==6 :
        print('Settings\n1. Call settings\n2. Phone settings\n3. Security settings\n4. Restore factory settings')
        sub_menu = 0
        while sub_menu in range(5) :
            sub_menu = int(input('Enter 1 to 4:'))
            if sub_menu ==1:
                print('Call settings \n1. Automatic redial \n2. Speed dialling \n3. Call waiting options \n4. Own number sending \n5. Phone line in use \n6. Automatic answer')
            if sub_menu ==2 :
                print('2. Phone settings\n1. Language\n2. Cell info display \n3. Welcome note \n4. Network selection \n5. Lights 2 \n6. Confirm SIM service actions')
            elif sub_menu ==3:
                print('3. Security settings\n1. PIN code request \n2. Call barring service \n3. Fixed dialling \n4. Closed user group \n5. Phone security \n6. Change access code')
            elif choice ==4 :       
                print('4. Restore factory settings')
            else:
                print('Invalid') 
        
    elif(choice==7):
        print('7. Call divert')  
    
    elif(choice==8):
        print('8. Games')     
    
    elif(choice==9):
        print('9. Calculator')                
                
    elif(choice==10):
        print('10.Reminders') 
    
    elif(choice==11):
        print('11. Clock\n1. Alarm clock\n2. Clock settings\n3. Date setting\n4. Stopwatch\n5. Countdown timer\n6. Auto update of date and time')             
        
    elif(choice==12):
        print('12. Profiles') 
            
    elif(choice==13):
        print('13. SIM services') 
           
    else:        
        print('Invalid selection, Try again !!!')        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
