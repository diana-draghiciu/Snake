from Game import SnakeGame
from GameLoop import GameLoop
from Settings import Settings

if __name__ == '__main__':

    settings = Settings("settings.properties")
    sg=SnakeGame(settings.dim,settings.count)
    print(str(sg))
    g=GameLoop(sg)
    g.start()