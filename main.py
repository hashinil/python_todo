while True:
    user_action = input("add , edit, show, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            with open('todo.txt', 'r') as file_r:
                todos = file_r.readlines()

            user_prompt = "Enter a todo: "
            todo = input(user_prompt)+'\n'
            todos.append(todo)

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(todos)
        case 'edit':
            user_index = int(input("what item need to edit: "))
            user_index = user_index - 1

            with open('todo.txt', 'r') as file_r:
                todos = file_r.readlines()

            new_todo = input("Enter a new todo: ")
            todos[user_index] = new_todo+'\n'

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(todos)
        case 'show':
            with open('todo.txt', 'r') as file_s:
                todos = file_s.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'complete':
            user_index = int(input("what item need to complete: "))
            user_index = user_index - 1

            with open('todo.txt', 'r') as file_r:
                todos = file_r.readlines()
            todo_to_remove = todos[user_index]
            todos.pop(user_index)

            with open('todo.txt', 'w') as file_w:
                file_w.writelines(todos)
            message = f"removed: {todo_to_remove}"
            print(message)
        case 'exit':
            break

print('bye')


