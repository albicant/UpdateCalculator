class Calculator:
    total = 0
    pUpdated = 0
    pGoal = 0
    goal = 0

    def __init__(self, fileName=None):
        self.upload_from_file(fileName)

    def upload_from_file(self, fileName):
        try:
            with open(fileName, "r") as file:
                total = file.readline()
                pUpdated = file.readline()
                pGoal = file.readline()
        except:
            return
        self.set_values(total, pUpdated, pGoal)
        self.calculate()

    def calculate(self):
        self.goal = round((self.total * self.pGoal - (self.total * self.pUpdated)) / 100)

    def set_values(self, total, pUpdated, pGoal):
        try:
            self.total = int(total)
        except:
            raise ValueError("Total Records is not a valid number!")
        try:
            self.pUpdated = float(pUpdated)
        except:
            raise ValueError("Percentage Completed is not a valid number!")
        try:
            self.pGoal = float(pGoal)
        except:
            raise ValueError("Percentage Goal is not a valid number!")
        if self.pUpdated < 0 or self.pUpdated > 100:
            raise ValueError("Percentage Completed must be in the range from 0 to 100!")
        if self.pGoal < 0 or self.pGoal > 100:
            raise ValueError("Percentage Goal must be in the range from 0 to 100!")
        if self.pUpdated > self.pGoal:
            raise ValueError("Percentage Completed cannot be greater than Percentage Goal!")

    def save_into_file(self, fileName):
        with open(fileName, "w") as file:
            file.write(str(self.total) + "\n")
            file.write(str(self.pUpdated) + "\n")
            file.write(str(self.pGoal) + "\n")