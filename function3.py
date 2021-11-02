import sqlite3
from _ast import For

import pandas as pd
import plotly.graph_objects as go
conn = sqlite3.connect('Ricin_Timeline')
c = conn.cursor()
#create lists for storing x and y coordinates of entities
x_coor=[]
y_coor=[]

#establish coordinates for moving entities
#query entity relationships and store all entities as a list
c.execute("Select Entity_ID FROM Entities")
Entities= c.fetchall()
print(Entities)
#establish list for storing query results of entities that move vertically on graph
Moving_Ent=[]
#use for loop to search relationship table for all Entities involved in trafficking relationships
#return entity1 that is moving, entity 2 that is moving to and start and end time
for i in range(0,len(Entities)):
    c.execute("Select Entity_ID_1, Entity_ID_2, Start_Time, End_Time "
          "FROM Relationships_1_2 WHERE Entity_ID_1 = ? AND Sub_Relationship = 'Traffic'", Entities[i])
    #store results in a temporary list
    temp_list = c.fetchall()
    #if temp list is not empty append results to nested list
    if temp_list:
        Moving_Ent.append(temp_list)
#create variable to store length of moving entities list
list_Length = len(Moving_Ent)
#for every item in moving entity list
for i in range(0,list_Length):
    list_length2 = len(Moving_Ent[i])
   #for every sublist in index i of moving list get item 2 and 3 and append to x_coor list
    for z in range(list_length2):
        x_coor.append(Moving_Ent[i][z][2])
        x_coor.append(Moving_Ent[i][z][3])

#create variable to control index during for loop to get y coordinates
index = 0
#for every item in moving entities list
for i in range(list_Length):
    list_length3 = len(Moving_Ent[i])
    #for every sublist in item i add the last index of y_coor list and item 4 of the moving entity sub list
    for z in range(list_length3):
        y_coor.insert(index + 1, y_coor[index])
        y_coor.append(Moving_Ent[i][z][4])
#add two to index variable
        index+=2

hello = [0,5,10,10,15,20]
#establish index variable equal to the last index of list x_coor
x=len(x_coor)-1
#for every item in x_coor list append the item x of x_coor to the end of x_coor
#subtract 1 from x at the end of each loop to get the next earliest item and append creating a mirror of the existing list after it
#this mirror list will create the x_coor for the bottom line part of the entity rectangle
for i in range(len(x_coor)):
    x_coor.append(x_coor[x])
    x=x-1
#append the first item of the list again to the end of x_coor list to complete the rectangle x coordinates
x_coor.append(x_coor[0])

#todo create algorithm for creating y coordinates for bottome line of rectangle

#dummy data to create pandas dataframe with
#insert various x and y coordinate lists into dictionary to create pandas dataframe, alternating between x and y coordiante of each entity
data={'X_1':[3,4,5,6,7,8,9], "Y_1":[7,9,11,13,15,17,19], 'X_2':[7,9,11,13,15,17,19],
      'Y_2':[7,9,11,13,15,17,19], 'X_3':[1,4,7,10,13,16,19], 'Y_3':[7,9,11,13,15,17,19]}
#create second dataframe with entity names. other attributes such as color can be put here as well
df_2=['Ricin','Golgi', 'Vesicle']
#create dataframe from dictionary variable storing x and y coordinates
df=pd.DataFrame(data)


#create blank plotly figure to add scatterplot traces to
fig = go.Figure()
#create range variable for for loop that is half the length of the number of columns in the dataframe
range_length = int(len(df.columns)/2)
#create variable to store indexes for columns during for loop
col = 0
#for every two columns in the dataframe add a scatter plot trace
#where the 1st column is used as the x coordinates, the second column is the y coordinates. add two to column index variable at the end of each loop to move to next two columns
for i in range(0,range_length):
    fig.add_trace(
        go.Scatter(
        x=df.iloc[:, col], y=df.iloc[:,col+1], name=df_2[i]
        ))
    col +=2
#show figure
fig.show()


conn.commit()
conn.close()