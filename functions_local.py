FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_list_local = file_local.readlines()
    return todos_list_local

def push_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def show(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        for index, item in enumerate(file_local):
            print(f"{index + 1}.{item.strip('\n')}")



# def add(user_action):
#     """this function add new item to the list"""
#     #new_item = user_action[4:] + "\n"
#     new_item = user_action
#     todos = get_todos()
#
#     todos.append(new_item)
#
#     push_todos(todos)
#
#     show()
#
# def edit(user_action):
#     number_edit = int(user_action[4:]) - 1
#
#     todos = get_todos()
#
#     new_item = input("enter new todo:")
#     todos[number_edit] = new_item + "\n"
#
#     push_todos(todos)
#
#     show()
#
# def complete(user_action):
#     completed = int(user_action[8:]) - 1
#     todos = get_todos()
#
#     todos.pop(completed)
#
#     push_todos(todos)
#
#     show()

if __name__ == "__main__":
    print("test")
