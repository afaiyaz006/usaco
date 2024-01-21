import random
if __name__=='__main__':
  
    print("1000000 2500")
    
    for i in range(1,2501):
        a=random.randint(2500,1000000)
        b=random.randint(2500,1000000)
        c=[a,b]
        c.sort()
        print(f"{c[0]} {c[1]}")
          
