# create a txt file to store data
user_count = 0
with open("./user_info_list.txt", "w") as info_file:
    while True:
        # Count amount of users
        user_count += 1
        print(f"User {user_count}: ")

        '''Ask user for 5 types of information'''

        # ask for user name
        user_name = input("Input User Name: ")
        info_file.write("Name: " + user_name + "\n")

        # ask for user age
        user_age = int(input("Input User Age: "))
        info_file.write("Age: " + str(user_age) + "\n")

        # ask user for favorite color
        user_color = input("Input User Favorite Color: ")
        info_file.write("Color: " + user_color + "\n")

        # ask user for favorite programming language
        user_language = input("Input User Favorite Programming Language: ")
        info_file.write("Language: " + user_language + "\n")

        # ask user for hobbies
        user_hobby = input("Input User Favorite Hobby: ")
        info_file.write("Hobby: " + user_hobby + "\n")

        info_file.write("----------------------------------------------------------\n")

        # Ask if they want to add another user
        will_add = input("Would you like to continue <Yes/No> :")
        will_add = will_add.lower()
        if will_add == "no":
            print("Goodbye!")
            break  # Exit the loop if the answer is 'no'
        elif will_add != "yes":
            print("Error! Please input <Yes, No>.")