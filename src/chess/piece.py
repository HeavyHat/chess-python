class Move(object):

    def __init__(self, x, y, directional=False, can_take=True):
        self.x = x
        self.y = y
        self.directional = directional
        self.can_take = can_take

    def __repr__(self):
        if self.directional:
            return f"Move along {self.x},{self.y}"
        return f"Move {self.y} up, {self.x} across."

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __hash__(self):
        return 11 * self.x + 13 * self.y + 7 * self.directional + 3 * self.can_take
    
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.x==other.x and self.y==other.y and self.can_take == other.can_take and self.directional==other.directional
        return False

class ChessPiece(object):

    def __init__(self, team_id, name):
        self._team_id = team_id
        self._name = name

    def __str__(self):
        return f"{self._team_id} {self._name}"

    def __repr__(self):
        return self._name[0]

    @property
    def team(self):
        return self._team_id

    @property
    def moves(self):
        return {}


class Pawn(ChessPiece):

    def __init__(self, team_id):
        super(Pawn, self).__init__(team_id, "Pawn")

    @property
    def moves(self):
        return {Move(0,1, can_take=False),
                Move(-1,1),
                Move(1,1)}


class Rook(ChessPiece):

    def __init__(self, team_id):
        super(Rook,self).__init__(team_id, "Rook")

    @property
    def moves(self):
        return {Move(0,1,directional=True),
                Move(1,0,directional=True),
                Move(0,-1,directional=True),
                Move(-1,0,directional=True)}


class Knight(ChessPiece):

    def __init__(self, team_id):
        super(Knight,self).__init__(team_id, "Knight")

    @property
    def moves(self):
        return {Move(1,3),
                Move(-1,3),
                Move(1,-3),
                Move(-1,-3),
                Move(3,1),
                Move(-3,1),
                Move(3,-1),
                Move(-3,-1)}

    def __repr__(self):
        return self._name[0].lower()

class Bishop(ChessPiece):

    def __init__(self, team_id):
        super(Bishop,self).__init__(team_id, "Bishop")

    @property
    def moves(self):
        return {Move(1,1,True),
                Move(-1,1,True),
                Move(1,-1,True),
                Move(-1,-1,True)}


class Queen(ChessPiece):

    def __init__(self, team_id):
        super(Queen,self).__init__(team_id, "Queen")

    @property
    def moves(self):
        return {Move(1,0,True),
                Move(-1,0,True),
                Move(0,-1,True),
                Move(0,1,True),
                Move(1,1,True),
                Move(-1,1,True),
                Move(1,-1,True),
                Move(-1,-1,True)}


class King(ChessPiece):

    def __init__(self, team_id):
        super(King,self).__init__(team_id, "King")

    @property
    def moves(self):
        return {Move(1,0),
                Move(-1,0),
                Move(0,-1),
                Move(0,1),
                Move(1,1),
                Move(-1,1),
                Move(1,-1),
                Move(-1,-1)}
