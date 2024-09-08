# FlashCards App

### Video Demo:  <URL HERE>

### Description:

This is a simple python app I made which takes in a CSV file of Flashcards and then displays the questions followed by their answers either through a terminal view using ```rich``` or using ```tkinter``` for a GUI view.

The program can be provided the CSV file as a command line argument or the user will be prompted for the file either through the terminal for the terminal view or through a filedialog for the GUI view.

The CSV file Should be in the following format: 
```question, answer```

> A question string followed by a comma followed by an answer string followed by the next entry on the next line.

For the terminal view the program also supports asking the user for an answer and then returns whether or not the answer is correct or incorrect, followed by the correct answer should an answer be incorrect.