# To-Do List Application in Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Added task:", task)

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print("Deleted task:", removed_task)
        else:
            print("Invalid task number. Please try again.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number you want to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
