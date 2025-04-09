#Reading a file and displaying its contents
try:
# Prompt the user to provide the name of an existing file
    filename = input(" Enter the file name to read: ")
    with open(filename, "r") as file:
        content = file.read()
        print(content) 
#Write the combined content into the new file  
    filename2 = input("Enter new file name to create: ")
    add_content = input("Write the content to add: " )
    with open(filename2, 'w') as file:
        mod_file = content + '\n' + add_content
        file.write(mod_file)      
    print(f"File created and contents added successfully. {mod_file}")
#Handle the scenario where the specified file is not found
except FileNotFoundError: 
    print("The specified file could not be found. Please check the file name and try again.")

