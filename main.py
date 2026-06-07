import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.title("To-Do List")
app.geometry("500x600")

BEIGE = "#F5F5DC"
PINK = "#FF69B4"
LIGHT_PINK = "#FFB6C1"
DARK_PINK = "#DB7093"

app.configure(fg_color=BEIGE)



def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    if not tasks:
        empty_label = ctk.CTkLabel(
            task_frame,
            text="No tasks yet 📭",
            font=("Segoe Script", 16),
            text_color=DARK_PINK
        )
        empty_label.pack(pady=20)
        return

    for index, task in enumerate(tasks):

        row = ctk.CTkFrame(task_frame, fg_color=LIGHT_PINK)
        row.pack(fill="x", pady=5, padx=5)

        var = ctk.BooleanVar(value=task["status"])

        def toggle_status(i=index, v=var):
            tasks[i]["status"] = v.get()

        checkbox = ctk.CTkCheckBox(
            row,
            text=task["task"],
            variable=var,
            command=toggle_status,
            font=("Segoe Script", 16),
            text_color="black",
            fg_color=PINK,
            hover_color=DARK_PINK
        )
        checkbox.pack(side="left", padx=10, pady=10)

        delete_btn = ctk.CTkButton(
            row,
            text="Delete",
            width=80,
            fg_color=PINK,
            hover_color=DARK_PINK,
            text_color="white",
            font=("Segoe Script", 12),
            command=lambda i=index: delete_task(i)
        )
        delete_btn.pack(side="right", padx=10)


def add_task():
    task_name = entry.get().strip()

    if task_name == "":
        messagebox.showerror("Error", "Task cannot be empty.")
        return

    for task in tasks:
        if task["task"].lower() == task_name.lower():
            messagebox.showwarning("Warning", "Task already exists.")
            return

    tasks.append({
        "task": task_name,
        "status": False
    })

    entry.delete(0, "end")
    refresh_tasks()


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        refresh_tasks()


def clear_all():
    if not tasks:
        messagebox.showinfo("Info", "Task list already empty.")
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:
        tasks.clear()
        refresh_tasks()

# ---------------- UI ----------------

title = ctk.CTkLabel(
    app,
    text=" TO-DO LIST",
    font=("Segoe Script", 30, "bold"),
    text_color=DARK_PINK
)
title.pack(pady=20)

entry_frame = ctk.CTkFrame(app, fg_color=BEIGE)
entry_frame.pack(pady=10, padx=20, fill="x")

entry = ctk.CTkEntry(
    entry_frame,
    placeholder_text="Enter a new task...",
    height=40,
    font=("Segoe Script", 15),
    fg_color="white",
    border_color=PINK,
    text_color="black"
)
entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)

add_btn = ctk.CTkButton(
    entry_frame,
    text="Add",
    width=100,
    fg_color=PINK,
    hover_color=DARK_PINK,
    font=("Segoe Script", 14),
    command=add_task   # ✅ FIXED
)
add_btn.pack(side="right", padx=10)

clear_btn = ctk.CTkButton(
    app,
    text="Clear All",
    fg_color=DARK_PINK,
    hover_color="red",
    font=("Segoe Script", 14),
    command=clear_all
)
clear_btn.pack(pady=10)

task_frame = ctk.CTkScrollableFrame(
    app,
    width=450,
    height=350,
    fg_color=BEIGE
)
task_frame.pack(padx=20, pady=10, fill="both", expand=True)

refresh_tasks()

app.mainloop()
