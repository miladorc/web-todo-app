import streamlit as st
import functions_local as function


todos =  function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.push_todos(todos)

st.title("TODO list:")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        function.push_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new TODO...",
              on_change=add_todo, key='new_todo')