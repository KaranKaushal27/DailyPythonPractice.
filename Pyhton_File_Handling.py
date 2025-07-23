with open("logfile.txt","w") as file:
    file.write("Log start: \n")
    file.write("System initialized: \n")

with open("logfile.txt", "a") as file:
    file.write("Uer loging at 10:00AM \n")
    file.write("User performed backup operations.\n")

with open("logfile.txt", "r") as file:
    content = file.read()
    print("final log content \n")
    print(content)

    
