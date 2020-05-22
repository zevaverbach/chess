from collections import namedtuple
from typing import Tuple, List, NewType
    
class NotEnough(Exception):
    pass

class Piece:
    def __init__(self, position: Tuple[int, int], color: str):
        self.color = color
        self.position = position
        
    def __repr__(self):
        piece_name = str(self.__class__).replace("class 'app.chess.", "").replace("'", "")
        return f"{piece_name} {self.position}"


class Pawn(Piece):
    pass

class Rook(Piece):
    pass
      
class King(Piece):
    pass
 
class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Knight(Piece):
    pass
      

class Chess:
    """a dummy chess class"""
    def __init__(self, *player_names):
        print("Hi I am a chess object")
        self.players = [Player(n) for n in player_names]
        if len(self.players) > 2:
            raise NotImplementedError(
                f"Games with {len(self.players)} are not implemented yet")
        if len(self.players) < 2:
            raise NotEnough("Not enough players") 

        self.board = Board

    def start_game(self):
        self.board.set()
        print("Ready to start!")


Player = namedtuple('Player', ['first'])

Position = NewType("Position", Tuple[int, int])

def get_kings_and_queens():
    KING_COL, QUEEN_COL = 4, 3
    return [
        (King, (0, KING_COL), 'white'),
        (King, (7, KING_COL), 'black'),
        (Queen, (0, QUEEN_COL), 'white'),
        (Queen, (7, QUEEN_COL), 'black'),
    ]

def get_pawns():
    return [
        (Pawn, (row, col), color) 
        for row, color in ((1, 'white'), (6, 'black'))
        for col in range(8)
    ]

def get_first_row_pieces_except_king_and_queen() -> List[Tuple[Piece, Position, str]]:
    # TODO: refactor this to use column numbers from the classes themselves
    OFFSET_PIECE_TYPE_LOOKUP = {0: Rook, 1: Knight, 2: Bishop}
    first_row_pieces = []
    for row, color in ((0, 'white'), (7, 'black')):
        for mirrored_column in range(3):
            piece_type = OFFSET_PIECE_TYPE_LOOKUP[mirrored_column]
            column_indices = (0 + mirrored_column), (7 - mirrored_column)
            for col_index in column_indices:
                first_row_pieces.append((piece_type, (row, col_index), color))
    return first_row_pieces
           
def get_pieces():
    return (
        get_first_row_pieces_except_king_and_queen()
        + get_kings_and_queens()
        + get_pawns()
    )


PIECES = get_pieces()

class Board:

    board = {}

    @classmethod
    def set(cls):
        for piece_type, position, color in PIECES:
            cls.board[position] = piece_type(position=position, color=color)
    
    def __repr__(self):
        return self.board