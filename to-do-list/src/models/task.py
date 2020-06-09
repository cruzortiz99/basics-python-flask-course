from pathlib import Path


class Task():
    def __init__(self, id, name, completed=False):
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
