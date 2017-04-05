class Student(Person):
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber
        self.scores=scores
        
    def calculate(self):
        a=sum(self.scores)/len(self.scores)
        if a >= 90:
            return 'O'
        elif 90>a>=80:
            return 'E'
        elif 80>a>=70:
            return 'A'
        elif 70>a>=55:
            return 'P'
        elif 55>a>=40:
            return 'D'
        else:
            return 'T'
