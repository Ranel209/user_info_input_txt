# create a txt file to store data
user_count = 0
with open ("./user_info_list.txt", "w") as info_file:

# loop to ask user if they want to enter more information

    while True:
#Count amount of users
        user_count += 1
        print(f"User {user_count}: ")

        '''ask user for 5 types of information'''

# close loop 
        will_add = input("Would you like to continue<Yes/No> :")
        will_add = will_add.lower()
        if will_add == "no":
            print("Goodbye!")
            break  # Exit the loop if the answer is 'no'
        elif will_add != "yes":
            print("Error! Please input <Yes, No>.")    