tasks = []

#function to display options to the user
def display_menu():
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete a task")
    print("4. Quit")

#function to add a task to the list
def add_task():
    new_task= input("What task would you like to add to the list? ") #Prompt user to add a new task to list.
    tasks.append(new_task) #add new task to list
    print(f"Task '{new_task}' added successfully.")#print confirmation message
    print(tasks) #print the updated list of tasks   

#function to view the tasks in the list
def view_tasks():
    print("Tasks in the list:")
    try:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        if len(tasks) == 0:
            print("No tasks in the list.")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")


#function to delete a task from the list
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    try:
        choice = int(input("Enter the number of the task you want to delete: "))
        if 1 <= choice <= len(tasks):
            deleted = tasks.pop(choice - 1)
            print(f"Task '{deleted}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    print("Updated tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

#main loop to run the program
while True: 
    display_menu() #show the user the menu options
    choice = input("Enter your choice (1-4): ") #prompt user to enter their choice
    if choice == "1":
        add_task() #call the function to add a task
    elif choice == "2":
        view_tasks() #call the function to view tasks
    elif choice == "3":
        delete_task() #call the function to delete a task
    elif choice == "4":
        print("Goodbye!") #print goodbye message and exit the program
        break
    else:
        print("Invalid choice. Please try again.") #print error message if input is invalid