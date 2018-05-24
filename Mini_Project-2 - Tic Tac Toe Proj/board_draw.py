def draw(row = 3, col = 3):
    
    print('_'*3*row)
    for i in range(0,row):
        #print('\n')
        #for j in range(0,col):
        print('|  '*(col+1))
            #print('  ')
        #print('\n')
        print('_'*3*row)

c = draw(3,3)
#Used only when we want to print a arbitrary board
'''while True:
    try:
        print("Enter the number of rows you want on the board")
        r  = int(input())
        print("Enter the number of columns you want on the board")
        c  = int(input())
        if r is not c:
            print("Please make sure the number of rows and columns match")
    
        else:
            draw(r,c)

    except ValueError:
        print("Enter only integers please")'''