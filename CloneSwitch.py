from ciscoconfparse import CiscoConfParse

# Carica la configurazione dello switch
parse = CiscoConfParse("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\3850dmo.txt", syntax='ios')

stringa = ""
ask = True
# Importa interfacce
interface = parse.find_blocks('^interface',False,False)
print("Importo interface ", end='')
try: 
    stringa += "! INTERFACCE \n"
    for obj in interface:
        stringa += obj + "\n"

    print(" \t[OK]")
except:
    print(" \t[ERROR]: " + TypeError)

# Importa Vlan
print("Importo vlan " , end='')

try:
    vlan = parse.find_blocks('^vlan',False,False)
    stringa += "! VLAN \n"
    for obj in vlan:
        stringa += obj + "\n"

    print(" \t\t[OK]")
except:
    print(" \t\t[ERROR]: " + TypeError)

#spanningtree
while ask:
    answ = input("Vuoi importare la configurazione di spanning tree? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo spanning tree " , end='')

        try:
            stp = parse.find_blocks('^spanning-tree',False,False)
            stringa += "! SPANNINGTREE \n"
            for obj in stp:
                stringa += obj + "\n"
            ask = False
            print(" \t[OK]")
            
        except:
            print(" \t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True           
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

#NTP
print("Importo NTP " , end='')

try:
    ntp = parse.find_blocks('^ntp',False,False)
    stringa += "! NTP \n"
    for obj in ntp:
        stringa += obj + "\n"

    print(" \t\t[OK]")
except:
    print(" \t\t[ERROR]: " + TypeError)

#credenziali
#AAA
print("Importo AAA " , end='')

try:
    aaa = parse.find_blocks('^aaa',False,False)
    stringa += "! AAA \n"
    for obj in aaa:
        stringa += obj + "\n"

    aaa = parse.find_blocks('^radius server',False,False)
    for obj in aaa:
        stringa += obj + "\n"

    print(" \t\t[OK]")
except:
    print(" \t\t[ERROR]: " + TypeError)
    
#console
#acl
print("Importo ACL " , end='')

try:
    acl = parse.find_blocks('^access-list',False,False)
    stringa += "! ACL \n"
    for obj in acl:
        stringa += obj + "\n"
    
    print(" \t\t[OK]")
except:
    print(" \t\t[ERROR]: " + TypeError)

#static
#routing

#SNMP
print("Importo SNMP " , end='')

try:
    snmp = parse.find_blocks('^snmp-server',False,False)
    stringa += "! SNMP \n"
    for obj in snmp:
        stringa += obj + "\n"

    print(" \t\t[OK]")
except:
    print(" \t\t[ERROR]: " + TypeError)
#route map
print("Importo Route MAP " , end='')

try:
    rmap = parse.find_blocks('^route-map',False,False)
    stringa += "! ROUTE MAP \n"
    for obj in rmap:
        stringa += obj + "\n"

    print(" \t[OK]")
except:
    print(" \t[ERROR]: " + TypeError)

#error disable
print("Importo ErrDisable " , end='')

try:
    err = parse.find_blocks('^errdisable',False,False)
    stringa += "! ERRDISABLE \n"
    for obj in err:
        stringa += obj + "\n"

    print(" \t[OK]")
except:
    print(" \t[ERROR]: " + TypeError)


#dhcp
print("Importo DHCP POOL " , end='')

try:
    dhcp = parse.find_blocks('^ip dhcp',False,False)
    stringa += "! DHCP POOL \n"
    for obj in dhcp:
        stringa += obj + "\n"

    print(" \t[OK]")
except:
    print(" \t[ERROR]: " + TypeError)


#dns
while ask:
    answ = input("Vuoi importare i DNS? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo DNS " , end='')

        try:
            dns = parse.find_blocks('^ip name-server',False,False)
            stringa += "! DNS \n"
            for obj in dns:
                stringa += obj + "\n"
            ask = False
            print(" \t[OK]")
            
        except:
            print(" \t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True 

#dominio
while ask:
    answ = input("Vuoi importare il dominio? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo Dominio " , end='')

        try:
            dom = parse.find_lines('^ip domain-name',False,False)
            dom += parse.find_lines('^ip domain-lookup',False,False)
            stringa += "! DOMINIO \n"
            for obj in dom:
                stringa += obj + "\n"
            ask = False
            print(" \t[OK]")
            
        except:
            print(" \t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True 

#Hostname
temp =  input("Inserisci hostname: ")
stringa += "hostname " + temp + "\n"

#Rimuovere sporcherie
frase_da_rimuovere = "--More-- "
stringa = stringa.replace(frase_da_rimuovere, "")

#cambiare interfacce
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
with open("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\New_Conf.txt", "w") as f:
    f.write(stringa)
