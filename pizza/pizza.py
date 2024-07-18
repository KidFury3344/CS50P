import sys
from tabulate import tabulate

def prettier(menu_path):
    try:
        if menu_path.endswith(".csv") == False:
            sys.exit("Not a CSV file")
        with open(menu_path) as f:
            menu = []
            for line in f:
                line = line.rstrip().split(",")
                menu.append(line)
            print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("Menu Not Found")
        
        
if __name__ == "__main__":
    try:
        menu_path = sys.argv[1]
        prettier(menu_path)
    except IndexError:
        sys.exit("Too Few Command Line Arguments")