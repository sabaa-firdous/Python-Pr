def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            
            if val == ".":
                continue
            
            # Identify which 3x3 box we are in
            box_idx = (r // 3) * 3 + (c // 3)

            # Check if value already exists in current row, column, or box
            if (val in rows[r] or 
                val in cols[c] or 
                val in boxes[box_idx]):
                return False

            # Add value to the sets
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True

# --- Test Case ---
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(f"Is this board valid? {is_valid_sudoku(board)}")