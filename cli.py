#from functions import get_todos,write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("add , edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todos = functions.get_todos()

        todo = user_action[4:]+'\n'
        todos.append(todo)

        functions.write_todos(todos)
    elif user_action.startswith("edit"):
        try:
            user_index = int(user_action[5:])
            user_index = user_index - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[user_index] = new_todo+'\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid!")
            continue
    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("complete"):
        try:
            user_index = int(user_action[9:])
            user_index = user_index - 1

            todos = functions.get_todos()
            todo_to_remove = todos[user_index]
            todos.pop(user_index)

            functions.write_todos(todos)
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


