


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import cv2
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from PIL import *
from PIL import ImageTk, Image
import image
from tkinter import filedialog
import PIL
dataset = pd.read_csv('DATA1.csv')
root = Tk()  
root.iconbitmap('BRICK.ico')
root.title("BRICK COMPRESSIVE STRENGTH PREDICTOR") 
def open_img(): 

    global pr
    x = openfilename() 
    img1 = Image.open(x) 
    mean=np.mean(img1)
    median=np.median(img1)
    standard_deviation=np.std(img1)
    n=[[mean,median,standard_deviation]]
    X = dataset.iloc[:,0:3].values
    y = dataset.iloc[:,3].values
    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()
    (scaler_x.fit(X))
    xscale=scaler_x.transform(X)
    y=np.reshape(y, (-1,1))
    (scaler_y.fit(y))
    yscale=scaler_y.transform(y)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=57)
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train) 
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    pr=float(regressor.predict(n))
    label = tk.Label(root, fg="#fc6a03", bg="#cacaca")
    label.config(text='The Predicted Compressive Strength of the Brick is %.3f'%(pr)+' MPa', font=("Times New Roman", 20, 'bold'))
    label.place(x=350,y=355)
#cacaca
#d1d1d1
#e3e3e3
#cccccc
#fc6a03
#dd571c
def openfilename(): 
    filename = filedialog.askopenfilename(title ='PROJECT ') 
    return filename 


root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(width = True, height = True)
canvas = tk.Canvas(root, width = 1366, height = 768)
canvas.pack()
photo =ImageTk.PhotoImage(Image.open('123.jpg'))
canvas.create_image(0, 0,  anchor=NW, image=photo)
img = ImageTk.PhotoImage(Image.open("c2.png"))  
canvas.create_image(550, 100, anchor=NW, image=img)

canvas_text = canvas.create_text(450, 640, text='',fill='red', font=("Monotype Corsiva", 20,'bold'), anchor=tk.NW)

canvas.create_text(700,70,text="BRICK COMPRESSIVE STRENGTH PREDICTOR", font=("Monotype Corsiva", 35,'bold'))

btn = Button(root, text =' UPLOAD IMAGE & PREDICT', command = open_img)
btn.place(x=700,y=450)

root.mainloop() 







