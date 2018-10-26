class Move(object):

    def __init__(self, x, y, directional=False):
        self.x = x
        self.y = y
        self.directional = directional

    def __repr__(self):
        if self.directional:
            return f"Move along {self.x},{self.y}"
        return f"Move {self.y} up, {self.x} across."


class ChessPiece(object):

    def __init__(self, team_id, name):
        self.__team_id = team_id
        self.__name = name

    def __str__(self):
        return f"{self.__team_id} {self.__name}"

    def __repr__(self):
        return self.__name[0]

    @property
    def team(self):
        return self.__team_id

    @property
    def moves(self):
        return []


class Pawn(ChessPiece):

    def __init__(self, team_id):
        super(Pawn, self).__init__(team_id, "Pawn")

    @property
    def moves(self):
        return []


class Rook(ChessPiece):

    def __init__(self, team_id):
        super(Rook,self).__init__(team_id, "Rook")

    @property
    def moves(self):
        return []


class Knight(ChessPiece):

    def __init__(self, team_id):
        super(Knight,self).__init__(team_id, "Knight")

    @property
    def moves(self):
        return []


class Bishop(ChessPiece):

    def __init__(self, team_id):
        super(Bishop,self).__init__(team_id, "Bishop")

    @property
    def moves(self):
        return []


class Queen(ChessPiece):

    def __init__(self, team_id):
        super(Queen,self).__init__(team_id, "Queen")

    @property
    def moves(self):
        return []


class King(ChessPiece):

    def __init__(self, team_id):
        super(King,self).__init__(team_id, "King")

    @property
    def moves(self):
        return []
