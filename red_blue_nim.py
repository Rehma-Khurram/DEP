import sys
class RedBlueNim:
    def __init__(self, red, blue, version='standard', player1='computer', depth=3):
        self.redMarbles = red
        self.blueMarbles = blue
        self.version = version
        self.currentTurn = player1
        self.searchDepth = depth

    def gameOver(self):
        if self.version == 'standard':
            return self.redMarbles == 0 or self.blueMarbles == 0
        else:
            return (self.redMarbles == 0 or self.blueMarbles == 0) and self.currentTurn == 'computer'

    def availableMoves(self):
        moves = []
        if self.redMarbles >= 2:
            moves.append((2, 0))
        if self.blueMarbles >= 2:
            moves.append((0, 2))
        if self.redMarbles >= 1:
            moves.append((1, 0))
        if self.blueMarbles >= 1:
            moves.append((0, 1))
        return moves

    def applyMove(self, red, blue):
        self.redMarbles -= red
        self.blueMarbles -= blue

    def revertMove(self, red, blue):
        self.redMarbles += red
        self.blueMarbles += blue

    def computeScore(self):
        return self.redMarbles * 2 + self.blueMarbles * 3

    def getPlayerMove(self):
        moves = self.availableMoves()
        print(f"Possible moves: {moves}")
        while True:
            try:
                user_input = input("Input your move as 'red blue' separated by space: ").strip().split()
                red, blue = int(user_input[0]), int(user_input[1])
                if (red, blue) in moves:
                    self.applyMove(red, blue)
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter two integers separated by a space.")

    def aiMove(self):
        _, best_move = self.minimax(self.searchDepth, -float('inf'), float('inf'), True)
        self.applyMove(best_move[0], best_move[1])
        print(f"Computer chooses: {best_move}")

    def minimax(self, depth, alpha, beta, isMaximizing):
        if self.gameOver() or depth == 0:
            return self.computeScore(), (0, 0)

        possible_moves = self.availableMoves()
        optimal_move = (0, 0)

        if isMaximizing:
            best_score = -float('inf')
            for move in possible_moves:
                self.applyMove(move[0], move[1])
                score, _ = self.minimax(depth - 1, alpha, beta, False)
                self.revertMove(move[0], move[1])
                if score > best_score:
                    best_score = score
                    optimal_move = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score, optimal_move
        else:
            best_score = float('inf')
            for move in possible_moves:
                self.applyMove(move[0], move[1])
                score, _ = self.minimax(depth - 1, alpha, beta, True)
                self.revertMove(move[0], move[1])
                if score < best_score:
                    best_score = score
                    optimal_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score, optimal_move

    def startGame(self):
        while not self.gameOver():
            print(f"Current state: Red marbles: {self.redMarbles}, Blue marbles: {self.blueMarbles}")
            if self.currentTurn == 'human':
                self.getPlayerMove()
                self.currentTurn = 'computer'
            else:
                self.aiMove()
                self.currentTurn = 'human'

        if self.version == 'standard':
            if self.currentTurn == 'human':
                print("Computer wins!")
            else:
                print("Human wins!")
        else:  # misere version
            if self.currentTurn == 'human':
                print("Human wins!")
            else:
                print("Computer wins!")
        print(f"Final score: {self.computeScore()}")

def parseArgs():
    if len(sys.argv) < 3:
        print("Usage: python red_blue_nim.py <num-red> <num-blue> [<version>] [<first-player>] [<depth>]")
        sys.exit(1)

    red = int(sys.argv[1])
    blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else 'standard'
    player1 = sys.argv[4] if len(sys.argv) > 4 else 'computer'
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else 3

    return red, blue, version, player1, depth

if __name__ == "__main__":
    red, blue, version, player1, depth = parseArgs()
    game = RedBlueNim(red, blue, version, player1, depth)
    game.startGame()
