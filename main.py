import customtkinter as ctk
import random

# ---------------- SETTINGS ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# ---------------- FONTS ----------------
FONT_TITLE = ("Helvetica", 26, "bold")
FONT_QUESTION = ("Helvetica", 16)
FONT_SCORE = ("Helvetica", 14, "bold")
FONT_RESULT = ("Helvetica", 14)

# ---------------- COLORS ----------------
BG_COLOR = "#0a192f"
PANEL_COLOR = "#112240"
PRIMARY_COLOR = "#64ffda"
ACCENT_COLOR = "#64ffda"
ERROR_COLOR = "#ff6b6b"
TEXT_COLOR = "#ccd6f6"

# ---------------- QUESTIONS ----------------
questions = [
    {"question": "What is the capital of France?", "answer": ["paris"]},
    {"question": "What planet is known as the Red Planet?", "answer": ["mars"]},
    {"question": "Which ocean is the largest on Earth?", "answer": ["pacific", "pacific ocean"]},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": ["william shakespeare", "shakespeare"]},
    {"question": "What is the chemical symbol for water?", "answer": ["h2o"]},
    {"question": "How many continents are there on Earth?", "answer": ["7", "seven"]},
    {"question": "What gas do plants absorb from the atmosphere?", "answer": ["carbon dioxide", "co2"]},
    {"question": "What is the largest planet in our solar system?", "answer": ["jupiter"]},
]

random.shuffle(questions)

current_question = 0
score = 0


def check_answer():
    global current_question, score

    user_answer = answer_entry.get().strip().lower()

    if user_answer in questions[current_question]["answer"]:
        score += 1
        result_label.configure(
            text="Correct! +1 point",
            text_color=ACCENT_COLOR
        )
    else:
        result_label.configure(
            text="Incorrect!",
            text_color=ERROR_COLOR
        )

    score_label.configure(text=f"Score: {score}/{len(questions)}")

    current_question += 1

    if current_question < len(questions):
        window.after(1000, show_question)
    else:
        window.after(1000, show_results)


def show_question():
    answer_entry.delete(0, "end")
    result_label.configure(text="")

    question_label.configure(
        text=f"Question {current_question + 1}/{len(questions)}\n\n"
             f"{questions[current_question]['question']}"
    )


def show_results():
    question_label.configure(
        text=f"🎉 Quiz Finished!\n\nFinal Score: {score}/{len(questions)}"
    )

    answer_entry.pack_forget()
    button_frame.pack_forget()

    result_label.configure(
        text="Great job!",
        text_color=ACCENT_COLOR
    )


def reset_quiz():
    global current_question, score

    score = 0
    current_question = 0

    random.shuffle(questions)

    answer_entry.pack(pady=10)
    button_frame.pack(pady=10)

    score_label.configure(text=f"Score: {score}/{len(questions)}")
    result_label.configure(text="", text_color=TEXT_COLOR)

    show_question()


def submit_with_enter(event):
    check_answer()



window = ctk.CTk()
window.title("General Knowledge Quiz")
window.geometry("700x500")
window.configure(fg_color=BG_COLOR)


title_label = ctk.CTkLabel(
    window,
    text="General Knowledge Quiz",
    font=FONT_TITLE,
    text_color=TEXT_COLOR
)
title_label.pack(pady=(25, 10))

score_label = ctk.CTkLabel(
    window,
    text=f"Score: {score}/{len(questions)}",
    font=FONT_SCORE,
    text_color=ACCENT_COLOR
)
score_label.pack()
question_frame = ctk.CTkFrame(
    window,
    fg_color=PANEL_COLOR,
    corner_radius=15,
    width=600,
    height=180
)
question_frame.pack(pady=20, padx=20)
question_frame.pack_propagate(False)

question_label = ctk.CTkLabel(
    question_frame,
    text="",
    font=FONT_QUESTION,
    wraplength=520,
    text_color=TEXT_COLOR,
    justify="center"
)
question_label.pack(expand=True)

# ---------------- ANSWER ENTRY ----------------
answer_entry = ctk.CTkEntry(
    window,
    width=350,
    height=40,
    font=("Helvetica", 14),
    placeholder_text="Type your answer here..."
)
answer_entry.pack(pady=10)

answer_entry.bind("<Return>", submit_with_enter)

# ---------------- BUTTONS ----------------
button_frame = ctk.CTkFrame(
    window,
    fg_color="transparent"
)
button_frame.pack(pady=15)

submit_button = ctk.CTkButton(
    button_frame,
    text="Submit Answer",
    command=check_answer,
    fg_color=PRIMARY_COLOR,
    text_color="black",
    hover_color="#4ddbc5",
    width=150
)
submit_button.grid(row=0, column=0, padx=10)

reset_button = ctk.CTkButton(
    button_frame,
    text="Reset Quiz",
    command=reset_quiz,
    fg_color=ERROR_COLOR,
    hover_color="#ff5252",
    width=150
)
reset_button.grid(row=0, column=1, padx=10)

# ---------------- RESULT LABEL ----------------
result_label = ctk.CTkLabel(
    window,
    text="",
    font=FONT_RESULT,
    text_color=TEXT_COLOR
)
result_label.pack(pady=15)

# ---------------- START QUIZ ----------------
show_question()

window.mainloop()