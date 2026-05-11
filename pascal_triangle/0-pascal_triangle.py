#!/usr/bin/env python3

def pascal_triangle(n):
    if n <= 0:
        return []
    
    #initialisation triangle
    triangle = [[1]]

    #create rows
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]# always star with a 1

        #num between the edge
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)# always end with 1
        triangle.append(new_row)#add the new line
    
    return triangle