ad, am, ay = [int(x) for x in raw_input().split(' ')]
ed, em, ey = [int(x) for x in raw_input().split(' ')]


if(ay<ey):
    fine=0
    print(fine)
elif(ay>ey):
    fine=10000
    print (fine)
else:
    if(am<em):
        fine=0
        print (fine)
    elif(am>em):
        fine=500 * (am-em)
        print (fine)
    else:
        if(ad<=ed):
            fine=0
            print (fine)
        else:
            fine=15 * (ad-ed)
            print (fine)
