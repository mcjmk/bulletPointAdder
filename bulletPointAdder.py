#! python3
# bulletPointAdder.py - Adds bullet points to the start of each line of the clipboard text that is separated by '\n'.
import pyperclip
import sys

if __name__ == '__main__':

    text = pyperclip.paste().split('\n')
    if len(sys.argv) == 1:
        text[:] = ['* ' + line for line in text]

    elif len(sys.argv) == 2 and sys.argv[1] == 'o':
        text[:] = [str(i+1) + '. ' + line for i, line in enumerate(text)]

    text = '\n'.join(text)
    pyperclip.copy(text)
    print(text)
