

START = [[1, 2,  3,  4],
         [5, 6,  7,  8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

END = [[13, 9, 5, 1],
       [14, 10, 6, 2],
       [15, 11, 7, 3],
       [16, 12, 8, 4]]


def rotateArray(start):

    # Initiate End
    end = []

    # Fill End to be pre-set size
    for i in range(len(start)):
        end.append([None] * len(start))

    # Starting Rotation
    newRow = 0   
    # Iterate over the row
    for i in range(len(start))[::-1]: 
        newColumn = 0

        # Iterate over the column
        for j in range(len(start[i])):

            # Assign the new position with the old value
            end[newColumn][newRow] = start[i][j]
            newColumn += 1

        newRow += 1


    return end

def main():
    rotated = rotateArray(START)
    print(rotated)

if __name__ == '__main__':
    main()