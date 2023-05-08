def biggie_size(list):
    
    for x in range(len(list)):
        if list[x]>0:
            list[x]="big"
    return list
print(biggie_size([-1,3,5,-5]))    

def  count_positives(list):
    count=0
    for x in range(len(list)):
        
        if list[x]>0:
            count+=1
    list[len(list)-1]=count
    return list
print(count_positives([1,6,-4,-2,-7,-2]))   

def sum_total(list):
    sum=0
    for x in range  (len(list)):
        sum+=list[x] 
    return sum
print(sum_total([1,2,3,4]))      
def average(list):
    sum=0
    avg =0
    for x in range  (len(list)):
        sum+=list[x] 
        avg=sum/len(list)

    return avg
print(average([1,2,3,4]))

def length(list):
    return len(list)
print (length([1,2,5]))
def minimum (list):
    min=list[0]
    if len(list)==0:
     return False
    else :
        for x in range( len(list)):
            if list[x]<min:
             min=list[x]
    return min
print (minimum([37,2,1,-9]))
def maximum (list):
    max=list[0]
    if len(list)==0:
     return False
    else :
        for x in range( len(list)):
            if list[x]>max:
             max=list[x]
    return max
print (maximum([37,2,1,-9]))
def ultimate_analysis(list):
   sum=sum_total(list)
   avg=average(list)
   min=minimum(list)
   max=maximum(list)
   len=length(list)
   dec={
      'sumTotal':sum,
      'avarage':avg,
      'minimum':min,
      'maximum':max,
      'length':len
   }
   return dec
print(ultimate_analysis([37,2,1,-9]))

def reverse_list (list):
   length=len(list)
   for x in range (int(length/2)):
      temp=list[length-1-x]
      list[length-1-x]=list[x]
      list[x]=temp
   return list   
print(reverse_list([4,20,5,7]))





