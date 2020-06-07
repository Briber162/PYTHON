#tkinter for indeed
#app_bot file used
import tkinter as tk
from app_bot import find_jobs  
def close_app():
    window.destroy()
def run_app():
    print('Taking input form User')
    user_city_from = str(from_city_entry.get())
    user_city_to = str(to_city_entry.get())
    
    print("Starting Chrome")
    bot=find_jobs()
    bot.find_url(user_city_from,user_city_to)
    

def caps_to(event):
    to_city1.set(to_city1.get().upper())
def caps_from(event):
    from_city1.set(from_city1.get().upper())

window=tk.Tk()
window.title("FIND JOBS")
window.geometry("600x400")
frame_header =tk.Frame(master=window,borderwidth=3,pady=2)
center_frame =tk.Frame(window,borderwidth=3,pady=5)
bottom_frame =tk.Frame(window,borderwidth=3,pady=5)
frame_header.grid(row=0,column=0)
center_frame.grid(row=1,column=0)
bottom_frame.grid(row=2,column=0)
header= tk.Label(frame_header, text='JOBS SCRAPPER TOOL',bg='blue',fg='white',height='3',width='50',font=("Helvetica 16 bold"))
header.grid(row=0,column=0)
frame_1=tk.Frame(center_frame,borderwidth=2,relief='sunken')
frame_2=tk.Frame(center_frame,borderwidth=2,relief='sunken')

from_city=tk.Label(frame_1,text="JOB TITLE:")
to_city=tk.Label(frame_2,text="JOB DESTINATION:")

from_city1=tk.StringVar()
to_city1=tk.StringVar()

from_city_entry=tk.Entry(frame_1,textvariable=from_city1,width=10)
from_city_entry.bind("<KeyRelease>",caps_from)
to_city_entry=tk.Entry(frame_2,textvariable=to_city1,width=10)
from_city_entry.bind("<KeyRelease>",caps_to)

button_run=tk.Button(bottom_frame,text="START",command=run_app,bg='dark green',fg='white',relief='raised',
                     width=10,font=('Helvetica 9 bold'))
button_run.grid(column=0,row=0,sticky='w',padx=100,pady=2)
button_close=tk.Button(bottom_frame,text="END",command=close_app,bg='dark red',fg='white',relief='raised',
                         width=10,font=('Helvetica 9 bold'))
button_close.grid(column=1,row=0,sticky='e',padx=100,pady=2)
frame_1.pack(fill='x',pady=2)
frame_2.pack(fill='x',pady=2)
from_city.pack(side="left")
from_city_entry.pack(side='left',padx=1)
to_city.pack(side="left")
to_city_entry.pack(side='left',padx=1)
window.mainloop()
