import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()
root.title('PDF to TEXT')
root.iconbitmap('./logo.png')
root.resizable(False, False)


canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3, rowspan=3)

# Insert logo into the window
logo = Image.open('logo2.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text='Select a PDF file on your device to extract all its text', font='calibre')
instructions.grid(columnspan=3, column=0, row=1)

# Get the PDF file on device
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='calibre', bg='red', width=15, height=1)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

root.mainloop()
