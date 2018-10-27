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
