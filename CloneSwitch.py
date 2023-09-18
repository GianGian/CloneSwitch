from ciscoconfparse import CiscoConfParse

# Carica la configurazione dello switch
parse = CiscoConfParse("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\3850dmo.txt", syntax='ios')

stringa = ""
# Importa interfacce
interface = parse.find_blocks('^interface',False,False)
print("Importo interface ", end='')
try: 
    stringa += "! INTERFACCE \n"
    for obj in interface:
        stringa += obj + "\n"

    print(" [OK]")
except:
    print(" [ERROR]: " + TypeError)

# Importa Vlan
print("Importo vlan " , end='')

try:
    vlan = parse.find_blocks('^vlan',False,False)
    stringa += "! VLAN \n"
    for obj in vlan:
        stringa += obj + "\n"

    print(" [OK]")
except:
    print(" [ERROR]: " + TypeError)

#spanningtree
print("Importo spanning tree " , end='')

try:
    stp = parse.find_blocks('^spanning-tree',False,False)
    stringa += "! SPANNINGTREE \n"
    for obj in stp:
        stringa += obj + "\n"

    print(" [OK]")
except:
    print(" [ERROR]: " + TypeError)

#vtp
#print("Importo vtp config" , end='')
#try:
#    vtp = parse.find_lines ('^vtp mode',False,False)
#    if vtp != "vtp mode transparent":
#        vtp = parse.find_blocks('^vtp',False,False)
#        stringa += "! VTP \n"
#        for obj in vtp:
#            stringa += obj + "\n"

#    print(" [OK]")
#except:
#    print(" [ERROR]: " + TypeError)


#Hostname
temp =  input("Inserisci hostname: ")
stringa += "hostname " + temp + "\n"

#Rimuovere sporcherie
frase_da_rimuovere = "--More-- "
stringa = stringa.replace(frase_da_rimuovere, "")

#cambiare interfacce
ask = True
old = ""
new = ""

while ask:
    answ = input("Vuoi cambiare il nome delle interfacce ? [y\\n]: ")
    lista = [] 
    lista = ["Ethernet" , "FastEthernet" , "GigabitEthernet" , "TenGigabitEthernet"]

    if answ == "y" or answ =="Y":
        print("--- Valori inseribili --------\n")
        print("[0] erthernet\n")
        print("[1] fastethernet\n")
        print("[2] Gigabitethernet\n")
        print("[3] Tengigabitethernet\n\n")

        old = lista[int(input("Inserisci il nome da da sostiture: "))]


        new = lista[int(input("Inserisci il nuovo nome: "))]

        stringa = stringa.replace(old, new)
        print("\nFATTO :)\n")
        
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
    
    if ask:
        answ = input("Vuoi cambiare il nome ad altre interfacce [y\\n]: ")

        if answ == "n" or answ == "N":
            ask = False
        else:
            print("Comando non valido, prego riprovare. \n")
        
#aggiungere default config
lines=""
with open("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\Template.txt", "r") as f:
    lines=f.readlines()

for line in lines:
    stringa += line

#stringa2 = stringa2.lstrip("\t")
with open("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\switch_config_parsed.txt", "w") as f:
    f.write(stringa)
