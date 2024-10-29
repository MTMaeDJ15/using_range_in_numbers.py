# - ask the user to input a NUMBER ranges from 1 to 50
         # > Less than or equal to 50 = VALID
         # > Greater than or equal to 51 = INVALID
         # > User input is not limited unless it's invalid
# - ask the user to input again until the user input is invalid
# - when the user input is invalid
         # > Display how many inputted numbers are in the following range:
         # > VALID NUM. = ASK NEXT NUM.
         # > INVALID NUM. = DISPLAY THE TALLY OF INPUTS IN THE RANGES THEY BELONG
         # > ex. 
            # Display should be like this:
              # 1 to 10: 3, 5, 8, 9, 
              # 11 to 20: 11, 15, 18, 20
              # 21 to 30: 24, 26, 28, 30
              # 31 to 40: 35, 38, 39, 
              # 41 to 50: 43, 45, 46, 

def collect_data():
    data_entered = []  # This will be the list storage for the information inputted by the user.

    # Loop1: This is to ask the user to input a random number.
    while True:
        random_number = int(input("Enter a number: "))
        data_entered.append(random_number)  # This will store the first number.

    # Check if the last entered `another` number was greater than 50 to exit Loop 1 as well.
        if random_number > 50:
            print("Invalid")
            break  # This will stop loop 1.

        # Loop2: To ask for another number.
        while True:
            another = int(input("Enter a number: "))
            
            data_entered.append(another)  # This will store the other numbers inputted.

            if another > 50:
                print("Invalid")
                break  # This will stop loop 2.

        return data_entered

def categorize(data_entered):
    # Set of lists that will store the different range of number they belong in.
    one_to_ten = []
    eleven_to_twenty = []
    twentyone_to_thirty = []
    thirtyone_to_forty = []
    fortyone_to_fifty = []

    one_to_ten = data_entered
    eleven_to_twenty = data_entered
    twentyone_to_thirty = data_entered
    thirtyone_to_forty = data_entered
    fortyone_to_fifty = data_entered

    print("1 to 10:", one_to_ten)
    print("11 to 20:", eleven_to_twenty)
    print("21 to 30:", twentyone_to_thirty)
    print("31 to 40:", thirtyone_to_forty)
    print("41 to 50:", fortyone_to_fifty)


def main(): #To define the whole program collect, print, and categorize.
    data_entered = collect_data()
    print("\nList of Numbers Entered and Categorized in their own Range:")
    categorize(data_entered)

if __name__ == "__main__":
    main()


    



