#This program will allow the user to view open invoices, submit payment for an open invoice, and see closed invoices on their fake account.
#version 1.3, Yvette Trujillo

from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.title('Payment Portal')
root.geometry("700x500")

#making the frame to the program to show it is a payment portal
frame = LabelFrame(root, text = "Welcome to Bakery Ingredients Payment Portal", padx=50, pady=50)
frame.pack(padx=10, pady=10)

#inserting a payment method picture 
my_img = Image.open("payments.jpg")
my_image= Image.open("thanks.jpg")
resized = my_img.resize((450, 300), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized)
my_label = Label( root, image = new_img )
my_label.pack()


#this will put in the information for the first window in the program that has all the open invoices for the user.
def first_win():
    window=Tk()
    window.title("Open Invoices")
    window.geometry("500x550")
    label_01=Label(window, text= 'Please see all open invoices below.').place(x=175, y=5)
    label_02=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 100\nAmount: $1,154.24\nDue On: 9/29/2021", justify="left").place(x=10, y=25)
    label_03=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 101\nAmount: $930.57\nDue On: 10/05/2021", justify="left").place(x=10, y=125)
    label_04=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 102\nAmount: $857.69\nDue On: 10/09/2021", justify="left").place(x=10, y=225)
    label_05=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 103\nAmount: $745.23\nDue On: 10/14/2021", justify="left").place(x=10, y=325)
    label_06=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 104\nAmount: $890.75\nDue On: 10/20/2021", justify="left").place(x=10, y=425)
    but_01=Button(window, text= "Exit Screen", command = window.destroy).pack(side=BOTTOM) #allows the user to close out the screen they're currently seeing.

#this is the second window that will allow the user to submit payments onto their account.
def second_win():
    def myfunction():
        entry_03.destroy() #these will remove the entries from user so they won't think it's still there being seen by everyone. 
        entry_04.destroy()
        entry_05.destroy()
        entry_06.destroy()
        entry_07.destroy()
        entry_08.destroy()
        entry_09.destroy()
        entry_10.destroy()
        entry_11.destroy()
        but_01.config(text="Thank you for your payment.")  #allows user to see that they have submitted for payment
    second_win=Tk()
    second_win.title("Payment Method")
    second_win.geometry("600x500")
    label_02=Label(second_win, text= 'Please enter your payment methods.')
    label_02.grid(row=0, column=10)
    label_03=Label(second_win, text="Enter your first name: ") #asks for user to enter their info for the following fields below
    entry_03= Entry(second_win, width=30)
    label_03.grid(row=7, column=10)
    entry_03.grid(row=7, column=10)
    label_03.grid(row=7, column=1)
    label_04=Label(second_win, text="Enter your Last name: ")
    entry_04= Entry(second_win, width=30)
    label_04.grid(row=10, column=10)
    entry_04.grid(row=10, column=10)
    label_04.grid(row=10, column=1)
    label_05=Label(second_win, text="Type of Credit card will you use: ")
    entry_05= Entry(second_win, width=30)
    label_05.grid(row=13, column=10)
    entry_05.grid(row=13, column=10)
    label_05.grid(row=13, column=1)
    label_06=Label(second_win, text="Enter your Credit Card Number: ")
    entry_06= Entry(second_win, width=30)
    entry_06.config(show="*")
    label_06.grid(row=16, column=10)
    entry_06.grid(row=16, column=10)
    label_06.grid(row=16, column=1)
    label_07=Label(second_win, text="Enter the expiration date: ")
    entry_07= Entry(second_win, width=30)
    label_07.grid(row=19, column=10)
    entry_07.grid(row=19, column=10)
    label_07.grid(row=19, column=1)
    label_08=Label(second_win, text="Enter the CCV: ")
    entry_08= Entry(second_win, width=30)
    label_08.grid(row=22, column=10)
    entry_08.grid(row=22, column=10)
    label_08.grid(row=22, column=1)
    label_09=Label(second_win, text="Enter your Zip Code: ")
    entry_09= Entry(second_win, width=30)
    label_09.grid(row=25, column=10)
    entry_09.grid(row=25, column=10)
    label_09.grid(row=25, column=1)
    label_10=Label(second_win, text="Enter Invoice Number: ")
    entry_10= Entry(second_win, width=30)
    label_10.grid(row=28, column=10)
    entry_10.grid(row=28, column=10)
    label_10.grid(row=28, column=1)
    label_11=Label(second_win, text="Enter Invoice Amount: ")
    entry_11= Entry(second_win, width=30)
    label_11.grid(row=31, column=10)
    entry_11.grid(row=31, column=10)
    label_11.grid(row=31, column=1)
    but_01=Button(second_win, text='Submit for Payment', command=myfunction) #submits payment and lets user know they have sent in payment onto their account
    but_01.grid(row=35, column=10)
    but_02=Button(second_win, text= "Exit Screen", command = second_win.destroy).place(x=240,y=300) #allows the user to close out the screen they're currently seeing.

#this is the third window that allows the user to see their closed invoices in the system. 
def third_win():
    window=Tk()
    window.title("Closed Invoices")
    window.geometry("500x550")
    label_03=Label(window, text= 'Please see all closed invoices below.').place(x=165, y=5) #show them a list of all their closed invoices
    label_02=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 095\nAmount: $658.45\nDue On: 9/01/2021", justify="left").place(x=10, y=25)
    label_03=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 096\nAmount: $758.96\nDue On: 09/06/2021", justify="left").place(x=10, y=125)
    label_04=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 097\nAmount: $896.75\nDue On: 09/13/2021", justify="left").place(x=10, y=225)
    label_05=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 098\nAmount: $1,125.78\nDue On: 09/19/2021", justify="left").place(x=10, y=325)
    label_06=Label(window, text= "Customer Name: Sweet Cookies\nCustomer Number: 2540\nInvoice Number: 099\nAmount: $765.86\nDue On: 09/24/2021", justify="left").place(x=10, y=425)
    but_03=Button(window, text= "Exit Screen", command = window.destroy).pack(side=BOTTOM) #allows the user to close out the screen they're currently seeing.


#this are the frames for the three different functions within the GUI.
b = Button(frame, text = "Open Invoices", command = first_win) #commands it to go into the first window
b2 = Button(frame, text = "Payment Method", command = second_win) #commands it to go into the second window
b3 = Button(frame, text = "Closed Invoices", command = third_win) #commands it to go into the third window
b.grid(row = 0, column = 0) #states where the button to each function will be set on the main page
b2.grid(row =0, column = 1)
b3.grid(row = 0, column = 2)
exitButton = Button(root, text= "Exit Program", command = root.destroy).pack() #allows for the application to be closed out altogether from the main menu

root.mainloop()


