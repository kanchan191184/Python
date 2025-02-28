
GREEN = "\033[92m"
RED = "\033[31m"
BLUE = '\033[94m'
BOLD = '\033[1m'
ITALICS = '\033[3m'
UNDERLINE = '\033[4m'
RESET = "\033[00m"
CLEAR_SCREEN = "\033c"

# Foreground colors
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'


# Give the user some context. 
print (CLEAR_SCREEN)
print(FG_GREEN + BG_YELLOW + BOLD + "PASSWORD MANAGER" + RESET) 

# Set an initial value for choice other than the value for 'quit'. 

choice = '' 
#f = open("myfile.txt", "x")

# Start a loop that runs until the user enters the value for 'quit'. 
while choice != 'q': 

# Give all the choices in a series of print statements.  
    print("\n[a] Enter 'a' to Add Credentials.") 
    print("[v] Enter 'v' to View Credentials") 
    print("[q] Enter 'q' to quit.") 

# Ask for the user's choice. 
    choice = input("\nMake your choice:").lower().strip()

# Respond to the user's choice. 
    if choice == 'a': 
        print(CLEAR_SCREEN + "\nEnter your crendetials\n") 
        print("Please enter the following details")
        username = input("Username: ")
        password = input("Password: ")
        resource = input("Resource: ")
        print("You have entered: " + username +
              " " + password + " " + resource)
    elif choice == 'v': 
        print(CLEAR_SCREEN + "\nView your credentials\n") 
    elif choice == 'q': 
        print(CLEAR_SCREEN + "\nExiting the menu\n") 
    else: 
        print(FG_RED + "\nInvalid option, please try again.\n" + RESET) 

# Print a message that we are all finished. 
print("Program exit.") 

"""
#ROT3 Encryption

clearText = "myPassword" 
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, " 
encText = "".join([charSet[(charSet.find(c)+3)%95] for c in clearText]) 
print(encText) 

"""