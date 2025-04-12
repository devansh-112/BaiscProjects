# Initialize an empty task list
Task = []

def addtask():
    task = input("Enter the task you want to add to the list: ")
    Task.append(task)
    print(f"The task '{task}' has been successfully added.")

def listtask():
    if not Task:  
        print("There are no tasks added.")
    else:
        print("Your tasks:")
        for index, task in enumerate(Task):  
            print(f"{index}. {task}")

def deltask():
    listtask()  
    try:
        deltask1 = int(input("Enter the index of the task you want to delete: "))
        if deltask1 < 0 or deltask1 >= len(Task):  
            print("Invalid input. Index out of range.")
        else:
            deleted_task = Task.pop(deltask1)
            print(f"The task '{deleted_task}' has been deleted successfully.")
    except ValueError:  
        print("Invalid Input. Please enter a number.")

while True:
    print("\nEnter to Your Personalized To-Do List")
    print("------------------------------------------")
    print("What do you want to do in today's to-do list?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. List all tasks")
    print("4. Quit")
    print("-----------------------------------------------")
    
    try:
        choice = int(input("Enter your preferred choice (1-4): "))
        
        if choice == 1:
            addtask()
        elif choice == 2:  
            deltask()
        elif choice == 3:  
            listtask()  
        elif choice == 4:
            print("Exiting the to-do list application. Goodbye!")
            break 
        else:
            print("Invalid Input. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid Input. Please enter a number.")
