from texttable import Texttable
import random


class SnakeGame:
    def __init__(self, DIM, apple_count):
        # displayed as line1, column1, line 2, column 2,...
        self._initial_apple_count = int(apple_count)
        self._snake = []
        self._board = [0] * int(DIM)
        for i in range(int(DIM)):
            self._board[i] = [0] * int(DIM)
        self.display_initial_pos()
        self.display_snake()
        self.randomise_apples(int(DIM), int(apple_count))
        # board. 1 for apples, 2 for snake head, 3 for body


    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, index1, index2, value):
        self._board[index1][index2] = value

    @property
    def snake(self):
        return self._snake

    @snake.setter
    def snake(self, index, value):
        self._snake[index] = value

    def place_apple(self, dim):
        l = random.randint(0, dim - 1)
        c = random.randint(0, dim - 1)
        if self._board[l][c] == 0:
            if c - 1 >= 0 and self._board[l][c - 1] == 1 or c + 1 < dim and self._board[l][
                c + 1] == 1 or l - 1 >= 0 and self._board[l - 1][c] == 1 or l + 1 < dim and self._board[l + 1][
                c] == 1:
                return False
            self._board[l][c] = 1
            return True

    def randomise_apples(self, dim, apple_count):
        """
        This program places apples on the board. Since the snake was already placed
        in its initial position before calling this function, it cannot overlap with its initial position.
        Although it can place an apple on its original position only if the snake has moved!
        :param dim: board dimension
        :param apple_count: nr of apples placed
        :return:
        """
        for i in range(apple_count):
            found = True
            tryout = 0
            while not self.place_apple(dim) and tryout < self._initial_apple_count*2:
                tryout += 1
                found = False
            if not found and tryout == apple_count:
                break

    def display_initial_pos(self):
        c = len(self._board[0]) // 2
        self._snake.append(c - 1)
        self._snake.append(c)
        self._snake.append(c)
        self._snake.append(c)
        self._snake.append(c + 1)
        self._snake.append(c)

    def display_snake(self):
        self._board[self._snake[0]][self._snake[1]] = 2
        for i in range(2, len(self._snake), 2):
            self._board[self._snake[i]][self._snake[i + 1]] = 3

    def change_snake_pos(self, l, c):
        self.clear_snake()
        for i in range(len(self._snake) - 1, 1, -1):
            self._snake[i] = self._snake[i - 2]
            # self._snake[i+1]=
        self._snake[0] = l
        self._snake[1] = c
        self.display_snake()

    def clear_snake(self):
        for i in range(0, len(self._snake), 2):
            self._board[self._snake[i]][self._snake[i + 1]] = 0

    def __str__(self):
        t = Texttable()

        # 1 for apples
        for row in range(0, len(self._board[0])):
            aux = []
            for elem in self._board[row]:
                if elem == 1:
                    aux.append('.')
                elif elem == 2:
                    aux.append("*")
                elif elem == 3:
                    aux.append("+")
                else:
                    aux.append(' ')
            t.add_row(aux)
        return t.draw()
