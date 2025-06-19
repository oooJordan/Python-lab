#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mossa_valida(board, a, b, current_player):
    if board[(a, b)] != ".":
        return False

    for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        r = a + r_offset
        c = b + c_offset
        if (r, c) in board and board[(r, c)] != "." and board[(r, c)] != current_player:
            return True

    return False

def aggiorno_scacchiera(board, row, col, current_player):
    for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        r = row + r_offset
        c = col + c_offset
        if (r, c) in board and board[(r, c)] != "." and board[(r, c)] != current_player:
            board[(r, c)] = current_player

                
def conto_pedine(board, mosse_disponibili, current_player):
    nero_count = 0
    bianco_count = 0
    mosse_disponibili[0] = False
    for coord in board:
        if board[coord] == "B":
            nero_count += 1
        elif board[coord] == "W":
            bianco_count += 1
        elif board[coord] == ".":
            if mossa_valida(board, coord[0], coord[1], current_player):
                mosse_disponibili[0] = True
                break
    return (nero_count, bianco_count)

def verifica_mosse_disponibili(board, current_player):
    for coord in board:
        if board[coord] == "." and mossa_valida(board, coord[0], coord[1], current_player):
            return True
    return False

def verifica_vincitore(board, current_player):
    nero_count, bianco_count = conto_pedine(board, [True], current_player)
    if nero_count > bianco_count:
        return "B"
    elif bianco_count > nero_count:
        return "W"
    else:
        return "P"

def verifica_tavole(board, current_player, nero_win, bianco_win, parita):
    if not verifica_mosse_disponibili(board, current_player):
        result = verifica_vincitore(board, current_player)
        if result == "B":
            nero_win[0] += 1
        elif result == "W":
            bianco_win[0] += 1
        else:
            parita[0] += 1
    else:
        for coord in board:
            if board[coord] == "." and mossa_valida(board, coord[0], coord[1], current_player):
                board_copy = board.copy()
                board_copy[(coord[0], coord[1])] = current_player
                aggiorno_scacchiera(board_copy, coord[0], coord[1], current_player)
                next_player = "W" if current_player == "B" else "B"
                verifica_tavole(board_copy, next_player, nero_win, bianco_win, parita)
                
                
def dumbothello(filename : str) -> tuple[int,int,int] :
    
    with open (filename, encoding='utf8' ) as file:
        lines = file.readlines()
    board = {(r, c): cell for r, row in enumerate(lines) for c, cell in enumerate(row.split())}

    nero_win = [0]
    bianco_win = [0]
    parita = [0]
    
    verifica_tavole(board, "B", nero_win, bianco_win, parita)

    return (nero_win[0], bianco_win[0], parita[0])


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
