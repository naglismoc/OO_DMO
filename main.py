# from library.Book import Book
#
# knyga = {
#     "pavadinimas": "grybų karas ir taika",
#     "autorius": "Juozapas Erlickas",
#     "puslapiai": 176,
#     "išleidimo_metai": 1995
# }
#
# print(knyga)
# print(knyga['pavadinimas'])
#
# book = Book(5, "bumbliauskas", 256, 2012, 14)
#
# print(book)
#
# book.Author = "Tapinas"
# print(book)
#
# book2 = Book()
# book2.Author = "autorius"
# book2.Title = "knygos pavadinimas"
# book2.Pages = 641
# book2.RelesaseYear = 1986
# book2.Price = 12
# print(book2)
#
# book3 = Book(author="Škėma")
# print(book3)
#
# print(book.pagePrice())
# print(book2.pagePrice())
# print(book3.pagePrice())
#
# print(book.prettify())
# print(book2.prettify())
# print(book3.prettify())


'''
Sukurti klasę Student
vardas (suformatuojame iki teisingo užrašymo)
pavardė (suformatuojame iki teisingo užrašymo)
gimimo data date
studies dictionary{
           "subject": pvz ekoligija
           "disciplines:[
                {"matematika": [8,7,9]},
                { "geografija": [7,5,6,10,8,9,9]}
            ]

sukurti metodą get_age() kuris gražintų tikslų, gražiai suformatuotą amžių su metais, mėnesiais ir dienomis
sukurti metodą, kuris padavus disciplinos pavadinimą gražintų jos pažymių vidurkį
sukurti metodą, kuris paskaičiuotų visų disciplinų(int) vidurkių vidurkį(double). galima kurtis pagalbines funkcijas.
parašyti __str__ kuris gražiai atspausdintų visą išsamią, gražiai suformatuotą studento informaciją

Vėliau studentą išskaidysime į kelias klases.
'''
import datetime

from library.Book import Book
from university.Discipline import Discipline
from university.Student import Student
from university.Study import Study

adomo_matieka = Discipline()
adomo_matieka.Title = "Matematika"
adomo_matieka.Grades = [10, 9, 8, 10, 3, 8, 10, 9]

print(adomo_matieka.avg())

adomo_lytu = Discipline()
adomo_lytu.Title = "Lietuvių kalba"
adomo_lytu.Grades = [10, 9, 8, 10, 8, 8, 8]
print(adomo_lytu.avg())

adomo_fizika = Discipline()
adomo_fizika.Title = "Taikomosios fizikos pagrindai"
adomo_fizika.Grades = [7, 6, 5, 7, 3, 8, 4, 9]
print(adomo_fizika.avg())

study = Study("Taikomoji fizika",  [adomo_matieka, adomo_lytu, adomo_fizika])
# study = Study()
study.Title = "Taikomoji fizika"
study.Disciplines = [adomo_matieka, adomo_lytu, adomo_fizika]

stud = Student()
stud.name = "Adomas"
stud.surname = "Jakubauskas"
stud.birth_date = datetime.date(1990, 10, 20)
stud.studies = study

print(stud.studies.Disciplines['Matematika'])

print(stud.studies.avg())

print(stud)

#
# knyga = Book("kakės makės nuotykiai","nezinomas",20,2012)
# print(knyga.Title)
# print(knyga._Title)
# knyga.Title = "kakė 4"
# print(knyga)
# print(knyga.Title)
