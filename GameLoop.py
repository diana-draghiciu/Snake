class GameLoop:
    def __init__(self, game):
        self._repo = game
        self.done = 0
        self.last_op = 'up'

    def print_board(self):
        print(str(self._repo))

    def check_if_end_game(self, l, c):
        """
        This function checks if the game has ended (self.done marks the interruption of the game loop)
        :param l: line index
        :param c: column index
        :return: True if ended/ False if not
        """
        if l < 0 or l >= len(self._repo.board) or c < 0 or c >= len(self._repo.board):
            self.done = 1
            return True
        if self._repo.board[l][c] == 3:
            self.done = 1
            return True
        return False

    def move(self, command_params=0):
        if command_params==0:
            if self.last_op == 'up':
                self.up()
            elif self.last_op == 'down':
                self.down()
            elif self.last_op == 'left':
                self.left()
            elif self.last_op == 'right':
                self.right()
        else:
            try:
                int(command_params)
            except ValueError as va:
                print("Input not an integer!")
            else:
                for i in range(0,int(command_params)):
                    if self.last_op == 'up':
                        self.up()
                    elif self.last_op == 'down':
                        self.down()
                    elif self.last_op == 'left':
                        self.left()
                    elif self.last_op == 'right':
                        self.right()

    def up(self, command_params=0):
        if self.last_op=='down':
            raise ValueError("You cannot turn 180 degrees")
        self.last_op='up'
        l = self._repo.snake[0]
        c = self._repo.snake[1]
        if not self.check_if_end_game(l - 1, c):
            if self._repo.board[l - 1][c] == 1:
                self._repo.randomise_apples(len(self._repo.board[0]), 1) #adds a new apple
                self._repo.snake.append(0)
                self._repo.snake.append(0)
            self._repo.change_snake_pos(l - 1, c)
            #self.print_board()
        else:
            raise Exception("Game over!")

    def down(self, command_params=0):
        if self.last_op=='up':
            raise ValueError("You cannot turn 180 degrees")
        self.last_op = 'down'
        l = self._repo.snake[0]
        c = self._repo.snake[1]
        if not self.check_if_end_game(l + 1, c):
            if self._repo.board[l + 1][c] == 1:
                self._repo.randomise_apples(len(self._repo.board[0]), 1)
                self._repo.snake.append(0)
                self._repo.snake.append(0)
            self._repo.change_snake_pos(l + 1, c)
            #self.print_board()
        else:
            raise Exception("Game over!")

    def right(self, command_params=0):
        if self.last_op=='left':
            raise ValueError("You cannot turn 180 degrees")
        self.last_op = 'right'
        l = self._repo.snake[0]
        c = self._repo.snake[1]
        if not self.check_if_end_game(l, c + 1):
            if self._repo.board[l][c + 1] == 1:
                self._repo.randomise_apples(len(self._repo.board[0]),1)
                self._repo.snake.append(0)
                self._repo.snake.append(0)
            self._repo.change_snake_pos(l, c + 1)
            #self.print_board()
        else:
            raise Exception("Game over!")

    def left(self, command_params=0):
        if self.last_op=='right':
            raise ValueError("You cannot turn 180 degrees")
        self.last_op = 'left'
        l = self._repo.snake[0]
        c = self._repo.snake[1]
        if not self.check_if_end_game(l, c - 1):
            if self._repo.board[l][c - 1] == 1:
                self._repo.randomise_apples(len(self._repo.board[0]), 1)
                self._repo.snake.append(0)
                self._repo.snake.append(0)
            self._repo.change_snake_pos(l, c - 1)
        else:
            raise Exception("Game over!")

    @staticmethod
    def print_menu():
        print("You can: move [n], up|down|right|left ")

    @staticmethod
    def split_command(command):
        """
        Separate user command into command word and parameters
        :param command: User command
        :return: (command word, command parameters=might be returned as None if not found)
        """
        tokens = command.strip().split(' ', 1)
        command_word = tokens[0].lower().strip()
        command_params = tokens[1].strip() if len(tokens) == 2 else 0

        return command_word, command_params

    def start(self):
        self.print_menu()

        command_dict = {"move": self.move, "up": self.up, "down": self.down, "right": self.right, "left": self.left}
        while self.done == 0:
            command = input('command> ')
            command_word, command_params = self.split_command(command)

            if command_word in command_dict:
                try:
                    command_dict[command_word](command_params)
                    self.print_board()
                except Exception as val_error:
                    print(str(val_error))
            elif command_word == 'exit':
                self.done = 1
            else:
                print('No command found')
