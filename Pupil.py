class Pupil:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self.marks = {}

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name should be at least 3 letters long")
        self.name = value

    @property
    def surname(self):
        return self.surname
    
    @surname.setter
    def surname(self, value):
        if len(value) < 3:
            raise ValueError("Surname should be at least 3 letters long")
        self.surname = value

    def complete_marks(self, subjects: list, grades: list) -> None:
        if not isinstance(subjects, list):
            subjects = [subjects]

        if not isinstance(grades, list):
            grades = [float(grades)]
        
        for id, grade in enumerate(grades):
            grades[id] = float(grade)

        if len(grades) == len(subjects):
            for idx, subject in enumerate(subjects):
                if grades[idx] not in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]:
                    raise ValueError
                self.marks[subject] = grades[idx]
        else:
            raise IndexError("Both lists must be of the same length. Check your code.")

    def print_marks(self) -> None:
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print("\n")

    def mean(self) -> float or None:
        if len(self.marks) == 0:
            return None
        return sum(self.marks.values()) / len(self.marks)
    
    def __str__(self) -> str:
        return f"{self._name} {self._surname}: {self.mean()}"
    
class Student(Pupil):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.weights = {}

    def complete_weights(self, subjects: list, weights: list, marks: list) -> None:
        
        self.complete_marks(subjects, marks)

        if not isinstance(weights, list):
            weights = [weights]
        
        if len(weights) == len(marks):
            for idx, subject in enumerate(subjects):
                self.weights[subject] = weights[idx]
        else:
            raise IndexError("All lists must be of the same size")
    
    def mean(self):
        total_weighted_marks = 0
        total_weight = 0
        for subject, mark in self.marks.items():
            weight = self.weights[subject]
            total_weighted_marks += mark * weight
            total_weight += weight
        return total_weighted_marks / total_weight

    def __str__(self):
        return f"{self._name} {self._surname}, average grade: {self.mean():.2f}"
    
if __name__ == "__main__":
    pupil = Pupil("Marcelina", "Łukowska")
    student = Student("Maria", "Konieczna")
    pupil.complete_marks(["Matematyka", "Fizyka", "Polski", "Angielski"], [2.5, 3, 4, 4.5])
    student.complete_weights(["Matematyka", "Fizyka", "Polski", "Angielski"], [1.75, 2.5, 1.5, 0.5], [2.5, 3, 4, 4.5])
    pupil.print_marks()
    student.print_marks()

    print(pupil)
    print(student)

