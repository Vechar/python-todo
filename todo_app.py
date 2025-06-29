todo = []
user_input = ""

def add_todo(item):
    todo.append(item)
    return f"Added Task: {item}"

def list_todos():
    if todo:
        print("Todo List:")
        for i, item in enumerate(todo, start=1):
            print(f"{i}. {item}")
    else:
        print("Your todo list is empty.")

def remove_todo(index):
    try:
        if 0 <= index < len(todo):
            removed_item = todo.pop(index)
            print(f"Removed Task: {removed_item}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please provide a valid task number to remove.")

while user_input.lower() != "exit":
    user_input = input(">>> ")
    
    if user_input.lower() == "exit":
        print("Exiting the todo app.")
        break
    
    if user_input.lower().startswith("add "):
        item = user_input[4:].strip()
        if item:
            print(add_todo(item))
        else:
            print("Please provide a task to add.")
    if user_input.lower() == "list":
        list_todos()
    if user_input.lower().startswith("remove "):
        try:
            index = int(user_input[7:].strip()) - 1
            remove_todo(index)
        except ValueError:
            print("Please provide a valid task number to remove.")
    else:
        print("Unknown command. Use 'add <task>', 'list', 'remove <task number>', or 'exit'.")