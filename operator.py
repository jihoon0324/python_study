print(1+1)
print(2**3)# 2^3
print(10%3) #나머지 구하기
print(10//3) #몫 구하기 

print (10 >=3) # true false

print (3 == 3) 
print ( 1 != 3) #true
print("비교")
print (not(1 !=3))
print((3>0) and (3<5) )
print((3>0) & (3<5) )


print((3>0) or (3<5) )
print((3>0) | (3<5) )
print(5 >4>3)
print(5>4>7)
# random number
from random import *
print(random()) 
print(int(random())) 

print(int(random() *10) +1)
print(randrange(1,45)) # 1~45 미만의 값 생성 
print (randint(1,45)) # 1-45 이하의 임의의값 생성 


number ="01234-12341"
print("성별:" + number[0])
print("0부터 1 까지:" +number[0:2])  
print("0 부터 5 까지" +number[:6])  
print("6 번째 자리부터 끝까지" +number[6:]) 
print("끝에서 부터  7자리:" +number[-7:]) 
  