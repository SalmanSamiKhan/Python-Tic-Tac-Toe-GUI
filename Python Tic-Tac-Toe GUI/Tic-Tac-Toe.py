from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe by Salman")
root.iconbitmap()
root.resizable(width=False, height=False)
root.geometry("410x440")

# Click
click = True
count=0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED) 
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def score():

    global winner
    winner=False


# Check X
    if(b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner=True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        winner=True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        winner=True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        winner = True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        winner = True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    elif(b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        winner = True
        messagebox.showinfo('Player X', 'Winner is X!!')
        disable_all_buttons()

    #Check O

    elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O'):
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O'):
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O'):
        b7.config(bg='red')
        b8.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O'):
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'):
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        b3.config(bg='red')
        b6.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'):
        b1.config(bg='red')
        b5.config(bg='red')
        b9.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

    elif(b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):
        b3.config(bg='red')
        b5.config(bg='red')
        b7.config(bg='red')
        winner = True
        messagebox.showinfo('Player O', 'Winner is O!!')
        disable_all_buttons()

# Check if tie
    if count == 9 and winner == False:
	    messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
	    disable_all_buttons()

#Button Click
def button_click(b):
    global click, count
    if b["text"]==" " and click==True:
        b["text"]="X"
        click =False
        count+=1
        score()
    elif b["text"]==" " and click==False:
        b["text"]="O"
        click =True
        count+=1
        score()

    else:
        messagebox.showerror('Tic-Tac-Toe by Salman', 'Hey! That box has already been selected\n Please pick another box!')



def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global click,count
    click=True
    count=0
    #Build button
    b1 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b1))
    b2 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b2))
    b3 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b3))

    b4 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b4))
    b5 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b5))
    b6 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b6))

    b7 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b7))
    b8 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b8))
    b9 = Button(root, text=" ",font=("Times 20 bold"), bg='gray', fg='black', height = 4, width=8,  command= lambda: button_click(b9))


    #Button Grid1

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='options', menu=options_menu)
options_menu.add_command(label="New game",command=reset)

reset()
root.mainloop()