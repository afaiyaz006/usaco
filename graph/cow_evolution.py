if __name__=='__main__':
    t=int(input())
    res="yes"
    pops=[]
    chars=set()
    while t:
        data=list(map(str,input().split()))
        k=data[0]
        sub_pop=data[1:]
        pops.append(sub_pop)
        counter={}
        
        for node in sub_pop:
            chars.add(node)
            if node not in counter:
                counter[node]=0
            counter[node]+=1
            
            if counter[node]>1:
                res='no'
        t-=1
    if res=='no':
        print(res)
    else:
        chars=list(chars)
       
        for i in range(0,len(chars)):
            
            for j in range(i+1,len(chars)):
                trait_1=chars[i]
                trait_2=chars[j]
                
                has_t1,has_t2,has_both=0,0,0
     
                for sub_pop in pops:
                    if trait_1 in sub_pop and trait_2 not in sub_pop:
                        has_t1=1
                    elif trait_2 in sub_pop and trait_1 not in sub_pop:
                        has_t2=1
                    if trait_1 in sub_pop and trait_2 in sub_pop:
                        has_both=1
                if has_t1 and has_t2 and has_both:
                    res='no'
                    break
            if res=='no':
                break
        print(res)   

    