from chess.piece import *
import pytest

@pytest.mark.parametrize( "piece,expected",
    [   (Pawn("Black"), "Black Pawn"),
        (Knight("Black"), "Black Knight"),
        (Bishop("Black"), "Black Bishop"),
        (Rook("Black"), "Black Rook"),
        (Queen("Black"), "Black Queen"),
        (King("Black"), "Black King"),
        (Pawn("White"), "White Pawn"),
        (Knight("White"), "White Knight"),
        (Bishop("White"), "White Bishop"),
        (Rook("White"), "White Rook"),
        (Queen("White"), "White Queen"),
        (King("White"), "White King")]
)
def test_name_for(piece, expected):
    assert piece.__str__() == expected, f"{expected} printed {piece.__str__()}."


@pytest.mark.parametrize( "piece,expected",
    [   (Pawn("Black"), "P"),
        (Knight("Black"), "k"),
        (Bishop("Black"), "B"),
        (Rook("Black"), "R"),
        (Queen("Black"), "Q"),
        (King("Black"), "K"),
        (Pawn("White"), "P"),
        (Knight("White"), "k"),
        (Bishop("White"), "B"),
        (Rook("White"), "R"),
        (Queen("White"), "Q"),
        (King("White"), "K")]
)
def test_symbol_for(piece, expected):
    assert piece.__repr__() == expected, f"Expected {expected}, got {piece.__repr__()}."


@pytest.mark.parametrize( "piece,expected",
    [   (Pawn("Black"), 3),
        (Knight("Black"), 8),
        (Bishop("Black"), 4),
        (Rook("Black"), 4),
        (Queen("Black"), 8),
        (King("Black"), 8),
        (Pawn("White"), 3),
        (Knight("White"), 8),
        (Bishop("White"), 4),
        (Rook("White"), 4),
        (Queen("White"), 8),
        (King("White"), 8)]
)
def test_move_count_for(piece, expected):
    assert len(piece.moves) == expected, f"{str(piece)} should have {expected} moves, but had {len(piece.moves)} moves."

@pytest.mark.parametrize( "piece,x,y,directional,can_take",
    [
        (Pawn("Black"), -1, 1, False,True),
        (Pawn("Black"), 1, 1, False,True),
        (Pawn("Black"), 0, 1, False,False),
        (Knight("Black"), 1, 3, False,True),
        (Knight("Black"), -1, 3, False,True),
        (Knight("Black"), 1, -3, False,True),
        (Knight("Black"), -1, -3, False,True),
        (Knight("Black"), 3, 1, False,True),
        (Knight("Black"), -3, 1, False,True),
        (Knight("Black"), 3, -1, False,True),
        (Knight("Black"), -3, -1, False,True),
        (Rook("Black"), 0, 1, True,True),
        (Rook("Black"), 1, 0, True,True),
        (Rook("Black"), 0, -1, True,True),
        (Rook("Black"), -1, 0, True,True),
        (Bishop("Black"), 1, 1, True,True),
        (Bishop("Black"), -1, 1, True,True),
        (Bishop("Black"), 1, -1, True,True),
        (Bishop("Black"), -1, -1, True,True),
        (Queen("Black"), 0, 1, True,True),
        (Queen("Black"), 0, -1, True,True),
        (Queen("Black"), 1, 0, True,True),
        (Queen("Black"), -1, 0, True,True),
        (Queen("Black"), 1, 1, True,True),
        (Queen("Black"), 1, -1, True,True),
        (Queen("Black"), -1, 1, True,True),
        (Queen("Black"), -1, -1, True,True),
        (King("Black"), 0, 1, False,True),
        (King("Black"), 0, -1, False,True),
        (King("Black"), 1, 0, False,True),
        (King("Black"), -1, 0, False,True),
        (King("Black"), 1, 1, False,True),
        (King("Black"), 1, -1, False,True),
        (King("Black"), -1, 1, False,True),
        (King("Black"), -1, -1, False,True)

    ])
def test_move_exists_for(piece,x,y,directional,can_take):
    move = Move(x,y,directional,can_take)
    assert move in piece.moves, f"{move}, {directional}, {can_take} not found in {piece} moves."


