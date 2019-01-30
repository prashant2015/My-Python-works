#Word Count #
def word_count(val):
    val=val.lower()
    dist={}
    list1=val.split()
    #list1=val.split()
    for x in list1:
        if x in dist:
            dist[x] +=1
        
        else:
            dist[x]=1
            
    return dist 

