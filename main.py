def get_todos():
    with open('todo.txt', 'r') as file_read:
        todos_local = file_read.readlines()
    return todos_local

while True:
    user_action = input("add , edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todos = get_todos()

        todo = user_action[4:]+'\n'
        todos.append(todo)

        with open('todo.txt', 'w') as file_w:
            file_w.writelines(todos)
    elif user_action.startswith("edit"):
        try:
            user_index = int(user_action[5:])
            user_index = user_index - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[user_index] = new_todo+'\n'

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(todos)
        except ValueError:
            print("Your command is invalid!")
            continue
    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("complete"):
        try:
            user_index = int(user_action[9:])
            user_index = user_index - 1

            todos = get_todos()
            todo_to_remove = todos[user_index]
            todos.pop(user_index)

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(todos)
            message = f"removed: {todo_to_remove}"
            print(message)
        except IndexError:
            print("No Item")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")


print('bye')


