from board import Direction, Rotation, Action
from random import Random

class Player:
    def choose_action(self, board):
        raise NotImplementedError

class AbdulsPlayer(Player):

    def choose_action(self, board):
        best_moves = self.find_best_moves(board)
        return best_moves
    
    def calculate_score(self, board_initial, board, height_weight, cleared_weight, holes_weight, bumpy_weight):
        return (
            height_weight * self.real_height(board) +
            holes_weight * self.holes(board) +
            cleared_weight * self.blocks_cleared(board_initial, board) +
            bumpy_weight * self.bumpiness(board)
        )


    def find_best_moves(self, board):
        best_score, ideal_rotation, ideal_direction = -float('inf'), 0, 0

        height_weight, cleared_weight, holes_weight, bumpy_weight = -2.192, 5.535, -5.984, -2.22


        for rotations in range(4):
            for move in range(-5, 5):
                clone, clone_initial = self.clone_boards(board, rotations, move)

                for rotations2 in range(4):
                    for move2 in range(-5, 5):
                        clone2 = self.clone_board(clone, rotations2, move2)

                        score = self.calculate_score(clone_initial, clone2, height_weight, cleared_weight, holes_weight,
                                                bumpy_weight)
                        if score > best_score:
                            best_score, ideal_rotation, ideal_direction = score, rotations, move

        if self.max_height(board) < 3 and board.bombs_remaining > 0:
            return Action.Bomb

        final_moves = self.construct_final_moves(ideal_rotation, ideal_direction)
        return final_moves

    def clone_boards(self, board, rotations, move):
        clone = board.clone()
        clone_initial = board.clone()

        self.apply_rotations(clone, rotations)
        move = self.move_left_or_right(clone, move)

        try:
            clone.move(Direction.Drop)
        except:
            pass

        return clone, clone_initial

    def clone_board(self, board, rotations, move):
        clone = board.clone()

        self.apply_rotations(clone, rotations)
        move = self.move_left_or_right(clone, move)

        try:
            clone.move(Direction.Drop)
        except:
            pass

        return clone

    def apply_rotations(self, board, rotations):
        for _ in range(rotations):
            try:
                board.rotate(Rotation.Clockwise)
            except:
                break

    def move_left_or_right(self, board, move):
        for _ in range(abs(move)):
            try:
                if move < 0:
                    board.move(Direction.Left)
                else:
                    board.move(Direction.Right)
            except:
                move = self.handle_move_exception(move)
                break
        return move

    def handle_move_exception(self, move):
        return move + 1 if move < 0 else move - 1

    def construct_final_moves(self, ideal_rotation, ideal_direction):
        final_moves = []
        final_moves += [Rotation.Clockwise] * ideal_rotation
        final_moves += [Direction.Left] * abs(ideal_direction) if ideal_direction < 0 else [Direction.Right] * abs(ideal_direction)
        final_moves.append(Direction.Drop)
        return final_moves

    def calculate_score(self, board_initial, board, height_weight, cleared_weight, holes_weight, bumpy_weight):
        return (
            height_weight * self.real_height(board) +
            holes_weight * self.holes(board) +
            cleared_weight * self.blocks_cleared(board_initial, board) +
            bumpy_weight * self.bumpiness(board)
        )

    def max_height(self, board):
        return min([y for x, y in board.cells]) if board.cells else 100

    def real_height(self, board):
        return sum([24 - y for x, y in board.cells if (x, y + 1) not in board.cells])

    def holes(self, board):
        holes_total = 0
        for x, y in board.cells:
            if y > 24 and (x, y + 1) not in board.cells:
                holes_total += self.calculate_hole_score(y, 10, 20, 500, 19, 5000, 17, 50000, 16, 100000, 15, 100000000)
        return holes_total

    def calculate_hole_score(self, y, *thresholds):
        hole_score = 0
        for i in range(0, len(thresholds), 2):
            if y > thresholds[i]:
                hole_score += thresholds[i + 1]
        return hole_score

    def blocks_cleared(self, board_before, board_after):
        eliminated = len(board_before.cells) - len(board_after.cells)
        return self.calculate_blocks_cleared_score(eliminated)

    def calculate_blocks_cleared_score(self, eliminated):
        if 0 < eliminated <= 10:
            return -18
        elif 10 < eliminated <= 20:
            return -2
        elif 20 < eliminated <= 30:
            return 500
        elif 30 < eliminated:
            return 250000
        else:
            return 0

    def max_column_height(self, board, x):
        return 24 - min([y for col_x, y in board.cells if col_x == x], default=24)

    def bumpiness(self, board):
        return sum([abs(self.max_column_height(board, x) - self.max_column_height(board, x + 1)) for x in range(9)])

seed = 2023
SelectedPlayer = AbdulsPlayer