text = input().split()
for i in text:
    if (i.find("ki") != -1 or i.find("kü") != -1):
        i = i[0:i.find("ki")+2]
        if ((len(i) - 2 != 0) and (i == "sanki" or i == "oysaki" or i == "meğerki" or i == "belki" or i == "halbuki" or i == "çünkü" or i == "mademki" or i == "illaki")):
            print("yazım doğru, özel durum")
        elif ((len(i) - 2 != 0) and (i == "benimki" or i == "seninki" or i == "onunki" or i == "bizimki" or i == "sizinki" or i == "onlarınki")):
            print("yazım doğru, iyelik durumu")
        elif ((len(i) - 2 != 0) and (i == "dünkü" or i == "bugünkü" or i == "yarınki")):
            print("yazım doğru, zaman durumu")
        elif ((len(i) - 2 != 0) and (i[(len(i)-4):(len(i)-2)] == "de" or i[(len(i)-4):(len(i)-2)] == "da")):
            print("yazım doğru") 
        else:
            print("yazım yanlış")
            i = i[0:len(i)-2]
            print("doğru yazımı:", i, "ki")
        
