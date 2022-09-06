class Interface:
    question = ""
    value = ""

    def __init__(self):
        self.question = ""       
        self.value = ""       

    def ask(self, question):
        while True:
            self.value = str(input(question))
            return self.value

    def get_value(self):
        return self.value