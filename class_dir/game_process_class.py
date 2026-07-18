import weakref
from .screen import GameFrame

class GameNode:
    def __init__(self, game_frame: GameFrame):
        self.game_frame = game_frame
        self._front_node: GameNode | None = None
        self.next_node_dict = {}

    def add_node(self, game_node: 'GameNode', key: str) -> None:
        self.next_node_dict[key] = game_node
        game_node._front_node = weakref.ref(self)

    def get_next_node(self, key: str) -> 'GameNode' | None:
        if key in self.next_node_dict:
            return self.next_node_dict[key]
        return None
    
    @property
    def front_node(self) -> 'GameNode' | None:
        if self._front_node is not None:
            return self._front_node()
        return None

class GameProcess:
    def __init__(self, game_id: int, game_name: str, first_node: GameNode | None = None) -> None:
        self.game_id = game_id
        self.game_name = game_name
        self.first_node: GameNode | None = first_node
        self.current_node: GameNode | None = first_node


class GameProcessList:
    list = []

    def append(self, game_process: 'GameProcess') -> None:
        self.list.append(game_process)

    def get_game_process_by_id(self, game_id: int) -> 'GameProcess':
        for game_process in self.list:
            if game_process.game_id == game_id:
                return game_process
        return None
    
    def get_game_process_by_name(self, game_name: str) -> 'GameProcess':
        for game_process in self.list:
            if game_process.game_name == game_name:
                return game_process
        return None