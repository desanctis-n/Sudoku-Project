class SudokuGenerator:
	
	def __init__(self, row_length, removed_cells):
		self.row_length = row_length
        	self.removed_cells = removed_cells
        	self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        	self.generate_board()
		self.box_length = sqrt(row_length) 

    	def get_board(self): 
		return self.board

    	def print_board(self): 
		for row in self.board:
			print(row)
			
	def valid_in_row(self, row, num):
        	for i in range(self.row_length):
            		if self.board[row][i] == num:
                		return False
        	return True

    	def valid_in_col(self, col, num):
        	for i in range(self.row_length):
			if self.board[i][col] == num:
				return False
		return True

    	def valid_in_box(self, row_start, col_start, num):
        	# Check if the given number is present in the 3x3 box from (row_start, col_start) to (row_start + 2, col_start + 2)
        	for row in range(row_start, row_start + 3):
            		for col in range(col_start, col_start + 3):
                		if self.board[row][col] == num:
                    		return False
        	return True
	def is_valid(self, row, col, num):
      		# Check if the given number is within the valid Sudoku range (1-9)
        	if num < 1 or num > 9:
            		return False
		# Check if the given number can be placed at position (row, col) in the board
        	# Check if the number is present in the same column
        	for r in range(9):
            		if self.board[r][col] == num:
                		return False
        	# Check if the number is present in the same row
        	for c in range(9):
            		if self.board[row][c] == num:
                		return False
        	# Check if the number is present in the 3x3 box containing the cell (row, col)
        	box_row_start = row - row % 3
        	box_col_start = col - col % 3
        	return self.valid_in_box(box_row_start, box_col_start, num)
	
	def fill_box(self, row_start, col_start):
        	unused_nums = self.unused_in_box(row_start, col_start)
        	random.shuffle(unused_nums)
        	for i in range(row_start, row_start + 3):
            		for j in range(col_start, col_start + 3):
                		if self.board[i][j] == 0:
                    			self.board[i][j] = unused_nums.pop()
					
	def fill_diagonal(self):
        	for i in range(0, self.row_length, 3):
            		self.fill_box(i, i)
	
	def fill_remaining(self, row, col):
        	if col >= self.row_length and row < self.row_length - 1:
            		row += 1
            		col = 0
        	if row >= self.row_length and col >= self.row_length:
            		return True

        	if row < 3:
            		if col < 3:
                		col_start = 0
            		elif col < 6:
                		col_start = 3
            		else:
                		col_start = 6
            		row_start = 0
        	elif row < 6:
            		if col < 3:
                		col_start = 0
            		elif col < 6:
                		col_start = 3
            		else:
                		col_start = 6
            		row_start = 3
        	else:
            		if col < 3:
                		col_start = 0
            		elif col < 6:
                		col_start = 3
            		else:
                		col_start = 6
            		row_start = 6
			
	if self.board[row][col] != 0:
		return self.fill_remaining(row, col + 1)
	
	for num in range(1, 10):
        	if self.is_valid(row, col, num):
            		self.board[row][col] = num
            		if self.fill_remaining(row, col + 1):
                		return True
            	self.board[row][col] = 0

    	return False

	def remove_cells(self, num_cells_to_remove=20):
        	# Remove the specified number of cells from the board randomly
        	removed_cells = set()
        	while len(removed_cells) < num_cells_to_remove:
            		row = random.randint(0, 8)
            		col = random.randint(0, 8)
            		if (row, col) not in removed_cells and self.board[row][col] != 0:
                		self.board[row][col] = 0
                		removed_cells.add((row, col))
