# create a txt file to store data
with open ("./user_info_list.txt", "w") as info_file:

# loop to ask user if they want to enter more information

    while True:

# ask user for 5 types of information

            

                


# insert user inputs into txt
# close loop 
        will_add = input("Would you like to continue<Yes/No> :")
        will_add = will_add.lower()
        if will_add == "no":
            print("Goodbye!")
            break  # Exit the loop if the answer is 'no'
        elif will_add != "yes":
            print("Error! Please input <Yes, No>.")    
# close file
