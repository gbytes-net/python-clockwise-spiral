def create_spiral(n):
    if type(n) != int or n < 1:
        return []
        
    matrix = []
    x = 1
    for i in range(n):
        xlist = []
        for j in range(n):
            xlist.append(0)
        matrix.append(xlist)
    
    limit_x_r, limit_y_d = n - 1, n - 1
    limit_x_l = 0
    limit_y_u = 1

    x, y, counter = 0, 0, 0
    direction = 'R'
    while not (limit_x_r < limit_x_l and limit_y_d < limit_y_u):
        counter += 1
        print(str(x) + "," + str(y) + "=" + str(counter))
        matrix[y][x] = counter
    
        if direction == 'R':
            if x == limit_x_r:
                direction = 'D'
                limit_x_r -= 1
            else:
                x += 1

        if direction == 'D':
            if y == limit_y_d:
                direction = 'L'
                limit_y_d -= 1
            else:
                y += 1

        if direction == 'L':
            if x == limit_x_l:
                direction = 'U'
                limit_x_l += 1
            else:
                x -= 1

        if direction == 'U':
            if y == limit_y_u:
                direction = 'R'
                limit_y_u += 1
                x += 1
            else:
                y -= 1
    print(matrix)
    return matrix
    
