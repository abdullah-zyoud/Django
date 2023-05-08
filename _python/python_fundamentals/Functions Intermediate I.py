import random
def randInt(max=0,min=0):
    if (max==0 and min==0):
        print(round(random.random()*(100-0+1)+0))
    elif (max !=0 ):
        print(round(random.random()*(max-0+1)+0))
    elif (min !=0 ):
        print(round(random.random()*(100-min+1)+min))
    elif (max !=0 and min!=0):
        print(round(random.random() * (max - min + 1) + min))
    

randInt( )
randInt(5)
randInt( min=3)
randInt(5,3)
