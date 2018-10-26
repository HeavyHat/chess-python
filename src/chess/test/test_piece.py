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
    assert piece.__str__() == expected
