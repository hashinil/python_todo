import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_btn = sg.Button("Add")
edit_btn = sg.Button("Edit")
comp_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_btn], [edit_btn, comp_btn], [exit_btn]])
window.read()
window.close()
