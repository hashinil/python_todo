while True:
    user_action = input("add , edit, show, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            file_r = open('todo.txt', 'r')
            todos = file_r.readlines()
            file_r.close()

            user_prompt = "Enter a todo: "
            todo = input(user_prompt)+'\n'
            todos.append(todo)

            file_w = open('todo.txt', 'w')
            file_w.writelines(todos)
            file_w.close()
        case 'edit':
            user_index = int(input("what item need to edit: "))
            user_index = user_index - 1
            new_todo = input("Enter a new todo: ")
            todos[user_index] = new_todo
        case 'show':
            file_s = open('todo.txt', 'r')
            todos = file_s.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'complete':
            user_index = int(input("what item need to complete: "))
            user_index = user_index - 1
            todos.pop(user_index)
        case 'exit':
            break

print('bye')


