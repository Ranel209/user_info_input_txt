# opens file
try:
    with open("./user_info_list.txt", "r") as file:
        entire_txt = file.readlines()
        if_continue = "yes"
        
        while if_continue == "yes":
            if_found = 0
            find_name = input("Input The Name to get Information: ")
#Start searching for name
#loop to search for name
#if name found print next few lines
#move to next line if name not found
#ask to continue the search
except:
      print("An error occurred")