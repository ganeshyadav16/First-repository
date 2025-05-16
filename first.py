import pandas as pd
import datetime

def menu():
    print("\nTo-Do List with Deadlines")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

def add_task(df):
    description = input("Enter task description: ")
    deadline = input("Enter task deadline (DD-MM-YYYY): ")
    try:
        deadline_date = datetime.datetime.strptime(deadline, "%d-%m-%Y")
        new_task = pd.DataFrame({
            'Description': [description],
            'Deadline': [deadline_date],
            'Completed': [False]
        })
        df = pd.concat([df, new_task], ignore_index=True)
        print("Task added successfully!")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
    return df

def view_tasks(df):
    if df.empty:
        print("No tasks available.")
    else:
        print("\nAll Tasks:")
        print(df)

def mark_task_completed(df):
    if df.empty:
        print("No tasks available to mark as complete.")
        return df
    print("\nAll Tasks:")
    print(df)
    try:
        task_num = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_num < len(df):
            df.at[task_num, 'Completed'] = True
            print(f"Task '{df.at[task_num, 'Description']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    return df


columns = ['Description', 'Deadline', 'Completed']
df = pd.DataFrame(columns=columns)
    
while True:
    menu()
    choice = input("Choose an option: ")

    if choice == '1':
        df = add_task(df)
    elif choice == '2':
            view_tasks(df)
    elif choice == '3':
        df = mark_task_completed(df)
    elif choice == '4':
        print("Exiting the To-Do List program.")
        break
    else:
        print("Invalid choice, please try again.")
