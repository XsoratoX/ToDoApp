import tkinter as tk
from tkinter import ttk


class toDoApp(tk.Tk):
    _tasks = []

    def __init__(self):
        super().__init__()

        self.title("TODOリストアプリ")
        self.geometry("400x300")

        # input frame
        self.entry = ttk.Entry(self)
        self.entry.pack(fill="x", padx=10, pady=5)
        self.entry.bind("<Return>", self.add_task)

        # button
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", padx=10)

        ttk.Button(btn_frame, text="追加", command=self.add_task).pack(side="left")
        ttk.Button(btn_frame, text="削除", command=self.delete_task).pack(side="left")

        # toodoリスト
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

    # add a task
    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self._tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.deleta(0, tk.END)

    # delete a task
    def delete_task(self):
        selected_task = listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.listbox.delete(index)
            self._tasks.pop(index)


def main():
    app = toDoApp()
    app.mainloop()

if __name__ == "__main__":
    main()