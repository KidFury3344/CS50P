import sys
import csv

def name_sep(old_file, new_file):
    try:
        with open(old_file) as f:
            f = csv.DictReader(f)
            temp = []
            for row in f:
                temp.append({"name": row["name"].split(","), "house": row["house"]})
        with open(new_file, "w") as F:
            F = csv.DictWriter(F,fieldnames=["first", "last", "house"])
            F.writeheader()
            for i in range(len(temp)):
                F.writerow({"first":temp[i]["name"][1].strip(),"last":temp[i]["name"][0],"house":temp[i]["house"]})
        print(F)
    except FileNotFoundError:
        sys.exit("File Not Found.")
        
if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            sys.exit("Too Many Command Line Arguments.")
            
        name_sep(sys.argv[1], sys.argv[2])
    except IndexError:
        sys.exit("Too Few Command Line Arguments.")