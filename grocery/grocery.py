def grocery():
    grocery_list = []
    while True:
        try:
            item = input()
            grocery_list.append(item)
        except EOFError:
            break
    grocery_list.sort()
    grocery_set = set()
    for i in grocery_list:
        if i not in grocery_set:
            print(f"{grocery_list.count(i)} {i.upper()}")
            grocery_set.add(i)
        else:
            grocery_set.add(i)
            continue

grocery()