from ciscoconfparse import CiscoConfParse

# Carica la configurazione dello switch
parse = CiscoConfParse("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\3850dmo.txt", syntax='ios')

stringa = ""
ask = True

#Hostname
while ask:
    answ = input("Vuoi modificare l'hostname? [y\\n]: ")
    if answ == "y" or answ =="Y":
        host =  input("Inserisci hostname: ")
        stringa += "hostname " + host + "\n"
        print("Importo interfacce " , end='')
        ask = False
    elif answ == "n" or answ == "N":
        try:
            host = parse.find_blocks('^hostname',False,False)
            for obj in host:
                stringa += obj + "\n"
            ask = False
            print(" \t\t[OK]")
            
        except:
            print(" \t\t[ERROR]: " + TypeError)
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True  

# Importa interfacce
while ask:
    answ = input("Vuoi importare le interfacce? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo interfacce " , end='')
        try:
            interfacce = parse.find_blocks('^interface',False,False)
            stringa += "! INTERFACCE \n"
            for obj in interfacce:
                stringa += obj + "\n"
            ask = False
            interface = True
            print(" \t\t[OK]")
            
        except:
            print(" \t\t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
        interface = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True  

# Importa Vlan
while ask:
    answ = input("Vuoi importare la configurazione delle VLAN? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo vlan " , end='')
        try:
            vlan = parse.find_blocks('^vlan',False,False)
            stringa += "! VLAN \n"
            for obj in vlan:
                stringa += obj + "\n"
            ask = False
            print(" \t\t[OK]")
            
        except:
            print(" \t\t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True  

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
while ask:
    answ = input("Vuoi importare l' NTP? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo NTP " , end='')

        try:
            ntp = parse.find_blocks('^ntp',False,False)
            stringa += "! NTP \n"
            for obj in ntp:
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

#credenziali

#AAA
while ask:
    answ = input("Vuoi importare l' AAA? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo AAA " , end='')

        try:
            aaa = parse.find_blocks('^aaa',False,False)
            stringa += "! AAA \n"
            for obj in aaa:
                stringa += obj + "\n"
            aaa = parse.find_blocks('^radius server',False,False)
            for obj in aaa:
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
    
#line vty
while ask:
    answ = input("Vuoi importare la line? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo line " , end='')

        try:
            line = parse.find_blocks('^line',False,False)
            stringa += "! LINE \n"
            for obj in line:
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

#acl
while ask:
    answ = input("Vuoi importare le ACL? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo ACL " , end='')

        try:
            acl = parse.find_blocks('^access-list',False,False)
            stringa += "! ACL \n"
            for obj in acl:
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

#static
#routing

#SNMP
while ask:
    answ = input("Vuoi importare l' SNMP? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo SNMP " , end='')

        try:
            snmp = parse.find_blocks('^snmp-server',False,False)
            stringa += "! SNMP \n"
            for obj in snmp:
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

#route map
while ask:
    answ = input("Vuoi importare le Route MAP? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo Route MAP " , end='')

        try:
            rmap = parse.find_blocks('^route-map',False,False)
            stringa += "! SNMP \n"
            for obj in rmap:
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

#error disable
while ask:
    answ = input("Vuoi importare le Error Disable? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo ErrDisable" , end='')

        try:
            err = parse.find_blocks('^errdisable',False,False)
            stringa += "! ERRDISABLE \n"
            for obj in err:
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

#dhcp
while ask:
    answ = input("Vuoi importare il DHCP? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Importo DHCP POOL" , end='')

        try:
            dhcp = parse.find_blocks('^ip dhcp',False,False)
            stringa += "! DHCP POOL \n"
            for obj in dhcp:
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

#Rimuovere sporcherie
frase_da_rimuovere = "--More-- "
stringa = stringa.replace(frase_da_rimuovere, "")

#cambiare interfacce e chassis
if interface:
    #cambiare interfacce
    while ask:
        answ = input("Vuoi cambiare il nome delle interfacce ? [y\\n]: ")
        lista = [] 
        lista = ["Ethernet" , "FastEthernet" , "GigabitEthernet" , "TenGigabitEthernet"]

        if answ == "y" or answ =="Y":
            print("--- Valori inseribili --------\n")
            print("[0] Ethernet\n")
            print("[1] Fastethernet\n")
            print("[2] Gigabitethernet\n")
            print("[3] Tengigabitethernet\n\n")
            print("Ricorda di non fare overlap di interfacce!!!")

            old = ""
            new = ""
            old = lista[int(input("Inserisci il nome da sostiture: "))]
            new = lista[int(input("Inserisci il nuovo nome: "))]

            stringa = stringa.replace(old, new)
            print("\n[OK]\n")
            
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
    ask=True     

    #Cambiare chassis
    while ask:
        answ = input("Vuoi cambiare chassis ID? [y\\n]: ")
        if answ == "y" or answ =="Y":
            old = ""
            new = ""
            old = str(input("Inserisci ID da sostiture: "))
            new = str(input("Inserisci il nuovo ID: "))
            stringa = stringa.replace("tEthernet" + old,"tEthernet" + new)
            print("\n[OK]\n")
            
        elif answ == "n" or answ == "N":
            ask = False
        else:
            print("Comando non valido, prego riprovare. \n")
        
        if ask:
            answ = input("Vuoi cambiare un altro chassis ID [y\\n]: ")

            if answ == "n" or answ == "N":
                ask = False
            else:
                print("Comando non valido, prego riprovare. \n")
    ask=True   

#aggiungere default config
while ask:
    answ = input("Vuoi aggiungere il default template? [y\\n]: ")
    if answ == "y" or answ =="Y":
        print("Applicazione template " , end='')

        try:
            lines=""
            with open("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\Template.txt", "r") as f:
                lines=f.readlines()
            
            for line in lines:
                stringa += line
  
            ask = False
            print(" \t[OK]")
            
        except:
            print(" \t[ERROR]: " + TypeError)
    elif answ == "n" or answ == "N":
        ask = False
    else:
        print("Comando non valido, prego riprovare. \n")
ask=True

#stringa2 = stringa2.lstrip("\t")
with open("C:\\Users\\gianlorenzo.moser\\Documents\\Scripts\\python\\New_Conf.txt", "w") as f:
    f.write(stringa)
