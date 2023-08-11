import sys

class Element():
    def __init__(self, name, position, number, small, molar, electron):
        self.name = name
        self.position = position
        self.number = number
        self.small = small
        self.molar = molar
        self.electron = electron

def obter_arquivo():
    mf = open("periodic_table.txt", "r")
    file_line = mf.readlines()

    table = "<table> \n"    
    elementos = []
    
    for line in file_line:
        list = line.split("=")
        if(len(list) > 1):
            row = list[1].split(',')
            small = row[2].split(':')
            position = row[0].split(':')
            molar = row[3].split(':')
            electron = row[4].split(':')
            numero = row[1].split(':')
            elementos.append({"name" : list[0], "position" : position[1], "number": numero[1], "small": small[1], "molar" : molar[1], "electron" : electron[1]})
        
    mf.close()
        
    pos = 0 #colunas
    num = 0 #linhas
    item = 0
    while num < 9 and item < len(elementos):  
        table += "  <tr>\n"  
        while pos < 18:
            if(pos == int(elementos[item]["position"])):
                table += "  <td>\n"
                itemenvio = elementos[item]
                table += obter_rows(itemenvio)
                table += "  </td>\n"
                item +=1
            else:
                table += "  <td></td>\n"
            pos +=1      
        table += "  </tr>\n"
        pos = 0
        num +=1

    
                    
    file_html = open("periodic_table.html", "w")
    file_html.write('''<!DOCTYPE html>
    <html>
    <head>
        <title>Periodic Table</title>
        <style type="text/css">
            h1{
                text-align: center;
            }
            table{
                border-collapse: collapse;
                border-width: 1px;
            }
            td{
                border: solid black;
                padding: 6px
            }
            ul{
                list-style-type: none;
            }
        </style>
    </head> 
    <body>
        <h1>Periodic Table</h1>           
        ''' + table + '''
    </body>
    </html>''')
    
    file_html.close()

def obter_rows(elemento):
    # table = "<p style=\"text-align:center\">" + elemento["number"] + "</p><h1 style=\"text-align:center\">" + elemento["small"] + "</h1><h4 style=\"text-align:center\">" + elemento["name"] +"</h4><p style=\"text-align:center\">" + elemento["molar"] +"</p>" +"</h4><p style=\"text-align:center\">" + elemento["electron"] +"</p>\n"
    table = "<p style=\"text-align:center\">" + elemento["number"] + "</p><h1 style=\"text-align:center\">" + elemento["small"] + "</h1><h4 style=\"text-align:center\">" + elemento["name"] +"</h4>" + "<br> <ul> <li>" + elemento["molar"] + " </li>" + " <li>" + elemento["electron"] + " </li>"
    return table
    
def obter_objeto_linha(line):
    
    list = line.split("=")
    if(len(list) > 1):
        row = list[1].split(',')
        small = row[2].split(':')
        position = row[0].split(':')
        molar = row[3].split(':')
        electron = row[4].split(':')
        numero = row[1].split(':')
        # elemento = Element(list[0], position[1], numero[1], small[1], molar[1], electron[1])
        elemento = {"name" : list[0], "position" : position[1], "number": numero[1], "small": small[1], "molar" : molar[1]}
        return elemento

if __name__ == '__main__':
    obter_arquivo()
