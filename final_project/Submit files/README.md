# FlashCards App

### Video Demo:  <https://youtu.be/l-XgbPg4_dw>

### Description:
This FlashCards app is a simple yet versatile tool designed to help users study and memorize information efficiently. It leverages Python to load flashcards from a CSV file and presents them in two different modes: a terminal-based view using the rich library for enhanced styling and a graphical user interface (GUI) view using tkinter.

Key Features:
1. CSV Import for Flashcards: The app reads flashcards from a CSV file where each line contains a question, answer pair. The file can either be passed as a command-line argument or selected interactively through a file dialog in GUI mode or via terminal input in the terminal mode.

2. Terminal View (with rich Library): 
   - The terminal view offers a minimalist but stylish experience with enhanced formatting and colors using the rich library.
   - Users are presented with a question and can type their answer. After submission, the app will inform the user whether their answer is correct or incorrect, and, if incorrect, will display the correct answer.
   - This view allows for fast, distraction-free studying in the command-line environment.

3. Graphical User Interface (GUI) View (using tkinter):
   - For users who prefer a graphical experience, the app provides a tkinter-based GUI. The flashcards are displayed in a window, and users can interact by clicking buttons to reveal answers and navigate between questions.
   - This mode includes file selection through a file dialog, making it easier for users unfamiliar with command-line interfaces.

4. Dynamic File Input Handling:
   - If no file is passed as a command-line argument, the app will automatically prompt the user to provide a file path. In terminal mode, this is done through text input, while the GUI mode uses a file dialog to help users select the appropriate CSV file.
   - If the file path is incorrect or the file does not exist, the app will allow the user to provide a new path or gracefully exit the program.


5. User Interaction in Terminal Mode:
   - In terminal mode, after the question is displayed, users can type their answer directly. The app provides immediate feedback, indicating whether the answer was correct or incorrect, followed by the correct answer if necessary. This functionality mimics real-time quiz feedback, making it an effective learning tool.

### CSV Format:
 Each flashcard should be formatted as follows: question, answer, with each pair on a new line. For example:
 ```
 What is the capital of France?, Paris
 What is 2+2?, 4
 ```