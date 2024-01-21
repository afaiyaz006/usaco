import sys
from collections import Counter
sys.stdin=open("blocks.in","r")
sys.stdout=open("blocks.out","w")
def calculate_max_freq(upper_word,lower_word):
    counter_1=Counter(upper_word)
    counter_2=Counter(lower_word)
    counter=dict()
    for i in range(ord('a'),ord('z')+1):
        if chr(i) in counter_1 and chr(i) in counter_2:
            counter[chr(i)]=max(counter_1[chr(i)],counter_2[chr(i)])
        elif chr(i) in counter_1:
            counter[chr(i)]=counter_1[chr(i)]
        elif chr(i) in counter_2:
            counter[chr(i)]=counter_2[chr(i)]
        else:
            counter[chr(i)]=0
    return counter


if __name__=='__main__':
    t=int(input())
    word_pairs=[]
    words=[]
    min_val=sys.maxsize
    counter=dict()
    final=dict()
    while t:
        x,y=map(str,input().split())
        word_pairs.append((x,y))
        t-=1

    for i in range(0,len(word_pairs)):
        upper_word=word_pairs[i][0]
        lower_word=word_pairs[i][1]
        counter=dict()
        counter=calculate_max_freq(upper_word,lower_word)
        for j in range(0,len(word_pairs)):
            if i!=j:
                new_counter=calculate_max_freq(word_pairs[j][0],word_pairs[j][1])
                for i in new_counter.keys():
                    if i in counter:
                        counter[i]+=new_counter[i]
        
        res=sum(counter.values())
        if res<min_val:
            min_val=res
            final=counter

    for i in final.values():
        print(i) 

        