import sys
sys.stdin=open("notlast.in","r")
sys.stdout=open("notlast.out","w")
if __name__=="__main__":
    cow_names="Bessie,Elsie,Daisy,Gertie,Annabelle,Maggie,Henrietta"
    cow_names=list(cow_names.split(','))
    milk_dict=dict()
    milks=set()
    n=int(input())
    
    
    for i in range(0,n):
        inputs=input().split()
        cow_name=inputs[0]
        milk_amount=int(inputs[1])
       
        if cow_name in milk_dict:
            milk_dict[cow_name]+=milk_amount
        else:
            milk_dict[cow_name]=milk_amount

    for cow_name in cow_names:
        if cow_name not in milk_dict:
            milk_dict[cow_name]=0

    for cow_name,milk_amount in milk_dict.items():
        milks.add(milk_amount)

    milks=list(milks)
    milks.sort()
    if len(milks)==1:
        print("Tie")

    else:
        name=""
        for cow_name,milk_amount in milk_dict.items():
            if milk_amount==milks[1] and name=="":
                name=cow_name
            elif milk_amount==milks[1] and name!="":
                name="Tie"
                break
        print(name)

