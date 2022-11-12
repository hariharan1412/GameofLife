import random
import os
import time

from colorama import Fore
from colorama import Style

class cell:

    def __init__(self , i , j , size , body='.' , Alive=False):
        
        self.row = i 
        self.col = j 

        self.size = size

        self.body = body

        # self.Neibours = None

        self.Alive = Alive
        
        self.id = self.col + self.row * 10

    def update(self , Neibour):

        neibour_count = 0

        if self.row > 0:
            if Neibour[self.row - 1][self.col].body == '*':
                neibour_count += 1

        if self.row < self.size -1:
            if Neibour[self.row + 1][self.col].body == '*':
                neibour_count += 1

        if self.col > 0:
            if Neibour[self.row][self.col- 1].body == '*':
                neibour_count += 1


        if self.col < self.size -1 :
            if Neibour[self.row][self.col + 1].body == '*':
                neibour_count += 1




        if self.row > 0 and self.col > 0:
            if Neibour[self.row - 1][self.col -1].body == '*':
                neibour_count += 1

        if self.row < self.size - 1 and self.col < self.size - 1:
            if Neibour[self.row + 1][self.col + 1].body == '*':
                neibour_count += 1

        if self.row < self.size - 1 and self.col > 0:
            if Neibour[self.row + 1][self.col - 1].body == '*':
                neibour_count += 1

        if self.row > 0 and self.col < self.size - 1:
            if Neibour[self.row - 1][self.col + 1].body == '*':
                neibour_count += 1


        if neibour_count < 2:

            self.Alive = False

        elif neibour_count > 3:

            self.Alive = False
        
        elif self.body == '*' and neibour_count == 2:

            self.Alive = True

        elif neibour_count == 3:

            self.Alive = True

        else:
            self.Alive = False
        
        
size = 100

def display(life):
    
    for i in range(size):
        for j in range(size):

            if life[i][j].Alive:
                print(f'{Style.BRIGHT}{Fore.WHITE}{life[i][j].body}', end=' ')
            else:
                print(f'{Style.BRIGHT}{life[i][j].body}', end=' ')

        print()

def update(life):

    for i in range(size):
        for j in range(size):
            
            life[i][j].update(life)


    for i in range(size):
        for j in range(size):
            
            if life[i][j].Alive:

                life[i][j].body = '*'

            else:
                life[i][j].body = '.'


def main():

    life = [['*' for i in range(size)] for j in range(size)]
    

    for i in range(size):
        for j in range(size):

            rand_pop = random.randint(1 , 2)

            if rand_pop == 1:
            
                life[i][j] = cell(i , j , size , body='*' , Alive=True)

            else:
                life[i][j] = cell(i , j , size)


    while True:

        display(life)
        update(life)

        time.sleep(0.1)
        os.system('clear')
        print()
        print()

main()