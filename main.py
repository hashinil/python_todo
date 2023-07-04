todos = []
while True:
    user_action = input("add , show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            user_prompt = "Enter a todo:"
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print('bye')


