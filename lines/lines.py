import sys
import os.path as path

def count_lines(file_path):
    try:
        if file_path.endswith(".py") == False:
            sys.exit("Not A Python File")
        with open(file_path) as f:
            f = f.readlines()
        count = 0
        for line in f:
            if line.lstrip().startswith("#"):
                continue
            elif line.startswith("\n"):
                continue
            elif len(line.strip()) < 1:
                continue
            else:
                count += 1
        return count
    except FileNotFoundError:
        sys.exit("File Not Found")
        
if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            sys.exit("Too Many Command Line Arguments")
        file_path = sys.argv[1]
        print(count_lines(file_path))
    except IndexError:
        sys.exit("Too Few Command Line Arguments")