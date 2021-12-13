import numpy as np
inputFile = open('input.txt','r')

draws = inputFile.readline().strip().split(',')
draws = [int(s) for s in draws]
boards_input = inputFile.read().split('\n\n')
boards_input = [s.strip().replace('\n', ' ').replace('  ', ' ').split(' ') for s in boards_input]
boards_input = np.array(boards_input).astype(int)

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

def play_bingo(boards):
    hit_mask = np.zeros((len(boards),25), dtype=bool)
    for draw in draws:
        current_mask = boards == draw

        hit_mask = np.ma.mask_or(hit_mask, current_mask, copy=False)
        hl = np.ma.size(hit_mask)
        if np.ma.size(hit_mask) <= 1:
            continue
        for i in range(len(hit_mask)):
            found_bingo = is_bingo(hit_mask[i])
            if found_bingo:
                board_not_hits = np.ma.masked_array(boards[i], mask = hit_mask[i])
                not_hits_sum = board_not_hits.sum()
                print(board_not_hits)
                print(str(not_hits_sum) + ' * ' + str(draw) + ' = ' + str(not_hits_sum * draw))
                return i
    return -1

play_bingo(boards_input)

# Part 2
remaining_boards = boards_input
while True:
    if len(remaining_boards) == 0:
        break
    print('---')
    idx = play_bingo(remaining_boards)
    if idx == -1:
        break
    remaining_boards = np.delete(remaining_boards,(idx), axis=0)
