geheimnis=1245
versuch=-1
zaehler=0
while versuch!=geheimnis:
    versuch=int(input('Raten Sie: '))
    if versuch<geheimnis:
        print('Zahl ist zu klein!')
    if versuch>geheimnis:
        print('Zahl ist zu gross!')
    zaehler=zaehler+1
print("Super, sie es in ", zaehler, "Versuchen geschafft!")