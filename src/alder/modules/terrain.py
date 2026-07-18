def build_grid(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        grid.append(row)
    return grid

