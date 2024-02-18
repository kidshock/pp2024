import numpy as np
from .person import Person

class Student(Person):
    def __init__(self, name, id, dob):
        super().__init__(name, id, dob)
    
    def calculate_gpa(self):
        weighted_marks = np.array([mark * credit for (_, mark), credit in zip(self.marks, self.credits)])
        total_credits = np.sum(self.credits)
        return np.sum(weighted_marks) / total_credits if total_credits else 0