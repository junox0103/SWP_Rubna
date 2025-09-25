import random





print("Lotto spielen 6 zufallszaheln auf enter (Enter ziehungszahl)")
h=int(input())


l=0;
for l in range(h):

    num = []
    i = 0;

    for i in range(45):
        i = i + 1;
        num.append(i)
    def zufall(x):
        e=0;
        for e in range(x):
            zufallszahl=random.randint(0,44-e)
            temp=num[zufallszahl]
            num[zufallszahl]=num[44-e]
            num[44-e]=temp
            print(num[44-e],end=" ")

            e=e+1;


    zufall(6);
    print("Ende")
    l=l+1;
