# opens file
try:
    with open("./user_info_list.txt", "r") as file:
        entire_txt = file.readlines()
        if_continue = "yes"
        
        while if_continue == "yes":
            if_found = 0
            find_name = input("Input The Name to get Information: ")

#Start searching for name
            index = 0

            # Use a while loop to search for the name in the text file
            while index < len(entire_txt):
                line = entire_txt[index]
                
                if find_name.strip() in line:
                    if_found += 1
                    # If name is found, print the next few lines (user's info)
                    print("----------------------------------------------------------")
                    for i in range(index, index + 6):  # Print the next 5 lines (name + 5 more details)
                        if i < len(entire_txt):  # Ensure the index is in bounds
                            
                            print(entire_txt[i], end='')

#move to next line if name not found
                    index += 6  # Skip 6 lines to avoid repeating the user's information
                else:
                    # Move to the next line if no match is found
                    index += 1

            if if_found == 0:
                print("Name not found!")
#ask to continue the search
            if_continue = input("Would you like to seek another person? yes/no ")
            while if_continue.lower().strip() not in ["yes", "no"]:
                if_continue = input("Would you like to seek another person? yes/no ")

except:
      print("An error occurred")