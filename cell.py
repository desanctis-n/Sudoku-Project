class Cell:
  
  def __init__(self, value, row, col, screen): 
    self.value = value 
    self.row = row 
    self.col = col 
    self.screen = screen 
    self.sketched_value = 0 
    self.selected = False 
    
  def set_cell_value(self, value): 
    self.value = value 
    
  def set_sketched_value(self, value): 
    self.sketched value = value 
    
  def draw(self): 
    if self.selected: 
      pygame.draw.rect(self.screen, (255, 0, 0), (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL SIZE, CELL SIZE), 2)
    else:
      pygame.draw.rect(self.screen, (0, 0, 0), (self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL SIZE), 2) 
    if self.value != 0:
      font =pygame.font.SysFont("comicsansms", 30)
      text = font.render(str(self.value), True, (0, 0, 0))
      self.screen.blit(text, (self.col * CELL_SIZE CELL_SIZE / 2 - text.get_width() / 2, self.row * CELL_SIZE CELL SIZE / 2 - text.get height() / 2)) 
    if self.sketched value != 0:
      font = pygame.font.SysFont("comicsansms", 15) 
      text = font.render(str(self.sketched_value), True, (0, 0, 0)) 
      self .screen.blit(text,(self.col*CELL_SIZE+ CELL_SIZE/2.text.get_width()/2,self.row*CELL_SIZE+CELL_/2-text.get_height()/2))
      
