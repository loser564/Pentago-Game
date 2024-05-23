import numpy as np
import random 

def display_board(board):
    # Define the dimensions of the board
    rows = 6
    columns = 6

    for row in range(rows):
        for col in range(columns):
            print(board[row][col], end=' ')
            if (col + 1) % 3 == 0 and col < columns - 1:
                print('|', end=' ')
        print()  # Add a newline after each row
        if (row + 1) % 3 == 0 and row < rows - 1:
            print('-' * (columns * 2 - 1))  # Add horizontal separator after every 3 rows

def check_victory(board,turn,rot): #check before & after rotation
    
    x = 0 
    winner = 0
    while x < 2:
        # where x is a rotation counter 
        if x == 0 or x == 1: #checking for victory BEFORE and AFTER rotation
            if x == 1: #checking for victory AFTER rotation
                if rot % 2 == 0: #undoing the rotation 
                    rot = rot - 1 
                    board = rotation(board, rot)
                else: 
                    rot = rot + 1 
                    board = rotation(board, rot)
            win1=0
            win2=0
            
            # draw, everyone is a winner and everyone is a loser       
            i = 0
            j = 0
            while (i<6 and j<6):
                if (board[i][j] == 1 or board[i][j] == 2):
                    i += 1
                    j += 1
                else:
                    # got one empty space = no draw
                    break
            if (i == 6 and j == 6):
                return 3
        
            i = 0
            j = 0
        
            # horizontal winner
            while i < 6:
                if (board[i][1] == board[i][2] == board[i][3] == board[i][4]
                    and board[i][1] != 0):
                    if board[i][0] == board[i][1] or board[i][4] == board[i][5]:
                        if board[i][1] == 1:
                            win1 = 1
                            break
                        elif board[i][1] == 2:
                            win2 = 1
                            break
                    else:
                        i += 1
                else:
                    i += 1
            #updating the winner 
            if win1 == 1 and win2 == 0:
                return 1
            elif win2 == 1 and win1 == 0:
                return 2
            
        
            # vertical winner
            i = 0
            j = 0
            while j < 6:
                # for checking middle 4
                if (board[1][j] == board[2][j] == board[3][j] == board[4][j] 
                    and board[1][j] != 0):
                    
                    if (board[0][j] == board[1][j]) or (board[4][j] == board[5][j]):
                        if board[2][j] == 1:
                            win1 = 1
                            break
                        elif board[1][j] == 2:
                            win2 = 1
                            break
                else:
                    j += 1
            #updating the winner 
            if win1 == 1 and win2 == 0:
                return 1
            elif win2 == 1 and win1 == 0:
                return 2
            
            # diagonal winner
            i = 0
            j = 0
            #count accounts for the number of 0s. 1s and 2s in the board 
            count0 = 0 
            count1 = 0 
            count2 = 0 
        
            # forward short diagonal case 1; starting [0][1]
            for i in range(5):
                if board[i][i+1] == 1:
                    count1 += 1
                elif board[i][i+1] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
            
            # longest forward diagonal case 2 : starting [0][0]
            for i in range(6):
                if board[i][i] == 1:
                    count1 += 1
                elif board[i][i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
                
            # longest forward diagonal case 3 : starting [1][1]
            for i in range(1,6):
                if board[i][i] == 1:
                    count1 += 1
                elif board[i][i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
            
            # forward diagonal case 4 : starting [1][0]
            for i in range(1,6):
                if board[i][i-1] == 1:
                    count1 += 1
                elif board[i][i-1] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
                
            # backwards diagonal case 5 : starting [0][4]
            for i in range(5):
                if board[i][4-i] == 1:
                    count1 += 1
                elif board[i][4-i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
        
            # longest backward diagonal, case 6 : starting [0][5]
            for i in range(6):
                if board[i][5-i] == 1:
                    count1 += 1
                elif board[i][5-i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
             
            # longest backward diagonal, case 7 : starting [1][4]
            for i in range(1,6):
                if board[i][5-i] == 1:
                    count1 += 1
                elif board[i][5-i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
        
            # backwards diagonal case 8 : starting [1][5]
            for i in range(1,6):
                if board[i][6-i] == 1:
                    count1 += 1
                elif board[i][6-i] == 2:
                    count2 += 1 
                else:
                    count0 += 1
                #check for win
                if count1 == 5:
                    win1 = 1
                    break 
                if count2 == 5: 
                    win2 = 1
                    break 
                if count0 + count1 + count2 == 5:
                    break
                
            count0, count1, count2 = 0, 0, 0
            winner = win(win1, win2)
            if winner != 0:
                return winner
            x += 1
    if rot % 2 == 0: #undoing the rotation 
        rot = rot - 1 
        board = rotation(board, rot)
    else: 
        rot = rot + 1 
        board = rotation(board, rot)
    return 0



        
def win(win1, win2):
        if win1 == 1 and win2 == 0:
            return 1
        elif win2 == 1 and win1 == 0:
            return 2
        elif win1 == 1 and win2 == 1:
            return 3
        elif win1 == 0 and win2 == 0:
            return 0
        
        
def rotation(temp_board, rot):
    
    subgrid_rightUpper = [row[3:6] for row in temp_board[0:3]]
    subgrid_leftUpper = [row[0:3] for row in temp_board[0:3]]
    subgrid_leftLower = [row[0:3] for row in temp_board[3:6]]
    subgrid_rightLower = [row[3:6] for row in temp_board[3:6]]

    if rot == 1:
        subgrid_rightUpper = np.rot90(subgrid_rightUpper, -1)
        for i in range(3):
            for j in range(3,6):
                temp_board[i][j] = subgrid_rightUpper[i][j-3]
    elif rot == 2:
        subgrid_rightUpper = np.rot90(subgrid_rightUpper, 1)
        for i in range(3):
            for j in range(3,6):
                temp_board[i][j] = subgrid_rightUpper[i][j-3]
    elif rot == 3:
        subgrid_rightLower = np.rot90(subgrid_rightLower, -1)
        for i in range(3,6):
            for j in range(3,6):
                temp_board[i][j] = subgrid_rightLower[i-3][j-3]
    elif rot == 4:
        subgrid_rightLower = np.rot90(subgrid_rightLower, 1)
        for i in range(3,6):
            for j in range(3,6):
                temp_board[i][j] = subgrid_rightLower[i-3][j-3]
    elif rot == 5:
        subgrid_leftLower = np.rot90(subgrid_leftLower, -1)
        for i in range(3,6):
            for j in range(3):
                temp_board[i][j] = subgrid_leftLower[i-3][j]
    elif rot == 6:
        subgrid_leftLower = np.rot90(subgrid_leftLower, 1)
        for i in range(3,6):
            for j in range(3):
                temp_board[i][j] = subgrid_leftLower[i-3][j]
    elif rot == 7:
        subgrid_leftUpper = np.rot90(subgrid_leftUpper, -1)
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = subgrid_leftUpper[i][j]
    elif rot == 8:
        subgrid_leftUpper = np.rot90(subgrid_leftUpper, 1)
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = subgrid_leftUpper[i][j]
                
    return temp_board

def apply_move(board, turn, row, col, rot):
    print("Rotation in apply move: ", rot)
    if check_move(board, row, col):
        # Create a copy of the board
        temp_board = board.copy()  
        # Replacing the 0 with either 1 or 2
        temp_board[row][col] = turn
        temp_board = rotation(temp_board,rot)
        # display_board(temp_board)
        return temp_board
    else:
        # reason why move is invalid
        
        print("Invalid move at row", row, "column", col, "rotation", rot)

        display_board(board)
        return board


def check_move(board, row, col):
    if 0<= row <6 and 0<= col <6:
        if board[row][col] == 0:
            return True
        else:
            return False
    
        

def computer_move(board, turn, level):
    if turn == 1:
        player = 1
        computer = 2
    elif turn == 2:
        player = 2
        computer = 1

    if level == 1:
        
        #easy level 
        #computer plays randomly
        while True: #repeats random generation process until valid move is found 
            row = random.randint(0,5)
            col = random.randint(0,5)
            rot = random.randint(1,8) 
            if check_move(board, row, col):
                # print("Rotation in computer move: ", rot)
                apply_move(board, computer, row, col, rot)
                return row, col, rot
            else:
                continue
            
    if level == 2:
        while True: 
            row = random.randint(0,5)
            col = random.randint(0,5)
            rot = 1
            
             # check for a winning move
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        board[i][j] = 1
                        # try again with diff rotation value
                        while rot < 9:
                            # print("While loop rotation: ", rot)
                            # print("Row: ", i, "Col: ", j)
                            # print("Check victory: ", check_victory(board, 1, rot))
                            
                            if (check_victory(board, 1, rot) == 1):
                                # print("Rotation in computer move: ", rot)

                                row = i
                                col = j
                                if(check_move(board, row, col)):
                                    apply_move(board, computer, row, col, rot)
                                    return row, col, rot
                                
                                break
                            else:
                                rot += 1
                                continue
                        # all rotations have been tried
                        # try new i and j 
                        board[i][j] = 0
                        continue
            # if there is no winning move, check for a blocking move
                        

            # check for a blocking move
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        board[i][j] = 2
                        
                        while rot < 9:
                            if check_victory(board, 2, rot) == 2 or check_victory(board, 1, rot) != 1:
                                row = i
                                col = j
                                if(check_move(board, row, col)):
                                    apply_move(board, computer, row, col, rot)
                                    return row, col, rot
                            else:
                               
                                rot += 1
                                continue
                        board[i][j] = 0
                        continue
            # if there is no blocking move, play randomly
            while True:
                row = random.randint(0,5)
                col = random.randint(0,5)
                rot = random.randint(1,8) 
                if check_move(board, row, col):
                    apply_move(board, computer, row, col, rot)
                    return row, col, rot
                else:
                    continue
            
    return None
       

def menu(): 
    print("Welcome to Pentago!")
    print("1. Play against a friend")
    print("2. Play against the computer (easy)")
    print("3. Play against the computer (medium)")
    print("4. Exit")
    choice = input("Enter your choice: ")
    choice = int(choice)
    if choice == 1:
            board = [[0 for _ in range(6)] for _ in range(6)]
            display_board(board)
            print("You have decided to play with a friend")
            win = 0
            while(win == 0):
                #player 1's turn
                turn = 1
                if (win != 0):
                    break

                print("Player 1 input: ")
                row = int(input("Choose a row: "))
                col = int(input("Choose a column: ")) 
                rot = int(input("Choose a number for rotation: "))
                if (check_move(board, row, col) == False):
                    print("Invalid move. Try again.")
                    continue
                while(check_move(board, row, col)):
                    board = apply_move(board, 1, row, col, rot)
                    display_board(board)
                    win = check_victory(board, 1, rot)
                    if (win == 1):
                        print("Congrats! Player 1 has won!")
                        break

                    elif(win == 3):
                        print("Draw!")
                        break
                    elif(win == 2):
                        print("Congrats! Player 2 has won!")
                        break
                    else:
                        break
                        
                #player 2's turn
                if (win != 0):
                    break

                print("Player 2 input: ")
                row = int(input("Choose a row: "))
                col = int(input("Choose a column: "))
                rot = int(input("Choose a number for rotation: "))
                if (check_move(board, row, col) == False):
                    print("Invalid move. Try again.")
                    continue
                while(check_move(board, row, col)):
                    board = apply_move(board, 2, row, col, rot)
                    display_board(board)
                    win = check_victory(board, 2, rot)
                    if (win == 1):
                        print("Congrats! Player 1 has won!")
                        break
                    elif(win == 3):
                        print("Draw!")
                        break
                    elif(win == 2):
                        print("Congrats! Player 2 has won!")
                        break
                    else:
                        break
                       

                
    elif choice == 2:
            
            board = [[0 for _ in range(6)] for _ in range(6)]
            display_board(board)
            print("You have decided to play against the computer (easy)")
            win= 0
            display_board(board)
            # turn refers to player turn
            turn = input("Do you want to go first? (1/2): ")
            turn = int(turn)
            while (win == 0):
                
                if (turn == 1):
                    if (win != 0):
                        break
                    # player goes first
                    #player turn
                    print("Player input: ")
                    row = int(input("Choose a row: "))
                    col = int(input("Choose a column: ")) 
                    rot = int(input("Choose a number for rotation: "))
                    if (check_move(board, row, col) == False):
                        print("Invalid move. Try again.")
                    
                        continue
                    while(check_move(board, row, col)):
                        board = apply_move(board, 1, row, col, rot)
                       
                        display_board(board)
                        win = check_victory(board, 1, rot)
                        if (win == 1):
                            print("Congrats! Player 1 has won!")
                            break
                        elif(win == 3):
                                print("Draw!")
                                break
                        elif(win == 2):
                                print("Congrats! Computer has won!")
                                break
                        else:
                            break
    
                    # computer turn 
                    if (win != 0):
                        break
                    row,col,rot = computer_move(board, 1, 1)
                    print (" ")
                    display_board(board)
                    win = check_victory(board, 2, rot)
                    if (win == turn):
                        print("Player wins!")
                        break
                    elif (win == 3):
                        print("Draw!")
                        break
                    elif (win == 2):
                        print("Computer wins :(")
                        break

                if (turn == 2):
                    # computer goes first
                    # computer turn
                    if (win != 0):
                        break
                    row,col,rot = computer_move(board, 2, 1)
                    print (" ")
                    display_board(board)
                    win = check_victory(board, 1, rot)
                    if (win == turn):
                        print("Player wins!")
                        break
                    elif (win == 3):
                        print("Draw!")
                        break
                    elif (win == 1):
                        print("Computer wins :(")
                        break

                    #player turn
                    if (win != 0):
                        break
                    print("Player input: ")
                    row = int(input("Choose a row: "))
                    col = int(input("Choose a column: ")) 
                    rot = int(input("Choose a number for rotation: "))
                    if (check_move(board, row, col) == False):
                        print("Invalid move. Try again.")
                        continue
                    while(check_move(board, row, col)):
                        board = apply_move(board, 1, row, col, rot)
                        display_board(board)
                        win = check_victory(board, 1, rot)
                        if (win == turn):
                            print("Congrats! Player has won!")
                            break
                        elif(win == 3):
                            print("Draw!")
                            break
                        elif(win == 1):
                            print("Congrats! Computer has won!")
                            break
                        else:
                            break

            
            
    elif choice == 3:
            board = [[0 for _ in range(6)] for _ in range(6)]
            display_board(board)
            print ("You have decided to play against the computer (medium)")
            win=0
            display_board(board)
            turn = input("Do you want to go first? (1/2): ")
            turn = int(turn)
            while (win == 0):
              
                if (turn == 1):
                    # player goes first
                    #player turn
                    print("Player input: ")
                    row = int(input("Choose a row: "))
                    col = int(input("Choose a column: "))
                    rot = int(input("Choose a number for rotation: "))
                    if (check_move(board, row ,col)==False):
                        print ("Invalid move. Try again.")
                        continue
                    while(check_move(board, row, col)):
                        board = apply_move(board, 1, row, col, rot)
                        display_board(board)
                        win = check_victory(board, 1, rot)
                        if (win == 1):
                            print("Congrats! Player 1 has won!")
                            break
                        elif(win == 3):
                                print("Draw!")
                                break
                        elif(win == 2):
                                print("Congrats! Player 2 has won!")
                                break
                        else:
                            break
                        # computer turn
                    row,col,rot = computer_move(board, 1, 2)
                    print (" ")
                    display_board(board)
                    win = check_victory(board, 2, rot)
                    if (win == turn):
                        print("Player wins!")
                        break
                    elif (win == 3):
                        print("Draw!")
                        break
                    elif (win == 2):
                        print("Computer wins :(")
                        break
                        
                elif (turn == 2):
                    # computer goes first
                    # computer turn
                   row,col,rot = computer_move(board, 2, 2)
                   print (" ")
                   display_board(board)
                   win = check_victory(board, 1, rot)
                   if (win == turn):
                       print("Player wins!")
                   elif (win == 3):
                       print("Draw!")
                   elif (win == 2):
                       print("Computer wins :(")
    
                    #player turn
                   print("Player input: ")
                   row = int(input("Choose a row: "))
                   col = int(input("Choose a column: ")) 
                   rot = int(input("Choose a number for rotation: "))
                   if (check_move(board, row, col) == False):
                       print("Invalid move. Try again.")
                       continue
                   while(check_move(board, row, col)):
                       board = apply_move(board, 2, row, col, rot)
                       display_board(board)
                       win = check_victory(board, 31, rot)
                       if (win == 1):
                           print("Congrats! Player 1 has won!")
                       elif(win == 3):
                           print("Draw!")
                       elif(win == 2):
                           print("Congrats! Player 2 has won!")
                       else:
                           break
    
                    
            if (win == turn):
                print("Player wins!")
            elif (win == 3):
                print("Draw!")
            else:
                print("Computer wins :(")
                
    elif choice == 4:
        exit 
                
    else: 
        print("Error. Please input 1 to 4: ")
        menu()
        pass

if __name__ == "__main__":
    menu()
    