import tkinter 
import tkinter.messagebox
import pickle
from datetime import datetime

root=tkinter.Tk()
root.title("ToDO List")

def add_task():

    task=entry_task.get()
    if task!="":
     current_time=datetime.now().strftime("%y-%m-%d  %H:%M:%S")
     formatted_task=f"{current_time}:   {task}"
     listbox_task.insert(tkinter.END,formatted_task)
     entry_task.delete(0,tkinter.END)
    
    else:
     tkinter.messagebox.showwarning(title="Warning" , message="you must enter a task before adding")

def del_task():
  try:
   task_index=listbox_task.curselection()[0]
   listbox_task.delete(task_index)
   
  except:
    tkinter.messagebox.showwarning(title="Warning", message="you must select a task")

def load_task():
  task=pickle.load(open("Mention/your/path","rb"))
  for tasks in task:
    listbox_task.insert(tkinter.END,tasks)
     

def save_task():
  task =listbox_task.get(0, listbox_task.size())
  
  pickle.dump(task,open("task.dat" , "wb"))



frame_task=tkinter.Frame(root)
frame_task.pack()

listbox_task=tkinter.Listbox(frame_task,height=10 ,width=70)
listbox_task.pack(side=tkinter.LEFT)


scrollbar_task=tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT ,fill=tkinter.Y)


listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.configure(command=listbox_task.yview)


entry_task=tkinter.Entry(root,width=70)
entry_task.pack()



button_add_task=tkinter.Button(root,text="ADD TASK" ,width=40 ,command=add_task , bg="green"  , fg="white" ,height=1)
button_add_task.pack()

button_del_task=tkinter.Button(root,text="DELETE TASK" ,width=40 ,command=del_task , height=1,bg="green" ,fg="white")
button_del_task.pack()

button_load_task=tkinter.Button(root,text="LOAD TASK" ,width=40 ,command=load_task , height=1, bg="green" , fg="white")
button_load_task.pack()
button_save_task=tkinter.Button(root,text="SAVE TASK" ,width=40 ,command=save_task, bg="green", fg="white" ,height=1)
button_save_task.pack()
root.mainloop()