import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Define ANSI escape codes for colors
RESET = "\033[0m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

# Replacement for logging functions
def print_info(message, *args):
    print(f"{BLUE}[{datetime.now()}] INFO: {message % args if args else message}{RESET}")

def print_success(message, *args):
    print(f"{GREEN}[{datetime.now()}] SUCCESS: {message % args if args else message}{RESET}")

def print_warning(message, *args):
    print(f"{YELLOW}[{datetime.now()}] WARNING: {message % args if args else message}{RESET}")

def print_error(message, *args):
    print(f"{RED}[{datetime.now()}] ERROR: {message % args if args else message}{RESET}")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

MORSE_CODE_DICT_REVERSE = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morse_to_text(morse):
    return ''.join(MORSE_CODE_DICT_REVERSE.get(code, '') for code in morse.split())

def encode():
    text = text_input.get()
    morse_output.set(text_to_morse(text))
    print_success("Encoded text to Morse: %s", text)

def decode():
    morse = text_input.get()
    text_output.set(morse_to_text(morse))
    print_success("Decoded Morse to text: %s", morse)

root = tk.Tk()
root.title("Morse Code Translator")
root.geometry("450x300")
root.resizable(False, False)
style = ttk.Style()
style.theme_use("clam")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Nhập văn bản hoặc mã Morse:", font=("Segoe UI", 12)).pack(pady=5)
text_input = ttk.Entry(main_frame, width=50)
text_input.pack(pady=5)

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Mã hóa Morse", command=encode).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Giải mã Morse", command=decode).grid(row=0, column=1, padx=5)

morse_output = tk.StringVar()
text_output = tk.StringVar()

ttk.Label(main_frame, text="Kết quả:", font=("Segoe UI", 12)).pack(pady=5)
result_label = ttk.Label(main_frame, textvariable=morse_output, foreground="blue", font=("Segoe UI", 12))
result_label.pack()
text_result_label = ttk.Label(main_frame, textvariable=text_output, foreground="green", font=("Segoe UI", 12))
text_result_label.pack()

root.mainloop()
