#lineTmp = "D00/00/0000"

fichierDest = open("cpts.qif", "w")

with open("27042024_2244181.qif", "r") as fichierSource:    
    for line in fichierSource:
        if line[0] != "D":
            fichierDest.write(line)
        else:
            listTmp = list(line)
            listTmp[1] = line[4]
            listTmp[2] = line[5]
            listTmp[4] = line[1]
            listTmp[5] = line[2]
            lineTmp = "".join(listTmp)
            fichierDest.write(lineTmp)
#            print(line)
#            print(lineTmp)
fichierDest.close()

# "with" permet de refermer le fichier automatiquement ou en cas de probleme

# Il n'est pas possible de travailler sur un STRING directement, il faut passer par une LIST