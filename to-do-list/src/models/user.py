class User():
    def __init__(self, name, tasks=[]):
        '''
        User model

        :param name:str

        :param tasks: Task
        '''
        self.name = name
        self.tasks = tasks
