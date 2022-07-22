from classicSquare import classicSquare

if __name__ == '__main__':

    lista1=['nombre','apellido','direccion','telefono']
    lista2=['jorge','Daniel','Sofia','Dafne']
    lista3=['Donaires','asdfjlsdjf','alsdkjflasdkjf','askdfjalskdf']
    lista4=['av.aksdjfla','av askdfjasld','av. asldkfajs','av. asldkfjsd']
    lista5=['123456789','123789456','254684153','873945123']

    list_list=classicSquare.savingList(lista1,lista2,lista3,lista4,lista5)
    classicSquare.drawSquare(list_list)

