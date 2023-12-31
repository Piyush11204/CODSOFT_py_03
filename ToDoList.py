import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To_Do_application")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size(),)
    pickle.dump(tasks, open("tasks.dat", "wb",))


# Create GUI
frame_tasks = tkinter.Frame(root,bg ="#A9FFFB")
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=100,bg = '#A9FFFB',)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=70,bg = '#41A0F4')
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=70, command=add_task,bg="#95FF75")
button_add_task.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=70, command=save_tasks,bg="#5CFF4C")
button_save_tasks.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=70, command=load_tasks,bg="#F4FF4C")
button_load_tasks.pack()


button_delete_task = tkinter.Button(root, text="Delete task", width=70, command=delete_task,bg = '#FF1717')
button_delete_task.pack()



root.mainloop()