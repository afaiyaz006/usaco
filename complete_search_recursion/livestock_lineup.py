import copy
import sys
sys.stdin=open("lineup.in","r")
sys.stdout=open("lineup.out","w")
names=['Bessie','Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
names.sort()
check={names[i]:False for i in range(0,len(names))}
final_result=[]
solution_found=False
def gen(res,name_sets):
    if len(res)==len(names):
        global solution_found        
        final_result.append(copy.deepcopy(res))
        solution_found=True
    elif not solution_found:
        for i in range(len(names)):
            flag=False
            if check[names[i]]==False:
                if len(res)==0:
                    flag=True
                elif len(res)>=1:
                    if names[i] not in name_sets:
                            flag=True
                
                    elif names[i] in name_sets:
                        
                        if res[::-1][0] in name_sets[names[i]] and len(name_sets[names[i]])==1:
                            flag=True
                        elif len(name_sets[names[i]])==1:
                            if check[name_sets[names[i]][0]]==False:
                                flag=True
                        elif len(name_sets[names[i]])==2:
                            if (check[name_sets[names[i]][0]]==True and check[name_sets[names[i]][1]]==False) or (check[name_sets[names[i]][0]]==False and check[name_sets[names[i]][1]]==True):
                                if res[-1] in name_sets[names[i]]:
                                    flag=True
            if flag:
                check[names[i]]=True
                res.append(names[i])
                gen(res,name_sets)
                check[names[i]]=False
                res.pop()
                    


if __name__=='__main__':
    n=int(input())
    texts=[input() for i in range(n)]
    name_sets=dict(list())
    for text in texts:
        words=text.split(' ')
        name_pair=[]
        for name in names:
            if name in words:
                name_pair.append(name)
        if name_pair[1] not in name_sets:
            name_sets[name_pair[1]]=[]
        if name_pair[0] not in name_sets:
            name_sets[name_pair[0]]=[]
        name_sets[name_pair[1]].append(name_pair[0])
        name_sets[name_pair[0]].append(name_pair[1])
    
    res=[]
    total=[]
    gen(res,name_sets)
    print("\n".join(final_result[0]))