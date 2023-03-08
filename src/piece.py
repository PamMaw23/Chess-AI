

class Piece:

    def __init__(self, name, color, value, texture, texture_rect=None):
        pass

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color = 'white' else 1
        # the if statement below is the same as the statement above
        # if color == 'white':
        #     self.dir = -1
        # else :
        #     self.dir = 1