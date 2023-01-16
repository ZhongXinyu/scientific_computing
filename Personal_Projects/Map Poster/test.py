def isValidSudoku(board):
        squarelocation=[
            [-1,-1],[-1,0],[-1,1],
            [0,-1],[0,0],[0,1],
            [1,-1],[1,0],[1,1],
        ]
        for i in range (9):
            horizontal_list=[0,0,0,0,0,0,0,0,0,0]
            vertical_list=[0,0,0,0,0,0,0,0,0,0]
            square_list=[0,0,0,0,0,0,0,0,0,0]
            for j in range (9):
                # Horizontal
                if board[i][j] != ".":
                    if horizontal_list[int(board[i][j])-1]==0:
                        horizontal_list[int(board[i][j])-1]=1
                    else:
                        return (bool(False))
                # Vertical 
                if board[j][i] != ".":
                    if vertical_list[int(board[j][i])-1]==0:
                        vertical_list[int(board[j][i])-1]=1
                    else:
                        return (bool(False))
                # Square
                ii=5+squarelocation[i][0]*3+squarelocation[j][0]-1
                jj=5+squarelocation[i][1]*3+squarelocation[j][1]-1
                if board[ii][jj] !=".":
                    if square_list[int(board[ii][jj])-1]==0:
                        square_list[int(board[ii][jj])-1]=1
                    else:
                        return (bool(False))
        return (bool(True))

def solveSudoku(board):
        """
        Do not return anything, modify board in-place instead.
        """
        i=0
        while i<9:
            j=0
            while j<9:
                if j==8 and i==8 and board[i][j] !=".":  #if reach the last grid, then return true.
                    return True
                if board[i][j] !=".": #if a number, look for the next one
                    j+=1
                else: 
                    for n in range (9):
                        board[i][j]=str(n)
                        if isValidSudoku(board)==bool(True):  
                            if solveSudoku(board):
                                return True
                    board[i][j]='.'
                    #print ("False")
                    return False
            i+=1

board=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print (solveSudoku(board))
print (board)
