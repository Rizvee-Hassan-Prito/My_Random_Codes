# -*- coding: utf-8 -*-

#%%
print("\n\n\n                Welcome to Conjoin Bubble Simulation                \n\n\n")
print("               !!!Every beep is a sound of conjoin!!!             \n\n\n")
#%%
import numpy as np
import winsound

main_field=[['#','#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#','#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

#%%
"""print(("").join(a[0]))"""
import random
import time


bubbles=[]
position_direc=['up-right','up-left','down-right','down-left']
check_same_pos_value=[]

n=int(input("\nEnter number of bubbles (Not more than 132): "))
for i in range(n):
    c=0
    while(c!=1):
        status={}
        v0=random.randint(1,6)
        v00=random.randint(1,22)
        if [v0,v00] not in check_same_pos_value:
            check_same_pos_value.append([v0,v00])
            main_field[v0][v00]='O'
            status['position_v']=[v0,v00]
            status['position_direc']=position_direc[random.randint(0,3)]
            bubbles.append(status)
            c+=1


print('\n')
for i in main_field:
      print(("").join(i))
print('\n')
print("Total bubbles:", len(check_same_pos_value))
print('\n')


"""
status={}
v0=6
v00=16
main_field[v0][v00]='O'
status['position_v']=[v0,v00]
status['position_direc']='up-left'
bubbles.append(status)
    
for i in main_field:
    print(("").join(i))

print(bubbles)
"""
#%%

#print(bubbles[0]['position_v'][0])


def movement(status):
    
    if status['position_direc']=='down-left':
        
        x2=[(status['position_v'][0]), (status['position_v'][1])-1]
        
        if (main_field[x2[0]][x2[1]]=='#' and main_field[x2[0]+1][x2[1]+2]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]-1][x2[1]+2]='O'
            status['position_direc']='up-right'
            status['position_v']=[x2[0]-1,x2[1]+2]
            
            
        elif (main_field[x2[0]][x2[1]]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]][x2[1]+2]='O'
            status['position_direc']='down-right'
            status['position_v']=[x2[0],x2[1]+2]
            
        elif (main_field[x2[0]+1][x2[1]+1]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]][x2[1]+1]='O'
            status['position_direc']='up-left'
            status['position_v']=[x2[0],x2[1]+1]
        
        elif (main_field[x2[0]+1][x2[1]]=='O'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            bubbles.remove(status)
            frequency = 1000  # Set Frequency To 2500 Hertz
            duration = 800 # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        
        else:
            
            main_field[x2[0]+1][x2[1]]='O'
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            status['position_v']=[x2[0]+1,x2[1]]
    
##############################
   
    if status['position_direc']=='down-right':
        x2=[(status['position_v'][0]), (status['position_v'][1])+1]
        
        if (main_field[x2[0]][x2[1]]=='#' and main_field[x2[0]+1][x2[1]-2]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]-1][x2[1]-2]='O'
            status['position_direc']='up-left'
            status['position_v']=[x2[0]-1,x2[1]-2]
            
            
        elif (main_field[x2[0]][x2[1]]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]+1][x2[1]-2]='O'
            status['position_direc']='down-left'
            status['position_v']=[x2[0]+1,x2[1]-2]
        
        
        elif (main_field[x2[0]+1][x2[1]-1]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]][x2[1]-1]='O'
            status['position_direc']='up-right'
            status['position_v']=[x2[0],x2[1]-1]
                
            
        elif (main_field[x2[0]+1][x2[1]]=='O'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            bubbles.remove(status)
            frequency = 1500  # Set Frequency To 2500 Hertz
            duration = 800 # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        
        else:
            
            main_field[x2[0]+1][x2[1]]='O'
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            status['position_v']=[x2[0]+1,x2[1]]

##############################
    if status['position_direc']=='up-right':
        
        x2=[(status['position_v'][0]), (status['position_v'][1])+1]
        
        if (main_field[x2[0]][x2[1]]=='#' and main_field[x2[0]-1][x2[1]-2]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]+1][x2[1]-2]='O'
            status['position_direc']='down-left'
            status['position_v']=[x2[0]+1,x2[1]-2]
            
            
        elif (main_field[x2[0]][x2[1]]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]][x2[1]-2]='O'
            status['position_direc']='up-left'
            status['position_v']=[x2[0],x2[1]-2]
        
        
        elif (main_field[x2[0]-1][x2[1]-1]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]+1][x2[1]]='O'
            status['position_direc']='down-right'
            status['position_v']=[x2[0]+1,x2[1]]
                
            
        elif (main_field[x2[0]-1][x2[1]]=='O'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            bubbles.remove(status)
            frequency = 2000  # Set Frequency To 2500 Hertz
            duration = 800 # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        
        else:
            
            main_field[x2[0]-1][x2[1]]='O'
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            status['position_v']=[x2[0]-1,x2[1]]

##############################
    if status['position_direc']=='up-left':
        
        x2=[(status['position_v'][0]), (status['position_v'][1])-1]
        
        if (main_field[x2[0]][x2[1]]=='#' and main_field[x2[0]-1][x2[1]+2]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]+1][x2[1]+2]='O'
            status['position_direc']='down-right'
            status['position_v']=[x2[0]+1,x2[1]+2]
            
            
        elif (main_field[x2[0]][x2[1]]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]-1][x2[1]+2]='O'
            status['position_direc']='up-right'
            status['position_v']=[x2[0]-1,x2[1]+2]
        
        
        elif (main_field[x2[0]-1][x2[1]+1]=='#'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            main_field[x2[0]+1][x2[1]]='O'
            status['position_direc']='down-left'
            status['position_v']=[x2[0]+1,x2[1]]
                
            
        elif (main_field[x2[0]-1][x2[1]]=='O'):
            
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            bubbles.remove(status)
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 800 # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        
        else:
            
            main_field[x2[0]-1][x2[1]]='O'
            main_field[status['position_v'][0]][status['position_v'][1]]=' '
            status['position_v']=[x2[0]-1,x2[1]]




while(1):
    e=int(input ('Enter 1 to see the movement of 1 bubble at a time\nEnter 2 to see the movement of all the bubbles at a time\n\n----->'))
    print('\n')
    if e == 1:
        while(1):
            for i in bubbles:
                movement(i)
                
                for i in main_field:
                    print(("").join(i))
                print('\n')
                print("Total bubbles:", len(bubbles))
                print('\n')
                time.sleep(1)
    elif e == 2:
        while(1):
            for i in bubbles:
                movement(i)
                
            for i in main_field:
                print(("").join(i))
            print('\n')
            print("Total bubbles:", len(bubbles))
            print('\n')
            time.sleep(1)
    else:
        print("\nInvalid Input. Try again.\n")

""" 
movement(bubbles[0])
for i in main_field:
      print(("").join(i))
print(bubbles)
print('\n')
"""

