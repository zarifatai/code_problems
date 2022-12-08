def flood_fill(image, sr, sc, color):
    curr_color, rows, cols = image[sr][sc], len(image), len(image[0])

    def bfs(i, j):
        image[i][j] = color
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < rows and 0 <= y < cols and image[x][y] == curr_color:
                bfs(x, y)

    if curr_color != color:
        bfs(sr, sc)
    return image
