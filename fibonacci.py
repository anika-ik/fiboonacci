# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:45:02 2022

@author: A
"""

from tkinter import *

root= Tk()
root.title("Fibonacci series")
root.geometry("400x400")



label_series= Label(root, text="fibonacci series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num= 10
    
    first_no= 0
    second_no= 1
    sum= 0 
    counter= 1
    
    while(counter <= num):
        label_series["text"]+= str(sum)+" "
        counter= counter+1
        first_no = second_no
        second_no= sum
        sum= first_no + second_no


    label_flower['text']= "flower is fully bloomed"
    label_spiral["text"]= "spirals in right direction are " + str(first_no)+" and spitals in left directions are " + str(second_no) + "\n total spiral are" + str(sum)
    

btn = Button(root, text='show fibonacci series', command=Fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()