#!/usr/bin/env python
#_*_coding: utf8 _*_

#Script edit by Jorge Donaires Mendoza

from color import Color as Cl

class classicSquare:
    
    columns=[]
    color=Cl.red()
    reset_color=Cl.endColor()
    @classmethod
    def savingList(cls,*args):
        cls.list_list=list(args)

        return cls.list_list

    @classmethod
    def numberColumns(cls,list_list):
        
        for lst in cls.list_list[0]:
            cls.columns.append(len(lst))

        iterator=0
        for i in range(len(cls.list_list)-1):
            
            for item_lst in cls.list_list[i+1]:

                if cls.columns[iterator]<len(item_lst):
                    cls.columns[iterator]=len(item_lst)

            iterator+=1

        for itr in range(len(cls.columns)):

            if cls.columns[itr]%2==0:
                cls.columns[itr]=(cls.columns[itr]//2)+1

            else:
                cls.columns[itr]+=1
                cls.columns[itr]=(cls.columns[itr]//2)+1

        return cls.columns
    
    @classmethod
    def totalColumn(cls,columns):

        sum_column=0

        for item_column in cls.columns:
            sum_column+=item_column

        return sum_column

    @classmethod
    def drawSquare(cls,list_list):

        list_columns=cls.numberColumns(cls.list_list)
        total_column=cls.totalColumn(list_columns)

        print(cls.color,end='')
        print('+'+'--'*total_column+'+')
        print(cls.reset_color,end='')
        # i es el numero de filas que tendra la parte superior del cuadro
        #como solo sera una fila entonces podemos poner que solo recorra una vez
        for i in range(1):

            for j in range(2*total_column+2):
                if j==0:
                    print(cls.color,end='')
                    print('|',end='')
                    print(cls.reset_color,end='')
                elif j>0 and j<(2*total_column+1):
                    inf=0
                    indx=0
                    sup=2*list_columns[indx]
                    for k in range(len(list_columns)):
                        if j>inf and j<=sup:
                            if j<=inf + len(list_list[i][k]):
                                print(cls.list_list[i][k][j-1-inf],end='')
                            elif j==sup and k!=len(list_columns)-1:
                                print(cls.color,end='')
                                print('|',end='')
                                print(cls.reset_color,end='')
                            else:
                                print(' ',end='')
                        inf=sup
                        indx+=1
                        if indx<len(list_columns):
                            sup+=list_columns[indx]*2
                else:
                    print(cls.color,end='')
                    print('|',end='')
                    print(cls.reset_color,end='')
            print('\n',end='')
        print(cls.color,end='')
        print('-'+'--'*total_column+'-')
        print(cls.reset_color,end='')

        maximum=0
        for i in range(len(cls.list_list)):
            if i>0:
                if len(cls.list_list[i])>maximum:
                    maximum=len(cls.list_list[i])

        list_supreme=[]
        for i in range((maximum)):
                empty_list=[]
                for j in range(len(cls.list_list)-1):
                    empty_list.append(cls.list_list[j+1][i])
                list_supreme.append(empty_list)
        
        for i in range(len(list_supreme)):
            for j in range(2*total_column+2):
                if j==0:
                    print(cls.color,end='')
                    print('|',end='')
                    print(cls.reset_color,end='')
                elif j > 0 and j < (2*total_column+1):
                    inf=0
                    indx=0
                    sup=2*list_columns[indx]
                    for k in range(len(list_columns)):
                        if j > inf and j <= sup :
                            if j <= inf + len(list_supreme[i][k]):
                                print(list_supreme[i][k][j-1-inf],end='')
                            elif j==sup and k!=len(list_columns)-1:
                                print(cls.color,end='')
                                print('|',end='')
                                print(cls.reset_color,end='')
                            else:
                                print(' ',end='')
                        inf=sup
                        indx+=1
                        if indx<len(list_columns):
                            sup+=list_columns[indx]*2
                else:
                    print(cls.color,end='')
                    print('|',end='')
                    print(cls.reset_color,end='')
            print ('\n',end='')
        print(cls.color,end='')
        print('+'+'--'*total_column+'+')
        print(cls.reset_color,end='')
        

if __name__=='__main__':

    pass
