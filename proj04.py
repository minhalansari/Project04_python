#########################################################
#PROJECT 04
#get_ch function returns the character if it is single
#find_state function returns what the next state is 
#main function returns whether or not you are laughing
#main functoins uses the get_ch and find_state functions
##########################################################
def get_ch():
    ch = input("Enter a character or press the Return key to finish: ")
    while len(ch) >1:
        print("Invalid input, please try again.")
        ch = input("Enter a character or press the Return key to finish: ") 
    return ch   

def find_state(state, ch):
    sta= state
    if sta == 1:
        if ch == 'h':
            sta=2
            return sta
        else:
            sta =5 
            return sta
    if sta == 2:
        if ch == 'a' or ch =='o':
            sta=3
            return sta
        else:
            sta=5
            return sta
    if sta ==3:
        if ch == 'h':
            sta=2
            return sta
        elif ch == '!':
            sta=4
            return sta
        else :
            sta=5
            return sta
    if sta==4:
        if ch != '':
            sta=5
            return sta
    else:
        sta==5
        return sta
        
def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")
    state = 1
    ch = get_ch()
    string = ch
    while ch != '':
        state= find_state(state, ch)
        ch = get_ch()
        string += ch
    # call the functions in a loop
    # when user enters an empty string, you should print the results
    while state < 4:
        if state ==3:
                if ch == 'h':
                    state =2
            
                elif ch == '!':
                    state=4
            
                else :
                    state=5
    if state == 5:
        print("\nYou entered", string)
        print("You are not laughing.")
    elif state ==4:
        print("\nYou entered", string)
        print("You are laughing.")
    
      
        
main()
