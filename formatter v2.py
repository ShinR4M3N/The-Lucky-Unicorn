def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


text_2 = input("Enter the statement you want to format: ")
symbol_2 = input("What symbol do you want to use: ")
print()
print((formatter(symbol_2, text_2)))
