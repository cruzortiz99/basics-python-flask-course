from utils import get_higher_id
from pathlib import Path


class Task():
    id = 0

    def __init__(self, name, completed=False, id=0):
        '''
        Parameters:
        ---

        * id: integer

        * name:str

        * completed: str
        '''
        self.name = name
        self.completed = completed
        self.id = id
        if id == 0:
            Task.id = get_higher_id(
                Path(__file__).parent.joinpath(
                    '..', 'db', 'user.json'))
            self.id = Task.id
