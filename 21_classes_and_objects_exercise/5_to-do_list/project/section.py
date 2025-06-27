class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'


    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task.name}'

        return f'Could not find task with the name {task_name}'


    def clean_section(self):
        current_task = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f'Cleared {current_task - len(self.tasks)} tasks.'


    def view_section(self):
        details = "\n".join(task.details() for task in self.tasks)
        return f'Section {self.name}:\n{details}'