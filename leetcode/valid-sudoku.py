class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # setup three dictionaries/sets to store values 
        # Hashsets can be used to determine if there was a duplicate or not
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        # Traverse through the board. 0 to 8 is 9 values so completes the board
        for r in range(9):
            for c in range(9):
                
                # check if the value is . and continue if it is
                if board[r][c] == '.':
                    continue
                # check if there is a duplicate in rows or columns.
                # r // 3, c //3 puts the marker on a specific 3 x 3 grid and then we can check duplicates
                # in the 3 x 3 box
                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or 
                board[r][c] in squares[r // 3, c // 3]):

                    return False
                
                # add the values to hashset if there is no duplicate
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        
        return True