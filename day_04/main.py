import numpy as np
inputFile = open('input.txt','r')

draws = inputFile.readline().strip().split(',')
draws = [int(s) for s in draws]
boards = inputFile.read().split('\n\n')
boards = [s.strip().replace('\n', ' ').replace('  ', ' ').split(' ') for s in boards]
boards = np.array(boards).astype(int)

boards_hit =  [x[:] for x in [[False] * 25] * len(boards)]

def is_bingo(board):
    h1 = board[0] and board[1] and board[2] and board[3] and board[4]
    h2 = board[5] and board[6] and board[7] and board[8] and board[9]
    h3 = board[10] and board[11] and board[12] and board[13] and board[14]
    h4 = board[15] and board[16] and board[17] and board[18] and board[19]
    h5 = board[20] and board[21] and board[22] and board[23] and board[24]
    
    v1 = board[0] and board[5] and board[10] and board[15] and board[20]
    v2 = board[1] and board[6] and board[11] and board[16] and board[21]
    v3 = board[2] and board[7] and board[12] and board[17] and board[22]
    v4 = board[3] and board[8] and board[13] and board[18] and board[23]
    v5 = board[4] and board[9] and board[14] and board[19] and board[24]
    return h1 or h2 or h3 or h4 or h5 or v1 or v2 or v3 or v4 or v5

hit_mask = np.zeros((len(boards),25), dtype=bool)
found_bingo = False
for draw in draws:
    current_mask = boards == draw

    hit_mask = np.ma.mask_or(hit_mask, current_mask, copy=False)

    for i in range(len(hit_mask)):
        found_bingo = is_bingo(hit_mask[i])
        if found_bingo:
            board_not_hits = np.ma.masked_array(boards[i], mask = hit_mask[i])
            not_hits_sum = board_not_hits.sum()
            print(board_not_hits)
            print(str(not_hits_sum) + ' * ' + str(draw) + ' = ' + str(not_hits_sum * draw))
            break
    if found_bingo:
        break
