import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

sg.theme("Black")
clock_lbl =sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_input")
add_btn = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos_list_box", enable_events=True, size=(45, 10))
edit_btn = sg.Button("Edit")
comp_btn = sg.Button("Complete")

exit_btn = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock_lbl],
                           [label],
                           [input_box, add_btn],
                           [list_box, edit_btn, comp_btn],
                           [exit_btn]],
                   font=('Helvetica', 14))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo_input'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list_box'].update(values=todos)
        case 'Edit':
            try:
                edit_todo = value['todos_list_box'][0]
                new_todo = value['todo_input']

                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos_list_box'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 10))
        case 'todos_list_box':
            window['todo_input'].update(value=value['todos_list_box'][0])
        case 'Complete':
            try:
                complete_todo = value['todos_list_box'][0]
                todos = functions.get_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['todos_list_box'].update(values=todos)
                window['todo_input'].update(value='')
            except IndexError:
                sg.popup("Select an item first", font=('Helvetica', 10))
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
