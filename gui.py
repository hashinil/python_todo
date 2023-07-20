import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button("Add")
#edit_btn = sg.Button("Edit")
#comp_btn = sg.Button("Complete")
#exit_btn = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_btn]],
                   font=('Helvetica', 20))

while True:
    event, value = window.read()

    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
