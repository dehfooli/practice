# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Film import Film
from Actor import Actor
import json
import xlrd

workbook = xlrd.open_workbook('file.xlsx')
worksheet = workbook.sheet_by_index(0)
worksheet_actors = workbook.sheet_by_index(1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    worksheet = workbook.sheet_by_index(0)
    first_row = []  # The row where we stock the name of the column
    first_row_2 = []  # The row where we stock the name of the column
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0, col))
    for col in range(worksheet_actors.ncols):
        first_row_2.append(worksheet_actors.cell_value(0, col))
    data = []
    data2 = []
    films={}
    actors={}
    i = 0
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols):
            elm[first_row[col]] = worksheet.cell_value(row, col)

        films[i] = Film(elm['type'], elm["name"], elm["director"], elm["imdb_score"], elm["url"], elm["duration"], elm["casts"])
        data.append(elm)
        i = i +1
    j=0
    for row in range(1, worksheet_actors.nrows):
        elm = {}
        for col in range(worksheet_actors.ncols):
            elm[first_row_2[col]] = worksheet_actors.cell_value(row, col)

        actors[i] = Actor(elm['firstname'], elm["lastname"], elm["birthdate"], elm["Gender"])
        data2.append(elm)
        j= j + 1
        i = i +1
    print(data)
    print(films)
    print(actors)
    n1 = int(input('Enter max duration: '))
    n2 = int(input('Enter min duration: '))
    result = []
    for key,val in films.items():
        if n2 <= val.duration <= n1:
            result.append(val)
    for item in result:
        print (item.name)