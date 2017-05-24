

def sum_diag(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return sum(matrix[0])+sum(matrix[1])
    else:
        left, right, total = 0, 0, 0
        right = len(matrix)-1
        for line in matrix:
            total+= (line[left]+line[right])
            left+=1
            right-=1
        return total

m1 = [[1]]

m2 = [[1,2],
      [3,4]]

m3 = [[1,1,1,1],
      [1,2,2,1],
      [1,3,3,1],
      [4,1,1,4]]

print(sum_diag(m1))