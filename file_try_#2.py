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

    one_to_ten = data_entered[0:10]
    eleven_to_twenty = data_entered[10:20]
    twentyone_to_thirty = data_entered[20:30]
    thirtyone_to_forty = data_entered[30:40]
    fortyone_to_fifty = data_entered[40:50]

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
