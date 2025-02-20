def main():
    tasks = []
    while True:
        print("\n===== To-Do list =====")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Mark Task as Done")
        print("4.Exit")

        choice_ = input("Enter your choice:")

        if choice_ =='1':
            print()
            n_task = int(input("How may task you want add:"))

            for i in range(n_task):
                task = input("Enter your task:")
                tasks.append({"task":task,"done":False})
                print("Task added")
        elif choice_ == '2':
            print("\n Tasks:")
            for index, task in enumerate(tasks):
                status = "done" if task["done"] else "Not done"
                print(f"{index + 1}. {task['task']}-{status}")
        elif  choice_ == '3':
             task_index = int(input("Enter the task number to mark as done:"))
             if 0 <= task_index <len(tasks):
                 tasks[task_index]["done"] = True
                 print("Task marked as done!")
             else:
                 print("Invalid task number.")
        elif choice_ == '4':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice.Please try again.")
if __name__ == "__main__":
    main()