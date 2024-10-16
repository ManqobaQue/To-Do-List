def main():
    tasks =[]
    while True:
        print("\n=====To-Do List=====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark as Done")
        print("4. Remove Task")
        print("5. Exit")
        
        choice =input("Enter your choice: ")
        
        if choice == '1':
            print()
            try:
                n_tasks = int(input("How many task you want to add: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            for i in range(n_tasks):
                task =input("Enter the task: ")
                tasks.append({"task": task,"done": False})
                print("Task Added!")
                
        elif choice == '2':
            print()
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
                
        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
                continue
            try:
                task_index = int(input("Enter the task number to mark as done: "))-1
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            if 0 <= task_index <len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                
        elif choice == '4':
            
            if not tasks:
                print("No tasks to remove.")
                continue

            try:
                index_task = int(input("Enter the task number to be removed: ")) - 1
            except ValueError:
                print("Please enter a valid number.")

            if 0 <= index_task < len(tasks):
                del tasks[index_task]
                print("Task removed")
            else:
                print("Invalid task number")
                
        elif choice == '5':
            print("Exiting the To-Do list.")
            break
        
        else:
            print("Invalid Choice. Please try again")
            
if __name__ == "__main__":
    main()
        