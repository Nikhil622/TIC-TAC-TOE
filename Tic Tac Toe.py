#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe Game

# In[1]:


# Tic Tac Toe Game BY Master Coder Nikhil

mylist={'1':(0,0),'2':(0,1),'3':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'7':(2,0),'8':(2,1),'9':(2,2)}
psm=[]

def goto():
    while True:
        x=input('To play press Y or to exit press N:')
        if x=='Y':
            return True
        elif x=='N':
            print('Are you sure to quit!')
            x=input('If Yes then press Y or else N:')
            if x=='Y':
                return False
            return True
        else:
            print('Not understand input. Press Y or N')
def choose_pos():
    while True:
        x=input('Input position in (1-9):')
        if x.isdigit():
            if int(x)>=0 and int(x)<10:
                if x not in psm:
                    psm.append(x)
                    return x
                else:
                    print('Place is already taken!')
        else:
            print('Invalid user input!\n Try Again!')
def display(x):
    print('\n'*40)
    for j in range(0,3):
        print(' '*50,end='')
        print('|',end=' ')
        for i in range(0,3):
            print(x[j][i]+' |',end=' ')
        print('\n')
def isWinner(x):
    d=[]
    d.append(''.join(x[0][::]))
    d.append(''.join(x[1][::]))
    d.append(''.join(x[2][::]))
    for i in range(0,3):
        p=''
        for j in range(0,3):
            p=p+x[j][i]
        d.append(p)
    m='x'*3
    n='o'*3
    d.append((x[0][0]+x[1][1]+x[2][2]))
    d.append((x[2][0]+x[1][1]+x[0][2]))
    if m in d:
        print('Player one is winner')
        return True
    if n in d:
        print('Second player is winner')
        return True
    return False

def restart():
    x='Y'
    y=input('To restart press Y or else N')
    while y!='Y' and y!='N':
        print('Invalid input. Please retry!')
        y=input('To restart press Y or else N')
    if y=='Y':
        psm.clear()
        fun()
                                                                                                        
def fun():
    p=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    display(p)
    i=0
    j=0
    while i<10 and goto():
        X=choose_pos()
        a,b=mylist[X]
        print('\n'*20)
        if j%2==0:
            p[a][b]='x'
            j=1
        else:
            p[a][b]='o'
            j=0  
        display(p)
        t=input('If you want to restart the game!\n Press Y else press any key!')
        if t=='Y':
            restart()
            break;
        i=i+1
        if isWinner(p):
              break


# In[ ]:


fun()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




