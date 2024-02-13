"""
===============================================================================
ENGR 13300 Fall 2022

Program Description
    A program that is simultant of the 'Akinator' game

Assignment Information
    Assignment:     Indivivual Project
    Author:         Soham Agarwal, agarw317@purdue.edu
    Team ID:        
Contributor:
                
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

#Importing the different libraries being used
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Importing necessary UDFs for the program to work
import udf1 as ud
import udf2 as ud2
#import openpyxl


#Welcoming the user
plt.title("WELCOME!")
image = mpimg.imread("akinatorpurdue.png")
plt.axis('off')
plt.imshow(image)

plt.show()

#The menu where the user is also welcomed, and where they are prompted to run the code 
print("Hello, and Welcome to Purdue Akinator!")
print("Created by Soham Agarwal")
print("This is exclusively for Indian cinema universe so kindly ensure your character is along those lines!")
print("To start press 1 at the prompt")

#input check for the prompt
start = eval(input("prompt:"))
while start != 1:
    start = eval(input("prompt:"))

#assinging all important pre-reqs to global scope variables for the program to function
final = pd.read_excel('actordata.xlsx')
datax = pd.read_excel('actordata.xlsx')
data = datax.to_numpy()
#the list of all the questions
questions = ['Is your character male? ', 'is your character real? ', 'Is your character of or more than 50 years of age? ', 'Is your chatracter a Muslim? ', 'Is your character a villain? ', 'Does your character have kids? ', 'Has your character ever played in a superhero movie/a superhero? ', 'Is your character married? ', 'Is your character dead? ', 'Is your character over 30 years old? ', 'Has your character played in a medieval movie/or from a medieval movie?', 'is the complextion of your character fair?', 'does you character have family lefacy in the film industry', 'is your character from the housefull or golmaal franchise?', 'is your character a star from the 2000s or the 1990s', 'has your character even been to hollywood?', 'is your character usually associated with romance?', 'is your character usually assosciated with action?', 'is your character usually assosciated with comedy?']
lenq = int(len(questions))
leny = len(data[:,0])
lenx = len(data[0,:])

#Handling the data to accurately suit the flow of the program. For example, numeric conversions of the entire database
data1 = data
for q in range(leny):
    data1[q,0] = q
    for r in range(lenx):
        if data1[q,r] == 'y':
            data1[q,r] = 1
        elif data1[q,r] == 'n':
            data1[q,r] = 0
#some variable delclarations for the code to operate
y = 'y'
n = 'n'
i = 0
j = 0

#user defined function for writing out an important matrix that is crucial to the program. This is the output matrix after every outer iteration 
def writearray (x,y,z):
    for k in range(len(x)):
        y[k,:] = z[x[k],:]
    return y

#important UDF for the conversion of values to numeric values
def conversion (value):
    if value == 'n':
        value = 0
    else:
        value = 1
    return value

#main function
def main():
#handling and assinging data for variables. This included the entire data, lenght of data, initlization etc. This is especially important for indexing
    result = data1
    lend = len(result[:,0])
    add_list = []
#nested loop structure for the main body of the program. This part of the program determines the values in the database that align with the user's input of the database
    for i in range (lenq):
        value = ud.takeinput(i)
        value = conversion(value)
        for j in range (lend):
            if (result[j, i+1] == value):
                add_list.append(j)
#Important data handling for the outer iteration for the function to work. This part sets up the output of the program
        len1 = len(add_list)
        output = np.zeros([len1, lenx])
        output = writearray(add_list,output,result)
        result = output
        lend = len(result[:,0])
        add_list = []
        if lend == 1:
            break
#This part of the program finally outputs the desired output, that is the name of the character.
    helper = int(result[0,0])
    final_output = ud2.check(helper)
    with open ('Output1.txt', 'w') as file:
        file.write("And your character is:\n")
        file.write(final_output)
        file.write("\nI hope we got the correct guess. If not, please try re-running the code with the right answers, or another possibilty is that that the character you are thinking of is not included in our database.\n\n If you wish to add another data into our database, please go back to the page of the code")
        
       # rewrite = openpyxl.load_workbook('actordata.xlsx')
        #sheet = rewrite.get_sheet_by_name('Sheet1')
        
        #sheet['A1'] = 'hello world'
        #xfile.save('text2.xlsx')

#necessary statement for the code to function
if __name__ == '__main__':
    main()
