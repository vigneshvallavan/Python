import tkinter as tk
from tkinter.constants import END
from PyDictionary import PyDictionary

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Dictionary")

    # Setting Geometry of Tk window
    root.geometry("665x500")
    root.configure(background="gray")

    # meaning Label   
    meaning_label = tk.Label(root,text = "Meaning", bg = "gray", fg ="black")
    meaning_label.place(relx = 0.0,rely = 0.6)
    meaning_label.configure(font = ('Algerian',14))

    # Answer Text
    ans = tk.Text(root, height = 6, width = 57, bg = "light cyan")
    ans.place(relx = 0.0,rely = 0.67)
    ans.configure(font = ('Constantia',16))

    def meaning():

        ans.delete(1.0,END)

        if (word_field.get() != "") :

            word = word_field.get()
            dict1 = PyDictionary.meaning(word) # Gives result in dict{'Noun':'[meaning]'} foramat
            ans.insert(END,dict1)
            '''
            n = str(dict1['Noun'])
            ans.insert(END, n)

            v = str(dict1['Verb'])
            ans.insert(END, v)

            a = str(dict1['Adjective'])   
            ans.insert(END, a)    '''   
            
        else:
            print("Please Give Input")


    # create a word label
    word_label = tk.Label(root,text = "Enter the Word: ", bg = "gray", fg ="black")
    word_label.place(relx = 0.0,rely = 0.2)
    word_label.configure(font = ('Algerian',16))

    # Create a text box for the word
    word_field = tk.Entry(root)
    word_field.place(relx = 0.35, rely = 0.2)
    word_field.configure(font = ('Constantia',16))

    # Create a search button 
    search = tk.Button( root, text = 'Search', bg = "green", fg ="yellow", command = lambda:meaning()) 
    search.place(relx = 0.35,rely = 0.4)
    search.configure(font = ('Algerian',16))

    tk.mainloop()