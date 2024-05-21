# Tkinter version of AI Michelin Dessert Master System

This is the Tkinter version

Web App version in here："https://github.com/Nana1018/AIbaking"

### About:
This study utilizes neural network technology to establish a model for French dessert recipes. The system can identify dessert types from recipes. It empowers AI with innovative capabilities to create desserts with entirely new flavors, such as "Cakie" (50% cake, 50% cookie) and "Breakie" (50% bread, 50% cookie). Additionally, it provides baking guidelines for users, recommending appropriate oven temperatures and baking times. It can also generate dessert recipes based on taste preferences.

## How it Works

Downloading the total file,
first implement tktestbaking_returnv1.py file, which is the main program.
##### Models.
      0422bakingT_t = the model used by AI baking.
      bakingrecipefrench0420 = the model used by Generate Recipe.
##### files.
      francerecipet100.csv = data set
      bread.jpg , bread.jpg etc. = Pictures shown(You can change it to what you want)
## How to use

The system consists of two pages. The first page is the AI Baking interface, and the other page is the Make Recip page.

AI baking interface:
The recipe have 16 ingredients, enter the required ingredients and their weight (in grams) into the box grid. Press the "Baking" button,the dessert and baking method of this recipe will be obtained through the category neural model and the baking method neural model. You can also get the probability that the system recognizes that type of dessert.

Make Recip interface:
Pressing the "Output_recipes" button will navigate to the Generate Recipe page. In this screen, you'll enter the desired taste preferences. Pressing the "Making" button will utilize the generation neural model to generate an ingredient recipe that matches the taste requirements for this dessert.
      
## Citing

@article{AI Baking_Tkinter,

Author={Hsin-Le. {Lo},

title={Tkinter version of AI Michelin Dessert Master System - Research on the application of artificial intelligence in dessert making},

year={2024} }

Project Leader
Lo, Hsin-Le
