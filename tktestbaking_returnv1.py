# 分頁
import pandas as pd
import numpy as np
import tkinter as tk
import os
import tensorflow as tf

from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'

#initial
spacei = 10
spacec = 160
#y
row0 = 45
row1 = row0 + 35
row2 = row1 + 27
row3 = row2 + 35
row4 = row3 + 27
row5 = row4 + 30
row6 = row5 + 27
row7 = row6 + 32
row8 = row7 + 150


#x
column0 = spacei + 42
column1 = column0 - 35
#Egg
column2 = column0 + 14 

column3 = column0 + spacec 
column3_1 = column0 + spacec - 40
column4 = column3 -43

column5 = column3 + spacec
# column5_1 = column3 + spacec - 40
column6 = column5 -50


column7 = column5 + spacec
# column5_1 = column3 + spacec - 40
column8 = column7 -55

recipestr = ''
BS = 32
labelname = ["bread", "cake", "cookie","croissant"]
# df = pd.read_csv('francerecipe100.csv')
# df.pop('Label')

win = False

print("[INFO] Loading model...")
baking_model = load_model("0422bakingT_t")
recipe_model = load_model("bakingrecipefrench0420")
def show_bread(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')

    img = Image.open('bread.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_cake(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')

    img = Image.open('cake.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_cookie(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')

    img = Image.open('cookie.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_croissant(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')
    img = Image.open('croissant.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_breaie(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')
    img = Image.open('breaie.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_cakie(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')
    img = Image.open('cakie.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def show_cruskie(T, t):
    newWindow = tk.Toplevel()
    newWindow.title('Baking_Answer')
    width = 350
    height = 480
    left = 0
    top = 0
    newWindow.geometry(f'{width}x{height}+{left}+{top}')
    img = Image.open('cruskie.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件
    label = tk.Label(newWindow, image=tk_img, width=350, height=350, compound="top")  # 在 Lable 中放入圖
    label.pack()
    label2 = tk.Label(newWindow, font = ('Arial',17), text="Suggested Directions")
    label2.place(x = 30, y=350)
    Tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Oven Temperature：' + str(T) + chr(176) +'C'))
    Tlabel.place(x = 30, y=390)
    tlabel = tk.Label(newWindow, font = ('Arial',16), text=('Cooking Time：' + (str(t) + 'Minute')))
    tlabel.place(x = 30, y=430)
    newWindow.mainloop()

def normalize(test_data):
    data_max = np.array([3, 745, 310, 6, 45, 310, 3, 2.5, 120, 180, 3, 400, 80, 575, 400, 4])
    data_min = np.array([0, 10, 0, 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(data_max)
    print(data_min)
    print(test_data)
    return (test_data - data_min) /(data_max - data_min)

def recover(normal, index):
    data_max = np.array([3, 745, 310, 6, 45, 310, 3, 2.5, 120, 180, 3, 400, 80, 575, 400, 4, 260, 60])
    data_min = np.array([0, 10, 0, 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 135, 8])
    # print(data_max[index])
    # print(data_min[index])        
    return (data_max[index] - data_min[index]) * normal + data_min[index]

# def back():
#     global root
#     root.destroy()
#     main()

def main():
    global Yeast, Flour, Sugar, Egg, Oil, Milk, Soda, Powder, Almond, Chocolate, Banana, Flaky, Honey, Water, Butter, Salt, Bread, Cake, Cookie, Croissant
    global root
    global win

    if win:
        root.destroy()
        win = False

    root=tk.Tk()
    root.configure(background='#f5f5dc')
    root.title('AI baker')

    #root.iconbitmap = ('favicon.ico') 
    width = 650
    height = 480
    left = 0
    top = 0
    root.geometry(f'{width}x{height}+{left}+{top}')

    # Title
    tklabel = tk.Label(root, text='AI Baker',
        font = ('Arial', 20, 'bold'), fg = '#574740', bg='#f5f5dc')
    tklabel.place(relx=0.45, rely=0)

    # Yeast
    Yeastlabel = tk.Label(root, text='Yeast(g)',
        font = ('Arial', 16), bg='#f5f5dc', fg='#D18981')
    Yeastlabel.place(x = column0, y=row0)

    Yeast = tk.StringVar()
    tkyeast = tk.Entry(root, textvariable=Yeast)
    tkyeast.place(x = column1, y=row1, width = 145 , height = 20)
    print(tkyeast.place())

    #Flour
    Flourlabel = tk.Label(root, text='Flour(g)',
        font = ('Arial', 16), bg='#f5f5dc', fg='#D18981')
    Flourlabel.place(x = column0, y=row2)

    Flour = tk.StringVar()
    tkflour = tk.Entry(root, textvariable=Flour)
    tkflour.place(x = column1, y=row3, width = 145 , height = 20)

    #Sugar
    Sugarlabel = tk.Label(root, text='Sugar(g)',
        font = ('Arial',16), bg='#f5f5dc', fg='#D18981')
    Sugarlabel.place(x = column0, y=row4)

    Sugar = tk.StringVar()
    tkSugar = tk.Entry(root, textvariable=Sugar)
    tkSugar.place(x = column1, y=row5, width = 145 , height = 20)

    #Egg
    Egglabel = tk.Label(root, text='Egg',
        font = ('Arial',16), bg='#f5f5dc', fg='#D18981')
    Egglabel.place(x = column2, y=row6)

    Egg = tk.StringVar()
    tkegg = tk.Entry(root, textvariable=Egg)
    tkegg.place(x = column1, y=row7, width = 145 , height = 20)

    #Oil
    Oillabel = tk.Label(root, text='Oil(g)',
        font = ('Arial',16), bg='#f5f5dc', fg='#D18981')
    Oillabel.place(x = column3, y=row0)

    Oil = tk.StringVar()
    tkoil = tk.Entry(root, textvariable=Oil)
    tkoil.place(x = column4, y=row1, width = 145 , height = 21)

    #Milk
    Milklabel = tk.Label(root, text='Milk(g)',
        font = ('Arial',16), bg='#f5f5dc', fg='#D18981')
    Milklabel.place(x = column3, y=row2)

    Milk = tk.StringVar()
    tkmilk = tk.Entry(root, textvariable=Milk)
    tkmilk.place(x = column4, y=row3, width = 145 , height = 21)

    #Soda
    Sodalabel = tk.Label(root, text='Bake Soda(tsp)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Sodalabel.place(x = column3_1, y=row4)

    Soda = tk.StringVar()
    tksoda = tk.Entry(root, textvariable=Soda)
    tksoda.place(x = column4, y=row5, width = 145 , height = 21)

    #Bake Powder
    Powderlabel = tk.Label(root, text='Bake Powder(tsp)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Powderlabel.place(x = column3_1, y=row6)

    Powder = tk.StringVar()
    tkpowder = tk.Entry(root, textvariable=Powder)
    tkpowder.place(x = column4, y=row7, width = 145 , height = 21)

    #Almond Powder
    Almondlabel = tk.Label(root, text='Almond Powder(g)',
        font = ('Arial',13), bg='#f5f5dc', fg='#D18981')
    Almondlabel.place(x = column5 - 43, y=row0 + 6)

    Almond = tk.StringVar()
    tkalmond = tk.Entry(root, textvariable=Almond)
    tkalmond.place(x = column6, y=row1, width = 145 , height = 21)

    #Chocolate Powder
    Chocolatelabel = tk.Label(root, text='Chocolate Powder(g)',
        font = ('Arial',12), bg='#f5f5dc', fg='#D18981')
    Chocolatelabel.place(x = column5 - 50, y=row2 + 6)

    Chocolate = tk.StringVar()
    tkchocolate = tk.Entry(root, textvariable=Chocolate)
    tkchocolate.place(x = column6, y=row3, width = 145 , height = 21)

    #Banana
    Bananalabel = tk.Label(root, text='Banana',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Bananalabel.place(x = column5 - 15, y=row4)

    Banana = tk.StringVar()
    tkbanana = tk.Entry(root, textvariable=Banana)
    tkbanana.place(x = column6, y=row5, width = 145 , height = 21)

    #Flaky Butter
    Flakylabel = tk.Label(root, text='Flaky Butter(g)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Flakylabel.place(x = column5-35, y=row6)

    Flaky = tk.StringVar()
    tkflaky = tk.Entry(root, textvariable=Flaky)
    tkflaky.place(x = column6, y=row7, width = 145 , height = 21)

    #Honey
    Honeylabel = tk.Label(root, text='Honey(g)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Honeylabel.place(x = column7 - 25, y=row0)

    Honey = tk.StringVar()
    tkhoney = tk.Entry(root, textvariable=Honey)
    tkhoney.place(x = column8, y=row1, width = 145 , height = 21)

    #Water
    Waterlabel = tk.Label(root, text='Water(g)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Waterlabel.place(x = column7 - 25, y=row2)

    Water = tk.StringVar()
    tkwater = tk.Entry(root, textvariable=Water)
    tkwater.place(x = column8, y=row3, width = 145 , height = 21)

    #Butter
    Butterlabel = tk.Label(root, text='Butter(g)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Butterlabel.place(x = column7 - 25, y=row4)

    Butter = tk.StringVar()
    tkbutter = tk.Entry(root, textvariable=Butter)
    tkbutter.place(x = column8, y=row5, width = 145 , height = 21)

    #Salt
    Saltlabel = tk.Label(root, text='Salt(tsp)',
        font = ('Arial',14), bg='#f5f5dc', fg='#D18981')
    Saltlabel.place(x = column7 - 25, y=row6)

    Salt = tk.StringVar()
    tksalt = tk.Entry(root, textvariable=Salt)
    tksalt.place(x = column8, y=row7, width = 145 , height = 21)

    btn = tk.Button(root, text='Baking ?', command=predict, font = ('Arial', 20), bg ='#574740', fg='#f5f5dc')
    btn.place(relx=0.40, rely=0.65)

    button = tk.Button(root, text='Output_recipes',command=new_window, font = ('Arial', 11), bg ='#D18981', fg='#f5f5dc')
    button.place(x = column0-40, y=row8-70)
    # root.pack()
    # root.mainloop()

    tkBreadlabel = tk.Label(root, text='Bread：', font = ('Arial', 18), bg='#f5f5dc')
    tkBreadlabel.place(x = column0-40, y=row8)

    Bread = tk.StringVar()
    Breadlabel = tk.Label(root, textvariable = Bread, font = ('Arial', 18), bg='#f5f5dc')
    Breadlabel.place(x = column1+80, y=row8+2)

    tkCakelabel = tk.Label(root, text='Cake：', font = ('Arial', 18), bg='#f5f5dc')
    tkCakelabel.place(x = column3-37, y=row8)

    Cake = tk.StringVar()
    Cakelabel = tk.Label(root, textvariable = Cake, font = ('Arial', 18), bg='#f5f5dc')
    Cakelabel.place(x = column4+77, y=row8+2)

    tkCookielabel = tk.Label(root, text='Cookie：', font = ('Arial', 18), bg='#f5f5dc')
    tkCookielabel.place(x = column5-38, y=row8)

    Cookie = tk.StringVar()
    Cookielabel = tk.Label(root, textvariable = Cookie, font = ('Arial', 16), bg='#f5f5dc')
    Cookielabel.place(x = column6+105, y=row8+2)

    tkCroissantlabel = tk.Label(root, text='Croissant：', font = ('Arial', 18), bg='#f5f5dc')
    tkCroissantlabel.place(x = column7-30, y=row8)

    Croissant = tk.StringVar()
    Croissantlabel = tk.Label(root, textvariable = Croissant, font = ('Arial', 16), bg='#f5f5dc')
    Croissantlabel.place(x = column8+145, y=row8+2)
    root.mainloop()

# making recipes
def make():
    #權愈變數
    global B, Ca, Co, Cr
    global root
    #Preparint the class
    recipestr = ''
    b = float(B.get()) /100 if B.get() !='' else 0
    print('Bread(%):',b)
    ca = float(Ca.get()) /100 if Ca.get() !='' else 0 
    print('Cake(%):',ca)
    co = float(Co.get()) /100 if Co.get() !='' else 0
    print('Cookie(%):',co)
    cr = float(Cr.get()) /100 if Cr.get() !='' else 0
    print('Croissant(%):',Cr)

    dessert = [[b, ca, co, cr]]
    print('testX', dessert)

    recipe = recipe_model.predict(dessert)[0]
    print(recipe)
    for i in range(len(recipe)):
        recipe[i] = np.round(recover(recipe[i], i),1) if i != 3 else np.round(recover(recipe[i], i))
        print(recipe[i])
        if i == 0 and recipe[i] != 0:
            recipestr = 'Yeast :' + str(recipe[i]) +'g  '
            # print(recipestr)
        elif i == 1 and recipe[i] != 0:
            recipestr = recipestr + 'Flour : ' + str(recipe[i]) +'g  '
        elif i == 2 and recipe[i] != 0:
            recipestr = recipestr + 'Sugar : ' + str(recipe[i]) +'g  '
        elif i == 3 and recipe[i] != 0:
            recipestr = recipestr + 'Egg : ' + str(recipe[i]) +'g  \n'
        elif i == 4 and recipe[i] != 0:
            recipestr = recipestr + 'Oil : ' + str(recipe[i]) +'g  '
        elif i == 5 and recipe[i] != 0:
            recipestr = recipestr + 'Mike : ' + str(recipe[i]) +'g  '
        elif i == 6 and recipe[i] != 0:
            recipestr = recipestr + 'Baking Soda : ' + str(recipe[i]) +'(tsp)  \n'
        elif i == 7 and recipe[i] != 0:
            recipestr = recipestr + 'Baking Powder : ' + str(recipe[i]) +'(tsp)  '
        elif i == 8 and recipe[i] != 0:
            recipestr = recipestr + 'Almond P : ' + str(recipe[i]) +'g \n '
        elif i == 9 and recipe[i] != 0:
            recipestr = recipestr + 'Chocolate P : ' + str(recipe[i]) +'g  '
        elif i == 10 and recipe[i] != 0:
            recipestr = recipestr + 'Banan : ' + str(recipe[i]) +'g  '
        elif i == 11 and recipe[i] != 0:
            recipestr = recipestr + 'Flaky Butter : ' + str(recipe[i]) +'g \n '
        elif i == 12 and recipe[i] != 0:
            recipestr = recipestr + 'Honey : ' + str(recipe[i]) +'g  '
        elif i == 13 and recipe[i] != 0:
            recipestr = recipestr + 'Water : ' + str(recipe[i]) +'g  '
        elif i == 14 and recipe[i] != 0:
            recipestr = recipestr + 'Butter : ' + str(recipe[i]) +'g  '
        elif i == 15 and recipe[i] != 0:
            recipestr = recipestr + 'Salt : ' + str(recipe[i]) +'g  '
            # print(recipestr)
    Dlabel = tk.Label(root, font = ('Arial',14), text= recipestr, justify='left', bg ='#FCF8E8', fg='#574740')
    Dlabel.place(x = column1, y=350)
    
def new_window():
    global root
    global recipestr
    global B, Ca, Co, Cr
    global win
    win = True
    root.destroy()
    root=tk.Tk()
    root.title("Make_Recipes")
    root.configure(background='#FCF8E8')
    width = 650
    height = 480
    left = 0
    top = 0
    root.geometry(f'{width}x{height}+{left}+{top}')

    tklabel = tk.Label(root, text='Make Recipes',
    font = ('Arial', 20, 'bold'), fg = '#574740', bg='#FCF8E8')
    tklabel.place(relx=0.35, rely=0)

    Blabel = tk.Label(root, text='Bread(%)',
    font = ('Arial', 16), bg='#FCF8E8', fg='#D18981')
    Blabel.place(x = column0, y=row2)
    B = tk.StringVar()
    tkB = tk.Entry(root, textvariable=B)
    tkB.place(x = column1, y=row3, width = 145 , height = 20)

    Calabel = tk.Label(root, text='Cake(%)',
    font = ('Arial', 16), bg='#FCF8E8', fg='#D18981')
    Calabel.place(x = column3-10, y=row2)
    Ca = tk.StringVar()
    tkCa = tk.Entry(root, textvariable=Ca)
    tkCa.place(x = column4, y=row3, width = 145 , height = 21)

    Co = tk.Label(root, text='Cookie(%)',
    font = ('Arial', 16), bg='#FCF8E8', fg='#D18981')
    Co.place(x = column5-27, y=row2)
    Co = tk.StringVar()
    tkCo = tk.Entry(root, textvariable=Co)
    tkCo.place(x = column6, y=row3, width = 145 , height = 21)

    Cr = tk.Label(root, text='Croisssant(%)',
    font = ('Arial', 16), bg='#FCF8E8', fg='#D18981')
    Cr.place(x = column7-45, y=row2)
    Cr = tk.StringVar()
    tkCr = tk.Entry(root, textvariable=Cr)
    tkCr.place(x = column8, y=row3, width = 145 , height = 21)

    Rlabel = tk.Label(root, font = ('Arial',18), text='Ingredients：', bg ='#FCF8E8', fg='#574740')
    Rlabel.place(x = column1, y=300)

    Rlabel = tk.Label(root, font = ('Arial',16), text='*All elements must sum up to 100%', bg ='#FCF8E8', fg='#FF0000')
    Rlabel.place(x = column1, y=190)    

    btn = tk.Button(root, text='Making!', command=make, font = ('Arial', 20), bg ='#574740', fg='#f5f5dc')
    btn.place(relx=0.40, rely=0.50)

    button = tk.Button(root, text='Return',command=main, font = ('Arial', 11), bg ='#D18981', fg='#f5f5dc')
    button.place(x = column0-35, y=row8-160)

    root.mainloop()

def predict():
    global yeast, flour, sugar, egg, oil, milk, soda, powder, almond, chocolate, banana, flaky, honey, water, butter, salt

    yeast = float(Yeast.get()) if Yeast.get() !='' else 0
    print('Yeast(g):',yeast)

    flour = float(Flour.get()) if Flour.get() !='' else 0
    print('Flour(g):',flour)

    sugar = float(Sugar.get()) if Sugar.get() !='' else 0
    print('Sugar(g):',sugar)

    egg = float(Egg.get()) if Egg.get() !='' else 0
    print('Egg(g):',egg)

    oil = float(Oil.get()) if Oil.get() !='' else 0
    print('Oil(g):',oil)

    milk = float(Milk.get()) if Milk.get() !='' else 0
    print('Milk(g):',milk)

    soda = float(Soda.get()) if Soda.get() !='' else 0
    print('Soda(g):',soda)

    powder = float(Powder.get()) if Powder.get() !='' else 0
    print('Powder(g):',powder)

    almond = float(Almond.get()) if Almond.get() !='' else 0
    print('Almond(g):',almond)

    chocolate = float(Chocolate.get()) if Chocolate.get() !='' else 0
    print('Chocolate(g):',chocolate)

    banana = float(Banana.get()) if Banana.get() !='' else 0
    print('Banana(g):',banana)

    flaky = float(Flaky.get()) if Flaky.get() !='' else 0
    print('Flaky Butter(g):',flaky)

    honey = float(Honey.get()) if Honey.get() !='' else 0
    print('Honey(g):',honey)

    water = float(Water.get()) if Water.get() !='' else 0
    print('Water(g):',water)

    butter = float(Butter.get()) if Butter.get() !='' else 0
    print('Butter(g):',butter)

    salt = float(Salt.get()) if Salt.get() !='' else 0
    print('Salt(g):',salt)

    testX = [[yeast, flour, sugar, egg, oil, milk, soda, powder, almond, chocolate, banana, flaky, honey, water, butter, salt]]
    print('testX', testX)

    testX = np.array(testX)

    #Every item mustnot be 0

    if testX.sum() != 0 and testX[0][1] != 0:

        testX = normalize(testX)
        
        testX = np.nan_to_num(testX)
        print(testX)
        predictions, tem, time = baking_model.predict(testX)
        print(tem[0])
        T = recover(tem[0], -2)
        t = recover(time[0], -1)
        print(T)
        print(t)
        np.set_printoptions(precision=3, suppress=True)

        print(labelname)
        print("******************")
        print(predictions)
        print(tem)
        print(time)

        confidence = np.round(predictions[0]  * 100)
        T = int(np.round(T))
        t = int(np.round(t))

        print(confidence)
        Bread.set(str(confidence[0]) + '%')
        Cake.set(str(confidence[1]) + '%')
        Cookie.set(str(confidence[2]) + '%')
        Croissant.set(str(confidence[3]) + '%')

        if np.max(confidence) == 50:
            first = np.argmax(confidence)
            second = np.argmax(confidence[np.argmax(confidence)+1:])+ np.argmax(confidence)+1
            # print(np.max())
            if first == 0 and second == 2:
                show_breaie(T, t)
            elif first == 1 and second == 2:
                show_cakie(T, t)
            elif first == 2 and second == 3:
                show_cruskie(T, t)

        elif np.argmax(confidence) == 0:
            show_bread(T, t)
        elif np.argmax(confidence) == 1:
            show_cake(T, t)
        elif np.argmax(confidence) == 2:
            show_cookie(T, t)
        elif np.argmax(confidence) == 3:
            show_croissant(T, t)

    else: # Clear all
        Bread.set('')
        Cake.set('')
        Cookie.set('')
        Croissant.set('')

if __name__ == '__main__':    
    #root = tk.Tk()
    main()
    #root.mainloop()

    