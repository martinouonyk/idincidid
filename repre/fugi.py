import tkinter as tk

parent_view = tk.Tk()
child_view1 = tk.Label(parent_view, text="Child 1")
child_view1.pack()
child_view2 = tk.Label(parent_view, text="Child 2")
child_view2.pack()
