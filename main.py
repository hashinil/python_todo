todos = []
while True:
    user_action = input("add or show")
    match user_action:
        case 'add':
            user_prompt = "Enter a todo:"
            todo = input(user_prompt)
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break:


