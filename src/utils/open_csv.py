import csv 

with open('C:\\Users\\rafael.borsatto\\Projetos\\cypress\\auto_music\\src\\utils\\JIRA.csv', 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        print(linha)