from pathlib import Path


class Task():
    def __init__(self, id, name, completed=False):
        '''
        Task model

        :param id: integer

        :param name:str

        :param completed: str
        '''
        self.name = name
        self.completed = completed
        self.id = id
