
class LifeGrid:

    DEAD = 0
    LIVE = 1

    def __init__(self,ROWS, COLS):
        self._grid = [[0 for c in range(COLS)] for r in range(ROWS)]
    
    def get_numRows(self):
        return len(self._grid)
    def get_numCols(self):
        return len(self._grid[0])
    def getGrid(self):
        return self._grid
    
    def configure(self, coord_list):
        for r in range(self.get_numRows()):
            for c in range(self.get_numCols()):

                if (r,c) in coord_list:
                    self._grid[r][c] = self.LIVE
                else:
                    self._grid[r][c] = self.DEAD

    # Using Draw Functions Instead..

    # def __str__(self):
    #     result = ""
    #     for row in self._grid:
    #         result += f"{row}\n"
    #     return result

    def numLiveNeighbours(self, cell):
        r,c = cell
        count = 0
        
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0: # skipping center cell
                    continue
                if r+i < 0 or c+j < 0: # negative out of bound
                    continue
                if r+i >= ROWS or c+j >= COLS: # length out of bound
                    continue
                if self._grid[r+i][c+j] == self.LIVE:
                    count+=1
        return count 




    def isLiveCell(self, row,col):
        return self._grid[row][col] == self.LIVE

    def setCell(self, row, col):
        self._grid[row][col] = self.LIVE
    def clearCell(self, row, col):
        self._grid[row][col] = self.DEAD

def evolve(grid: LifeGrid):
    live_cells = []
    
    for r in range(grid.get_numRows()):
        for c in range(grid.get_numCols()):

            neighbours = grid.numLiveNeighbours((r,c))
            if (neighbours == 2 and grid.isLiveCell(r,c)) or neighbours == 3:
                live_cells.append((r,c))

    grid.configure(live_cells)

def draw(grid: LifeGrid):
    gridmap = grid.getGrid()
    for i in range(grid.get_numRows()):
        for j in range(grid.get_numCols()):
            if gridmap[i][j] == 1:
                print("@", end=" ")
            else:
                print(".", end=" ")
        print()  

# Book Example in Listing 2.4
li = [(2,2),(2,1),(1,2),(2,3)]

# li = [(3,3),(1,3),(3,1),(4,0),(0,4),(0,0),(1,1),(2,2),(3,3),(4,4)] ## (2)
# li = [(0,1),(1,1),(2,1),(3,1),(4,1),(0,3),(1,3),(2,3),(3,3),(4,3),(4,0),(4,4)] ## (3)

# (4)
# li= [(0,0),(0,1),(0,2),(0,3),(0,4), 
#     (1,0),(1,1),(1,2),(1,3),(1,4),
#     (2,0),(2,1),(2,2),(2,3),(2,4),
#     (3,0),(3,1),(3,2),(3,3),(3,4),
#     (4,0),(4,1),(4,2),(4,3),(4,4)]

# (5)
# li = [(0,2), (1,2), (2,0), (2,1), (2,2), (2,3), (2,4), (3,2), (4,2)]

# (6)
# li = [(0,0),(0,1),(0,3),(0,4),(4,0),(4,1),(4,3),(4,4),(1,1),(3,1),(1,3),(3,3)]

# (7)
# li = [(0,0),(0,1),(1,0),(12,12),(12,11),(11,12),(1,2),(3,2),(3,4),(5,4),(5,6),(7,6),(7,8),(9,8),(9,10),(11,10)]


# li = [(2,2),(2,1),(1,2),(2,3),(3,1),(3,2)]


ROWS = int(input("Enter Height (rows) of Grid: "))
COLS = int(input("Enter Width (Cols) of Grid: "))
NUM_GEN = int(input("Enter Number of Generations: "))

def main():
    grid = LifeGrid(ROWS, COLS)
    grid.configure(li)
    print("Gen-Number: 0")
    draw(grid)
    
    for i in range(1,NUM_GEN+1):
        evolve(grid)
        print(f"Gen-Number: {i}")
        draw(grid)
main()

