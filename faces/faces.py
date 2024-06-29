user_text = input()
def convert(user_text):
    user_text = user_text.replace(":)", "🙂")
    converted_text = user_text.replace(":(" , "🙁")
    print(converted_text)
convert(user_text)
