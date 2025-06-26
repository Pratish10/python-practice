from typing import List


class Game:
    def __init__(self, game_id: str, white_player_name: str, black_player_name: str):
        self.id = game_id
        self.white_player_name = white_player_name
        self.black_player_name = black_player_name
        self.moves: List[str] = []


class GameManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(GameManager, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.games: List[Game] = []
        self.__initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def add_game(self, game_id: str):
        game = Game(
            game_id=game_id, white_player_name="alice", black_player_name="john"
        )
        self.games.append(game)

    def add_move(self, game_id: str, move: str):
        game = next((g for g in self.games if g.id == game_id), None)
        if game:
            game.moves.append(move)


gm = GameManager.get_instance()
gm.add_game("game123")
gm.add_move("game123", "e4")

gm2 = GameManager.get_instance()
print(gm2.games[0].moves)
