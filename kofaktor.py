a=[[3,5,1,2,4],[8,12,3,4,4],[7,9,11,17,4],[2,36,3,1,4],[1,2,3,4,5]]
toplam=0
determinant=0
deger=0
kontrol=0
def kofaktor(matris,toplam,determinant,deger,kontrol):
    gecici=[]
    deneme=[]
    oldugu=0
    if len(matris)==2 :
        toplam=toplam+((matris[0][0]*matris[1][1])-(matris[0][1]*matris[1][0]))
        return toplam ,deger
    else:
        for i in matris[0]:
            for j in range(len(matris)):
                for k in range(len(matris[0])):
                    if (j!= 0 and k!=oldugu):
                      gecici.append(matris[j][k])
                if(len(gecici)!=0):
                  deneme.append(gecici)
                  print(deneme)
                gecici=[]
            deneme1,deger=kofaktor(deneme,toplam,determinant,deger,kontrol)
            if kontrol!=deger:
                if oldugu%2 == 0:
                    print("girdim")
                    print(i)
                    print(deneme1)
                    deneme1=((i*deneme1)-deneme1)
                    deger+=deneme1
                    print(deger)
                    kontrol=deger
                    determinant=0
                else:
                    deneme1=(-i*(deneme1)-deneme1)
                    deger+=deneme1
                    print(deger)
                    kontrol=deger
                    determinant=0
            else:
                if oldugu%2 == 0:
                    determinant+=(i*deneme1)
                else:
                    determinant+=(-i*deneme1)
            deneme=[]
            oldugu=oldugu+1
        deger = deger +determinant
        print("deger:",deger,"determinant:",determinant )
    return (determinant,deger)
print(kofaktor(a,toplam,determinant,deger,kontrol))
                    
                    
