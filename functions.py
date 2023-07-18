FILEPATH = 'todo.txt'


def get_todos(filepath=FILEPATH):
    """ Read Todos """
    with open(filepath, 'r') as file_read:
        todos_local = file_read.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write Todos """
    with open(filepath, 'w') as file_w:
        file_w.writelines(todos_arg)

# print(__name__)
if __name__ == "__main__":
    print("hello")
    print(get_todos())