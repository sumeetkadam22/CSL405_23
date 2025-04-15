from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='fr') #used deeptranslator..(googletrans not compatible with this py version) 
translated_text = translator.translate("Hello, how are you?")
print(translated_text)

root=Tk()
root.geometry("1100x320")  # dimensions of the window
root.resizable(0,0) #cannot be resized
root.iconbitmap(r"C:\Users\Sumeet\OneDrive\Desktop\Sumeet\translator\icon_ico_BGj_icon.ico")
root['bg']='crimson'

root.title('language translator')
Label(root, text="translator",font="Arial 20 bold").pack()

Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165,y=90)

input_text=Entry(root,width=60)
input_text.place(x=30,y=130)
input_text.get()

Label(root, text="Output", font='arial 13 bold',bg='white smoke').place(x=780,y=90)
Output_text=Text(root, font='arial 10', height=5, wrap= WORD, padx=5, pady=5, width=50)
Output_text.place(x=650, y=130)#output window

language = GoogleTranslator().get_supported_languages()
dest_lang=ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=160)
dest_lang.set('Choose Language')#language options

def translate():
    translator = GoogleTranslator(source='auto', target=dest_lang.get())  # Use deep_translator's GoogleTranslator
    translated_text = translator.translate(text=input_text.get())  # Get translation

    Output_text.delete(1.0, END)  # Clear output field
    Output_text.insert(END, translated_text)  # Insert translated text

# Corrected button creation (ensuring function name is correctly referenced)
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)

    


root.mainloop()
