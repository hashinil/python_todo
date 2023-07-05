todos = []
while True:
    user_action = input("add , edit, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            user_prompt = "Enter a todo: "
            todo = input(user_prompt)
            todos.append(todo)
        case 'edit':
            user_index = int(input("what item need to edit: "))
            user_index = user_index - 1
            new_todo = input("Enter a new todo: ")
            todos[user_index] = new_todo
        case 'show':
            for index, item in enumerate(todos):
                print(index, '-', item)
        case 'exit':
            break

print('bye')


