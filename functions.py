def get_todos(filepath='todo.txt'):
    """ Read Todos """
    with open(filepath, 'r') as file_read:
        todos_local = file_read.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todo.txt'):
    """ Write Todos """
    with open(filepath, 'w') as file_w:
        file_w.writelines(todos_arg)