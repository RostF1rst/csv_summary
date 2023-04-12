import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd

tk.Tk().withdraw()

try:
    messagebox.showinfo('CSV summary', 'Choose your CSV')
    filename = askopenfilename()
    if not filename:
        raise Exception('No file chosen')
    if not filename.endswith('.csv'):
        raise Exception('Chosen file is not CSV')

    messagebox.showinfo('CSV summary', 'Now choose file where you want to save the summary')
    save_file = askopenfilename()
    if not save_file:
        raise Exception('No file chosen')

    data = pd.read_csv(filename)
    result = {}

    for key in data.keys():
        sorted_answers = {}
        for i in data.get(key):
            try:
                sorted_answers[i] = int(sorted_answers.get(i)) + 1
            except TypeError as e:
                sorted_answers[i] = 1
        result[key] = sorted_answers

    str_res = ('-' * 100) + '\n'
    for k, v in result.items():
        str_res += '{}:\n'.format(k)
        for k1, v1 in v.items():
            str_res += '    {}: {}\n'.format(k1, v1)
        str_res += ('-' * 100) + '\n'

    print(str_res)

    with open(save_file, 'w', encoding='utf-16') as f:
        f.write(str_res)

    messagebox.showinfo('Success', 'Summary was successfully stored in {}'.format(save_file))

except Exception as e:
    messagebox.showerror('Error', str(e))
