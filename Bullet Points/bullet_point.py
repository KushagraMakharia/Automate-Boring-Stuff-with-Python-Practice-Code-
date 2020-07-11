import pyperclip

text = pyperclip.paste() # Copies text from clipboard

text = text.split("\n") #Splits the text into list by seprating on basis of \n

# Add * at the begiining of every line in the list
for i in range(len(text)):
    text[i] = "* " + str(text[i])

# Joins the line within list by appending \n in between
text = "\n".join(text)

# Copies the modified text onto the clipboard
pyperclip.copy(text)
