
def checklist (list1):
    count=0
    count1=0
    for i in list1:
        print(i) 
        if i[0] == i[-1]:
            count=count+1
         
        else:
            count1=count1+1
    return(count,count1)
           
        
list1=["abda","asfdsaa","dasd","wasdfasd"]
p,np=checklist(list1)
print("there are ",p,"number of words matching")
print("there are ",np,"number of words not matching")