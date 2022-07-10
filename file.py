# Files
###############

import os

# user is able to input
userEnters = input("Input a file to path:")

# Make sure the path exists
if os.path.exists(userEnters):
    path = userEnters.split("\\")
    container = "\\".join(path[:len(path)-1])
    backup = path[len(path)-1]

    blank = []
# Make sure the path is a text file
    if backup.endswith(".txt"):
        with open(container + "\\" + backup) as file:
            for line in file:
                blank.append(line)
                # goes through each line and put in blank list

        with open(container + "\\" + backup.replace(".txt", "") + "backup.txt.bak", "w") as file:
            for line in blank:
                file.write(line)
                # Puts every line that was in the blank list into the new backup file

    else:
        print("File not supported")
        # if the file is not a text file it won't work
else:
    print("Path does not exist")
    # the path needs to exist or it won't work
