import csv
from os import path
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from tkinter import ttk, filedialog
import tkinter as tk
import sys
from time import sleep


def main():
    try:
        view = get_view()
        if view == "tkinter":
            path_to_csv = select_file_graphically()
            flashcards = file_read(path_to_csv)
            tkinter_view(flashcards)
        elif view == "commandline":
            path_to_csv = get_file()
            flashcards = file_read(path_to_csv)
            terminal_view(flashcards)
        else:
            print("Did you mean to exit? Press CTRL+C to exit or please select a view.")
            main()
    except KeyboardInterrupt:
        sys.exit("\nExited Program Successfully")


def file_read(path_to_csv):
    while True:
        try:
            with open(path_to_csv) as csvfile:
                reader = csv.reader(csvfile)
                flashcards = [row for row in reader]
            return flashcards
        except FileNotFoundError:
            user_continue_choice = (
                input("File not found. Do you want to specify another path? (y/n): ")
                .strip()
                .lower()
            )
            if user_continue_choice in ["y", "yes"]:
                path_to_csv = input("Enter path: ")
            else:
                sys.exit("Thank you for using the service.")


def select_file_graphically():
    try:
        file_path = sys.argv[1]
        return file_path
    except IndexError:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select a CSV File", filetypes=[("CSV Files", "*.csv")]
        )
        root.destroy()
        if not file_path:
            sys.exit("No file selected. Exiting.")
        return file_path


class FlashCardTkinter:
    def __init__(self, root, qa_list):
        self.root = root
        self.root.title("Quiz App")

        style = ttk.Style()
        style.configure(
            "TButton",
            padding=6,
            relief="flat",
            background="#4CAF50",
            foreground="black",
            font=("Segoe UI", 20),
        )
        style.configure("TLabel", font=("Segoe UI", 20))
        style.configure(
            "TProgressbar",
            thickness=20,
            troughcolor="#f0f0f0",
            background="#4CAF50",
            borderwidth=0,
        )

        self.qa_list = qa_list
        self.current_index = 0

        self.content_frame = ttk.Frame(self.root, padding="20")
        self.content_frame.grid(row=0, column=0, sticky="nsew")

        self.progress_frame = ttk.Frame(self.content_frame)
        self.progress_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.progress = ttk.Progressbar(
            self.progress_frame, orient="horizontal", length=400, mode="determinate"
        )
        self.progress.grid(row=0, column=0, sticky="ew")

        self.progress_text = ttk.Label(
            self.progress_frame,
            text=f"Question {self.current_index + 1} of {len(self.qa_list)}",
        )
        self.progress_text.grid(row=0, column=1, padx=(10, 0))

        self.question_label = tk.Label(
            self.content_frame,
            text=self.qa_list[self.current_index][0],
            wraplength=400,
            fg="red",
            font=("Segoe UI", 25),
        )
        self.question_label.grid(row=1, column=0, pady=(10, 5), sticky="ew")

        self.answer_label = tk.Label(
            self.content_frame,
            text=self.qa_list[self.current_index][1],
            fg="green",
            font=("Segoe UI", 25),
            wraplength=400,
        )
        self.answer_label.grid(row=2, column=0, pady=(5, 10), sticky="ew")
        self.answer_label.grid_forget()

        self.buttons_frame = ttk.Frame(self.root, padding="10")
        self.buttons_frame.grid(row=1, column=0, sticky="ew")

        self.quit_button = ttk.Button(
            self.buttons_frame, text="Quit", command=self.root.quit
        )
        self.quit_button.grid(row=0, column=0, padx=5, sticky="w")

        self.answer_button = ttk.Button(
            self.buttons_frame, text="Show Answer", command=self.show_answer
        )
        self.answer_button.grid(row=0, column=1, padx=5, sticky="e")

        self.next_button = ttk.Button(
            self.buttons_frame, text="Next Question", command=self.next_question
        )
        self.next_button.grid(row=0, column=2, padx=5, sticky="e")
        self.next_button.grid_forget()

        # Set window focus
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.after_idle(self.root.attributes, "-topmost", False)
        self.root.focus_force()

    def show_answer(self):
        self.question_label.config(text=self.qa_list[self.current_index][1], fg="green")
        self.answer_label.grid_forget()
        self.answer_button.grid_forget()
        self.next_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")

    def next_question(self):
        if self.current_index < len(self.qa_list) - 1:
            self.current_index += 1
            self.question_label.config(
                text=self.qa_list[self.current_index][0], fg="red"
            )
            self.answer_label.config(text=self.qa_list[self.current_index][1])
            self.answer_label.grid_forget()
            self.answer_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")
            self.next_button.grid_forget()
            self.update_progress()
        else:
            self.question_label.config(text="No more questions!")
            self.answer_label.grid_forget()
            self.answer_button.grid_forget()
            self.next_button.grid_forget()

    def update_progress(self):
        progress_value = (self.current_index + 1) / len(self.qa_list) * 100
        self.progress["value"] = progress_value
        self.progress_text.config(
            text=f"Question {self.current_index + 1} of {len(self.qa_list)}"
        )


def tkinter_view(flashcards):
    root = tk.Tk()
    app = FlashCardTkinter(root, flashcards)
    root.mainloop()


def terminal_view(flashcards):
    printer = Console()
    completed = 1
    total = len(flashcards)
    for cards in flashcards:
        printer.clear()
        with Progress(
            BarColumn(bar_width=None), TextColumn(f"Question {completed} Of {total}\n")
        ) as progress:
            question = progress.add_task(
                total=total,
                completed=completed,
                description=f"Question {completed} Of {total}\n",
            )
        completed += 1
        printer.print(cards[0], style="bold yellow")
        user_answer = printer.input("[bold][yellow]What is your answer? [/]").strip()
        if user_answer.upper() == cards[1].upper().strip():
            printer.print(
                f"[bold yellow]Your Answer was Correct:[/] [bold green]{user_answer}[/]\n"
            )
        else:
            printer.print(
                f"[yellow]Your Answer was Incorrect:[/] [red]{user_answer}[/]",
                style="bold red",
            )
            printer.print(
                f"[yellow]Correct Answer is:[/] [green]{cards[1].strip()}[/]\n",
                style="bold red",
            )

        status = (
            "Exiting"
            if flashcards.index(cards) == len(flashcards) - 1
            else "Next Question"
        )
        with Progress(
            TextColumn(
                "[bold yellow]{task.fields[status_message]} {task.fields[elapsed_time]}"
            ),
            BarColumn(bar_width=None),
            transient=True,
        ) as progress:
            wait = progress.add_task(
                "", total=3, elapsed_time="0:00", status_message=f"{status} in"
            )
            for elapsed in range(3):
                progress.update(
                    wait, advance=1, elapsed_time=f"{elapsed // 60}:{elapsed % 60:02d}"
                )
                sleep(1)
            if status == "Exiting":
                sys.exit("Thank You For Using!")


def get_file():
    if len(sys.argv) > 1:
        path_to_csv = sys.argv[1]
        if path.exists(path_to_csv) and path_to_csv.endswith(".csv"):
            return path_to_csv
        else:
            print("Specified path is not a CSV file.")
            sys.exit("Invalid file path. Exiting.")
    else:
        path_to_csv = input(
            "No file provided in command line. Please enter the path to the CSV file: "
        ).strip()
        if path.exists(path_to_csv) and path_to_csv.endswith(".csv"):
            return path_to_csv
        else:
            sys.exit("Invalid file path. Exiting.")


def get_view():
    print("1. For Graphical view")
    print("2. For Terminal view")
    view_choice = input("What View Would You Like? (1 or 2): ").strip()
    if view_choice == "1":
        return "tkinter"
    elif view_choice == "2":
        return "commandline"
    return


if __name__ == "__main__":
    main()
