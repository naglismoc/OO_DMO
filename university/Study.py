class Study():
    def __init__(self,title = "", disciplines = []):
        self.Title = title
        self._Disciplines = self.listToDict(disciplines) #su apatiniu brūkšniu, tipo inkapsuliuota :))

    @property # sukuriamas propertis, leidzia paimti reiksme
    def Disciplines(self):
        return self._Disciplines

    @Disciplines.setter #kadangi yra propertis, galime ir settinti reiksmes, kazkaip jas apsitvarke, ar atlike X
    # veiksmus
    def Disciplines(self,disciplines):
        self._Disciplines = self.listToDict(disciplines)

    def listToDict(self, disciplines): #paprastas metodukas, objektų listą paverčiantis į objektų dictionary
        dict = {}
        for dis in disciplines:
            dict[dis.Title] = dis
        return dict

    def avg(self): #medotas kuris susumuoja study klasės objektų vidurkius ir išveda bendrą vidurkį
        sumGrades = 0
        for dis in self.Disciplines.values():
            sumGrades += dis.avg()
        return  sumGrades / len(self.Disciplines)

    def __str__(self): #toString metodas, skirtas apspręsti, kaip bus atvaizduojamas objektas kai jį bandysime
        # spausdinti
        toStr = f'{self.Title}: \n['
        for dis in self.Disciplines.values():
            toStr += f"\n {dis}"
        toStr += " \n] \n"
        return toStr