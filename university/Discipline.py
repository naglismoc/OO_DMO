class Discipline():
    def __init__(self,title = "",grades = []):
        self.Title = title,
        self.Grades = grades

    def __str__(self):
        return f'{self.Title} {self.Grades}'

    def avg(self):
        # return  sum(self.Grades)/len(self.Grades)
        return round(sum(self.Grades)/len(self.Grades))
