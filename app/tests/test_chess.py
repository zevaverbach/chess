from app.chess import Chess, Pawn, Knight, Rook, King, Queen, Bishop, Board
from pytest import raises

def test_that_there_is_a_chess_game():
    chess = Chess("Ro", "Bot")
    chess.start_game()
    assert chess

def test_that_pawn_is_instantiated_normally():
    with raises(Exception):
        pawn = Pawn()

    with raises(Exception):
        pawn = Pawn(position=(0, 1))
    
    pawn = Pawn(position=(0, 1), color="white")
    assert hasattr(pawn, 'position')

def test_that_pawn_is_positioned():
    pawn = Pawn((0, 1), color="white")
    assert pawn.position == (0, 1)

def test_set_board():
    Board.set()
    board_dict = Board.board
    print(board_dict)
    king = board_dict[(0, 4)]
    assert king.color == 'white'
    assert isinstance(king, King)

    print(dir(king))
    king = board_dict[(7, 4)]
    assert king.color == 'black'
    assert isinstance(king, King)

    queen = board_dict[(0, 3)]
    assert queen.color == 'white'
    assert isinstance(queen,Queen)

    queen = board_dict[(7, 3)]
    assert queen.color == 'black'
    assert isinstance(queen,Queen)
    
    rook = board_dict[(0, 0)]
    assert rook.color == "white"
    assert isinstance(rook, Rook)

    rook = board_dict[(0, 7)]
    assert rook.color == "white"
    assert isinstance(rook, Rook)
    
    rook = board_dict[(7, 0)]
    assert rook.color == "black"
    assert isinstance(rook, Rook)

    rook = board_dict[(7, 7)]
    assert rook.color == "black"
    assert isinstance(rook, Rook)

    knight = board_dict[(0, 1)]
    assert knight.color == "white"
    assert isinstance(knight, Knight)

    knight = board_dict[(0, 6)]
    assert knight.color == "white"
    assert isinstance(knight, Knight)
    
    knight = board_dict[(7, 1)]
    assert knight.color == "black"
    assert isinstance(knight, Knight)

    knight = board_dict[(7, 6)]
    assert knight.color == "black"
    assert isinstance(knight, Knight)

    bishop = board_dict[(0, 2)]
    assert bishop.color == "white"
    assert isinstance(bishop, Bishop)

    bishop = board_dict[(0, 5)]
    assert bishop.color == "white"
    assert isinstance(bishop, Bishop)
    
    bishop = board_dict[(7, 2)]
    assert bishop.color == "black"
    assert isinstance(bishop, Bishop)

    bishop = board_dict[(7, 5)]
    assert bishop.color == "black"
    assert isinstance(bishop, Bishop)
    
    for color, row in [('white', 1), ('black', 6)]:
        for col in range(8):
            pawn = board_dict[(row, col)]
            assert pawn.color == color
            assert isinstance(pawn, Pawn)