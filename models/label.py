class Label:
    def __init__(self, name, description, id = None):
        self.name = name
        self.id = id

    def get_name(self):
        return self.label['name']
        