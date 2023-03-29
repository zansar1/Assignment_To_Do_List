# Author: Zaid Ansari
# Date: 03/29/2023
# Purpose: The purpose of this app is to allow user to input university assignments with their due dates and display the assignments and the due dates
#======================================================================

# Define an empty list to store the assignments
assignments = []

# Define a function to add a new assignment to the list
def add_assignment():
    # Get the assignment name and due date from the user
    name = input("Enter the assignment name: ")
    due_date = input("Enter the due date (e.g. MM/DD/YYYY): ")
    
    # Add the assignment to the list
    assignments.append((name, due_date))
    
    # Print a message to confirm the assignment has been added
    print(f"Assignment '{name}' due on {due_date} has been added.")

# Define a function to display the list of assignments
def display_assignments():
    if not assignments:
        # If there are no assignments, print a message to inform the user
        print("There are no assignments yet.")
    else:
        # Otherwise, print the list of assignments
        print("Assignments:")
        for i, (name, due_date) in enumerate(assignments):
            print(f"{i+1}. {name} (due on {due_date})")

# Define a function to display the menu and get user input
def display_menu():
    print("Assignment To-Do List App\n")
    print("1. Add Assignment")
    print("2. Display Assignments")
    print("3. Exit\n")
    return input("Enter your choice (1-3): ")

# Loop until the user chooses to exit
while True:
    # Show the menu and get user input
    choice = display_menu()
    
    # Process the user's choice
    if choice == "1":
        # Add a new assignment
        add_assignment()
    elif choice == "2":
        # Display the list of assignments
        display_assignments()
    elif choice == "3":
        # Exit the program
        print("Goodbye!")
        break
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")