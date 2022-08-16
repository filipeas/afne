from utils.readFile import loadAndParse
from afne import AFNe

loaded_file = loadAndParse('languages/afn-e.yml')
automato = AFNe(**loaded_file['M'])

print("------------------------------")
print("Automato informado:")
print(automato)
print("------------------------------")

while True:
    word = input("Informe uma palavra: ")
    print("Palavra aceita: ", automato.accepts(word), "\n")
    if input("Deseja converter o automato para um AFN? (N/s)").lower().strip() in ["s", "sim"]:
        automato.convert()
    if input("Deseja testar outra palavra? (S/n)").lower().strip() in ["n", "nao"]:
        break
    print()