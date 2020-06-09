class User():
    def __init__(self, name, tasks=[]):
        '''
        Parameters:
        ---
        * name:str

        * tasks: Task
        '''
        self.name = name
        self.tasks = tasks
