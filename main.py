todos = []
while True:
    user_action = input("add or show")
    match user_action:
        case 'show':
            print(todos)
        case 'add':
            user_prompt = "Enter a todo:"
            todo = input(user_prompt)
            todos.append(todo)


