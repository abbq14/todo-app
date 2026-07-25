import os
import sys
import tkinter as tk
from tkinter import font as tkfont

# ---- colors (dark theme) ----
BG = "#1e1e2e"       # window background
CARD = "#313244"     # a task row
TEXT = "#cdd6f4"     # normal text
MUTED = "#6c7086"    # dim text
BLUE = "#89b4fa"     # add button
GREEN = "#a6e3a1"    # a done task
RED = "#f38ba8"      # delete button

# save tasks.txt next to the program, whether it runs as a script or an .exe
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
FILENAME = os.path.join(BASE_DIR, "tasks.txt")


class CheckCircle(tk.Canvas):
    """A round checkbox, drawn by hand (no font symbol / emoji).
    Empty grey ring when pending, filled green with a check when done."""

    def __init__(self, parent, done, command):
        size = 24
        super().__init__(parent, width=size, height=size, bg=CARD,
                         highlightthickness=0, cursor="hand2")
        pad = 3
        if done:
            self.create_oval(pad, pad, size - pad, size - pad, fill=GREEN, outline=GREEN)
            # the checkmark, drawn as two short lines
            self.create_line(size * 0.30, size * 0.52,
                             size * 0.43, size * 0.66,
                             size * 0.72, size * 0.34,
                             fill=BG, width=2, capstyle="round", joinstyle="round")
        else:
            self.create_oval(pad, pad, size - pad, size - pad, outline=MUTED, width=2)
        self.bind("<Button-1>", lambda event: command())


def load_tasks():
    """Read tasks back from the file. Returns a list of dicts."""
    tasks = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                done, title = line.split("|", 1)
                tasks.append({"title": title, "done": done})
    except FileNotFoundError:
        pass  # no file yet just means no tasks
    return tasks


def save_tasks(tasks):
    """Write every task to the file, one per line as  done|title."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task['done']}|{task['title']}\n")


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = load_tasks()

        root.title("My Tasks")
        root.configure(bg=BG)
        root.geometry("420x560")
        root.minsize(360, 400)

        title_font = tkfont.Font(family="Segoe UI", size=20, weight="bold")
        self.row_font = tkfont.Font(family="Segoe UI", size=12)
        self.done_font = tkfont.Font(family="Segoe UI", size=12, overstrike=1)
        self.del_font = tkfont.Font(family="Segoe UI", size=15)

        # header
        tk.Label(root, text="My Tasks", bg=BG, fg=TEXT,
                 font=title_font).pack(pady=(20, 10))

        # input row (entry + Add button)
        input_frame = tk.Frame(root, bg=BG)
        input_frame.pack(fill="x", padx=20)

        self.entry = tk.Entry(input_frame, bg=CARD, fg=TEXT, insertbackground=TEXT,
                              relief="flat", font=self.row_font)
        self.entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
        self.entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(input_frame, text="Add", command=self.add_task, bg=BLUE, fg=BG,
                  activebackground=BLUE, relief="flat", font=self.row_font,
                  width=6, cursor="hand2").pack(side="right", ipady=4)

        # area where all the task rows go
        self.list_frame = tk.Frame(root, bg=BG)
        self.list_frame.pack(fill="both", expand=True, padx=20, pady=15)

        self.refresh()
        self.entry.focus()

    def add_task(self):
        text = self.entry.get().strip()
        if text == "":
            return
        self.tasks.append({"title": text, "done": "0"})
        self.entry.delete(0, "end")
        save_tasks(self.tasks)
        self.refresh()

    def toggle(self, index):
        # flip done <-> not done
        self.tasks[index]["done"] = "0" if self.tasks[index]["done"] == "1" else "1"
        save_tasks(self.tasks)
        self.refresh()

    def delete(self, index):
        del self.tasks[index]
        save_tasks(self.tasks)
        self.refresh()

    def refresh(self):
        # clear the list, then rebuild it from self.tasks
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        if len(self.tasks) == 0:
            tk.Label(self.list_frame, text="no tasks yet — add one above",
                     bg=BG, fg=MUTED, font=self.row_font).pack(pady=20)
            return

        for i, task in enumerate(self.tasks):
            done = task["done"] == "1"
            row = tk.Frame(self.list_frame, bg=CARD)
            row.pack(fill="x", pady=4)

            # round checkbox on the left
            CheckCircle(row, done, command=lambda i=i: self.toggle(i)).pack(
                side="left", padx=(10, 8), pady=10)

            # task title — greyed out and struck through when done
            tk.Label(row, text=task["title"], bg=CARD,
                     fg=MUTED if done else TEXT,
                     font=self.done_font if done else self.row_font,
                     anchor="w").pack(side="left", fill="x", expand=True)

            # delete: a subtle × that turns red on hover
            del_btn = tk.Label(row, text="×", bg=CARD, fg=MUTED,
                               font=self.del_font, cursor="hand2")
            del_btn.pack(side="right", padx=(6, 12))
            del_btn.bind("<Button-1>", lambda event, i=i: self.delete(i))
            del_btn.bind("<Enter>", lambda event, w=del_btn: w.config(fg=RED))
            del_btn.bind("<Leave>", lambda event, w=del_btn: w.config(fg=MUTED))


if __name__ == "__main__":
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()
