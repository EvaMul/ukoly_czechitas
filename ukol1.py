# DOMACI UKOL C.1
print("__________________________")
print("RESENI UKOLU C.1:")
print("__________________________")
#########################################################
# TRIDA ZVIRE
print("ZVIRE")
class Zvire:
    def __init__(self, jmeno:str, druh:str, vaha:int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    def __str__(self):  
        #return f"{self.druh} se jmenuje {self.jmeno} a vazi {self.vaha} kilogramu"
        return f"{self.druh}"
    def export_to_dict(self):
        dict = {}
        dict['jmeno'] = self.jmeno
        dict['druh'] = self.druh
        dict['vaha'] = self.vaha
        return dict

#zkouska, ze export pracuje ok
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1

#vytvorim vlastni zvirata
zvire_panda = Zvire('Růženka', 'Panda Velká', 150)
zvire_vydra = Zvire('Vilda', 'Vydra Mořská', 150)
zvire_tygr = Zvire('Matýsek', 'Tygr Sumaterský', 300)
zvire_medved = Zvire('Karlík', 'Lední medvěd', 700)

#vytvorim z nich seznam a pak seznam jednotlivych slovniku
seznam_objektu_zvirata = []
seznam_zvirat = [zvire_panda, zvire_vydra, zvire_tygr, zvire_medved]
for zvire in seznam_zvirat:
    seznam_objektu_zvirata.append(zvire.export_to_dict())
print(f"Seznam zvirat, ktere jsou slovniky: {seznam_objektu_zvirata}")    

#############################################################
# TRIDA ZAMESTNANEC
print("")
print("ZAMESTNANEC")
class Zamestnanec:
    def __init__(self, jmeno:str, rocni_plat:int, pozice:str):
        self.jmeno = jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    def __str__(self):
        return f"Zamestnanec {self.jmeno} pracuje na pozici {self.pozice} a ma plat {self.rocni_plat}"
# metodu ziskej_inicialy(), která bude vracet výstup ve formátu A.W., uvažuj pouze změstnance se dvěma jmény.
    def ziskej_inicialy(self):
        list_jmeno = self.jmeno.split(' ')
        if len(list_jmeno) == 2:
            inicialy =  f"{list_jmeno[0][0]}.{list_jmeno[1][0]}."
            return inicialy
        else:
            print (f"Zamestnanec {self.jmeno} ma jiny pocet jmen nez 2!!!")
            return "!!!chyba v zadani jmena!!!"
    def export_to_dict(self):
        dict = {}
        dict['jmeno'] = self.jmeno
        dict['rocni_plat'] = self.rocni_plat
        dict['pozice'] = self.pozice
        return dict

#vytvorim jednotlive zamestnance
zamestnanec1 = Zamestnanec('Tereza', 700_000, 'Cvičitelka tygrů')
zamestnanec2 = Zamestnanec('Anet Krasna', 600_000, 'Cvičitelka vyder')
zamestnanec3 = Zamestnanec('Martin Veliky', 650_000, 'Cvičitel ledních medvědů')
#vytisknu inicialy
print(f"Zamestnanec {zamestnanec1.jmeno} ma inicialy {zamestnanec1.ziskej_inicialy()}")
print(f"Zamestnanec {zamestnanec2.jmeno} ma inicialy {zamestnanec2.ziskej_inicialy()}")
print(f"Zamestnanec {zamestnanec3.jmeno} ma inicialy {zamestnanec3.ziskej_inicialy()}")

#vytvorim seznam zamestnancu a pak seznam jednotlivych slovniku
seznam_zamestnancu = [zamestnanec1, zamestnanec2, zamestnanec3]
seznam_objektu_zamestnanec = []
for zamestnanec in seznam_zamestnancu:
    seznam_objektu_zamestnanec.append(zamestnanec.export_to_dict())
print(f"Seznam zamestnancu, kteri jsou jako slovniky: {seznam_objektu_zamestnanec}")

################################################################
# TRIDA REDITEL
print("")
print("REDITEL")
class Reditel(Zamestnanec):
    def __init__(self, jmeno, rocni_plat, oblibene_zvire):
        super().__init__(jmeno, rocni_plat, oblibene_zvire)
        self.oblibene_zvire = oblibene_zvire
        self.pozice = 'Reditel'

#vytvorim reditele
zvire = zvire_panda
nas_reditel = Reditel(jmeno='Karel Novy', rocni_plat=800_000, oblibene_zvire=zvire)
# kontrola
assert nas_reditel.pozice == 'Reditel'
assert isinstance(nas_reditel.oblibene_zvire, Zvire)
assert isinstance(nas_reditel, Zamestnanec)

#print(nas_reditel.export_to_dict())
print(f"Oblibene zvire reditele je {nas_reditel.oblibene_zvire}")
print(f"Reditel {nas_reditel.jmeno} ma inicialy {nas_reditel.ziskej_inicialy()}")

##################################################################
# TRIDA ZOO
print("")
print("ZOO")
class Zoo:
    def __init__(self, jmeno:str, adresa:str, reditel, zamestnanci:list, zvirata:list):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata
    def vaha_vsech_zvirat_v_zoo(self):
        vaha = 0
        for zvire in self.zvirata:
            vaha = vaha + zvire.vaha
        return vaha   
    def mesicni_naklady_na_zamestnance(self):
        naklady = 0
        for zamestn in self.zamestnanci:
            naklady = naklady + zamestn.rocni_plat
        naklady = naklady + self.reditel.rocni_plat
        return naklady  

#vytvorim zoo
nase_zoo = Zoo("Zoo Brno", "Brno-Bystrc", nas_reditel, seznam_zamestnancu, seznam_zvirat)

print(f"Reditelem {nase_zoo.jmeno} v {nase_zoo.adresa} je {nase_zoo.reditel.jmeno}")
print('Celková váha zvířat v ZOO v kg:', nase_zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance v Kč:', int(nase_zoo.mesicni_naklady_na_zamestnance()/12))
