class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            row = set()
            for c in range(9):
                # check row
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] not in row:
                        row.add(board[r][c])
                    else:
                        return False
        for c in range(9):
            col = set()
            for r in range(9):
                # check row
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] not in col:
                        col.add(board[r][c])
                    else:
                        return False

        # check squ
        for square in range(9):
            squs = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in squs:
                        squs.add(board[row][col])
                    else:
                        return False


        return True
                    
                
                    