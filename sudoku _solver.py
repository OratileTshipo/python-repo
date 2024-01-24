class Board:
    # implement the _init__ method to allow creation of class instances
    def __init__(self,board):
        # initialise the instance variables and assign parameter values
        self.board = board

    # implement the __str__method, its called automatically when you use the str() function or print() call on the instance
    def __str__(self):
        # draw upper border of the board
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

        """Enumeration is a convenient way to keep track of both the element and its position on a list.
          The enumerate() function is a built-in function in Python that takes an iterable (such as a list,
          tuple, or string) and returns an iterator that produces tuples containing indices and 
          corresponding values from the iterable"""
        
        for index,line in enumerate(self.board):
            # initialise variables to store contents of rows in board
            row_list = []

            # turn every line of board into a 3x3 mini-board, which will be assigned a square_no as the current seqment of baord
            for square_no,part in enumerate([line[:3],line[3:6],line[6:]],start=1):

                # every sliced list of the original row/line is  joined to fow rows
                row_square = '|'.join(str(item) for item in part)
                # add items from row_square iterable, not the whole object
                row_list.extend(row_square)

                # check if the current seqment is not the last in a 3x3 mini-board
                if square_no != 3:
                    # close the end of the board, add object at end of list
                    row_list.append('||')
                    

            # create string representation of board, with spaces between elements of row_list
            row = f'|| {" ".join(row_list)}\n'
            row_empty = row.replace('0',' ') 
            board_string += row_empty   
            # check if index is the last row of the board
            if index < 8:
                # verify if its the last row in the 3x3 mini-baord
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines
        return board_string
    
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            # try to return the values row and col if they exists
            try:
                col = contents.index(0)
                return row,col
            # catch exception of ValueError if 0 is not found
            except ValueError:
                pass
        return None

    # check if given number can be inserted into a specified row of board
    def valid_in_row(self,row,num):
        if num not in self.board[row]:
            return True
        else:
            return False
        
    # check if given number can be inserted into specified column within current row
    def valid_in_col(self,col,num):
        # the expression inside the all() generator function returns a list with true of false
        # all() checks if all items in iterable is not = to num
        return all(
            self.board[row][col] != num
            for row in range(9)
            )
    
    # check if a number can be inserted in the 3x3 mini-board
    def valid_in_square(self,row,col,num):
        # initialise starting variables
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for row_num in range(row_start,row_start+3):
            for col_num in range(col_start,col_start+3):
                if self.board[row_num][col_num] == num:
                    print(f'number: {num} cannot be inserted!')
                    return True
        return False
    
    # check if number is a valid choice for an empty cell and 3x3 mini-board
    def is_valid(self,empty,num):
        row, col = empty
        valid_in_row = self.valid_in_row(row,num)
        valid_in_col = self.valid_in_col(col,num)
        valid_in_square = self.valid_in_square(row,col,num)
        return all([valid_in_row,valid_in_col,valid_in_square])
    
    def sudoku_solver(self):
        if next_empty  := self.find_empty_cell() is None:
            return True
        else:
            for guess in range(1,10):
                if self.is_valid(next_empty,guess):
                    row,col = next_empty
                    self.board[row][col] = guess
                    if self.sudoku_solver():
                        return True
                    else:
                        self.board[row][col] = 0
        return False
    
# draw board and solve puzzel
def solve_sudoku(board):
        # initialise board
        gameboard = Board(board)
        print(f'\nPuzzel to solve: \n{gameboard}')
        if gameboard.sudoku_solver():
            print(f'\nSolved puzzel: \n{gameboard}')
        else:
            print('\nThe provided puzzle is unsolvable.')
            # return instance of the class
        return gameboard





puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)




