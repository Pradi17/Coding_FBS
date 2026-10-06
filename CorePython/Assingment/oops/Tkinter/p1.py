import tkinter as tk
root=tk.Tk()
root.title("Greeting Card ")
root.geometry("400x300")
labl=tk.Label(root,text="🍿🥞Happy Birdthday to U🍿🥞🎈",
              bg="Orange",
              font=("Script MT Bold",29)
              )
labl.pack(pady=200)
root.mainloop()