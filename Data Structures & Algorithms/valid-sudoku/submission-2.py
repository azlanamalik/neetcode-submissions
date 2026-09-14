class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        column_set = set()
        threebythree = set()

        for row_num, row in enumerate(board):
            for column_num, data in enumerate(row):

                # Ignore empty cells
                if data == ".":
                    continue

                # Check row
                if (row_num, data) in row_set:
                    return False
                row_set.add((row_num, data))

                # Check column
                if (column_num, data) in column_set:
                    return False
                column_set.add((column_num, data))

                box_row = row_num // 3
                box_column = column_num // 3

                if (box_row, box_column, data) in threebythree:
                    return False

                threebythree.add((box_row, box_column, data))

        return True