from operator import index
from random import *
from string import *

#1
vokaali=["a","u","i","o","e","ü","ä","ö","õ","y"]
konsonanti="qwrtpsdfghklzxcvbnmj"
märgid=punctuation
v=k=m=t=0
tekst=input("Sisesta tekst: ")
print(tekst)
tekst_list=list(tekst)
print(tekst_list)
for element in tekst_list:
    if element.lower() in vokaali:
        v+=1
    elif element.lower() in konsonanti:
        k+=1
    elif element in märgid:
        m+=1
    elif element==" ":
        t+=1
print("Vokaali:",v)
print("Konsonanti:",k)
print("Märgid:",m)
print("Tühikud:",t)
print()

#2
nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi)
print("Sisestatud:",nimed)
nimed.sort()
print("Sorteeritud:",nimed)
print("Vimasena oli lisatud:",nimi)
while True:
    j=str(input("Kas tahate asendada nimi? "))
    if j=="jah":
        nimi=input("Mis nimi on vaja asendada? ")
        indeks=nimed.index(nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[indeks]=uus_nimi
    else:
        break
    nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed)
print(nimed)
vanused=[]
for i in range(5):
    v=int(input("Vanus: "))
    vanused.append(v)
sum_=sum(vanused)
min_=min(vanused)
max_=max(vanused)
kesk=sum_/len(vanused)
print(f"Kesknime on {kesk}\nSuurim on {max_}\nVäiksem on {min_}\nSumma on {sum_}")
print()

#3
while True:
    try:
        N=int(input("Mitu rida loome? "))
        break
    except:
        print("Vale tüüp")
while True:
  S=input("Mis sümbol korrutame? ")
  if S in punctuation:
      break
  else:
      print("Vale sümbol")
for i in range(N):
    print(randint(1,25)*S)
print()

#4
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]   
while True:
    indeks=input("Indeks: ")
    if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0":
        print("Sa elad piirkonnas",Indeksid[int(indeks[0])-1])
        if indeks[0]=="1" or indeks[0]=="2" or indeks[0]=="3":
            print("Оставайтесь дома!")
        else:
            print("MaskidНосите маски!")
        break 
    else:
        print("Sisesta indeks uuesti")
print()

#5
rida=[]
N=randint(2,25)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
n=int(input("Mitu paari vahetada? "))
if len(rida)//2>=n:
    for i in range(n):
        abi=rida[i]
        rida[i]=rida[len(rida)-1-i]
        rida[len(rida)-1-i]=abi
else:
    print("Liiga vähe elemente")
print(rida)
print()

#6
arvud=[1,2,3,4,5,6,122,44,5]
print(arvud)
max_=max(arvud)
indeks=arvud.index(max_)
max_=round(max_/len(arvud))
arvud[indeks]=max_
print(arvud)
print()

#7
arvud=[]
for i in range(5,20):
    N=randint(-15,25)
    arvud.append(N)
print(arvud)
sorted_arvud=sorted(arvud, key=abs, reverse=False)
print(" По возрастанию:",sorted_arvud)
sorted_arvud=sorted(arvud, key=abs, reverse=True)
print(" По убыванию:",sorted_arvud)
print()

#9
while True:
    nimi=str(input("Имя (латиницей): "))
    if nimi.isalpha():
        break
    else:
        print("Введите имя состоящее только из букв")
print("Здравствуй, ", nimi.capitalize())
glasn=0
soglasn=0
glasn_bukv= "AEIOU"
for letter in nimi.upper():
    if letter.isalpha():
        if letter in glasn_bukv:
            glasn+=1
        else:
            soglasn+=1
print("В имени", len(nimi), "букв")
print("Гласных:", glasn)
print("Согласных:", soglasn)
nl=nimi.lower()
bukvy=set(nl)
bukvy_s = sorted(bukvy)
print("буквы имени в алфавитном порядке:", bukvy_s)
print()

12
arvud=[]
for i in range(10):
    N=randint(1,100)
    arvud.append(N)
print(arvud)
min_=min(arvud)
max_=max(arvud)
indeks_max=arvud.index(max_)
indeks_min=arvud.index(min_)
abi=arvud[indeks_max]
arvud[indeks_max]=arvud[indeks_min]
arvud[indeks_min]=abi
print(arvud)