# Create a function to open a text file for storing the user information.
# The file must be opened so that entered data is added to the data already in the file.
# Use a loop to read the current records from the text file and save the user ID into a list object for validation purposes.
def open_file():
    # Open the file
    user_file = open("user_info.txt", "a+")
    # Read the file
    user_file.seek(0)
    user_list = user_file.readlines()
    # Create a list to store the user IDs
    user_id_list = []
    # Loop through the file and store the user IDs in the list
    for user in user_list:
        user_id = user.split("|")
        user_id_list.append(user_id[0])
    # Return the list
    return user_id_list

# Create a function to use a loop that will obtain user input until terminated by the user typing “End.”
# Allow the user to input a user ID, password, and authorization code.
# Validate that the user ID does not already exist in the list object and that only “Admin” or “User” is entered as an authorization code.
# Write the user ID, password, and validation code as a pipe-delimited list to the text file and add the user ID to the list object if all validations have passed.
def user_input(user_id_list):
    # Create a loop to get user input
    while True:
        # Get the user ID
        user_id = input("Enter a user ID: ")
        # Check if the user ID is in the list
        if user_id in user_id_list:
            print("User ID already exists. Please try again.")
        # If the user ID is not in the list, get the password and authorization code
        else:
            password = input("Enter a password: ")
            auth_code = input("Enter an authorization code (Admin or User): ")
            # Check if the authorization code is valid
            if auth_code == "Admin" or auth_code == "User":
                # Open the file
                user_file = open("user_info.txt", "a+")
                # Write the user ID, password, and authorization code to the file
                user_file.write(user_id + "|" + password + "|" + auth_code + "\n")
                # Close the file
                user_file.close()
                # Add the user ID to the list
                user_id_list.append(user_id)
                # Ask the user if they want to enter another user
                another_user = input("Do you want to enter another user? (Y/N): ")
                # If the user does not want to enter another user, break out of the loop
                if another_user.upper() == "N":
                    break
            # If the authorization code is not valid, display an error message
            else:
                print("Invalid authorization code. Please try again.")

# Create a function that will open the text file that contains the user login information.
# Display the user ID, password, and authorization code for all users.
def display_users():
    # Open the file
    user_file = open("user_info.txt", "r")
    # Read the file
    user_list = user_file.readlines()
    # Loop through the file and display the user information
    print()
    for user in user_list:
        user_id, password, auth_code = user.split("|")
        print("User ID: " + user_id)
        print("Password: " + password)
        print("Authorization Code: " + auth_code)
    # Close the file
    user_file.close()

# Call the open_file function to get the user ID list
user_id_list = open_file()
# Call the user_input function to get the user input
user_input(user_id_list)
# Call the display_users function to display the user information
display_users()

