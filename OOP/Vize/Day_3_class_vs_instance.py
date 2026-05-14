class School:
    total_student = 0
    passing_grade = 50

    def __init__(self, name,notes ):
        self.name = name
        self.notes = notes

        School.total_student += 1
        print(f"Added new Student : {self.name}")

    def check_notes(self):
        if self.notes >= School.passing_grade:
            print(f"{self.name} is successful. Notes : {self.notes}")
        else:
            print(f"{self.name} is unsuccessful. Notes : {self.notes}")

    @classmethod
    def total(cls):  # Don't forget to run the function -- Exm: School.total()d
        print(f"Total Students: {cls.total_student}")


S1 = School("Sefa", 58)
S2 = School("Ömer", 38)

School.total()

School.check_notes(S1)
School.check_notes(S2)



