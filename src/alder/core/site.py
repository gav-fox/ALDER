from alder.modules.terrain import build_grid
class Site:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = build_grid(rows,cols)
        