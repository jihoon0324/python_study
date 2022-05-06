animal ="강아지"
name ="연탄이"
age = 4 
age_add =3
hobby ="산책"
is_adult =age >=3

print("우리집"+ animal+ name+ "나이는" + str(age) +"그리고 곧" +str(age+age_add) + str(not is_adult))
print("우리집", animal, name, "나이는" , str(age) +"그리고 곧" +str(age+age_add) + str(not is_adult))



station = "사당"

print(station,"행 열처 들어온다")

station="신도림"
print(station +"행 열처 들어온다")
#


sentence ="""
나는 소년이고 ,
파이썬은 쉬워요
"""
print(sentence)

python ="Python is Amazing"
print("전부 소문자 :"+ python.lower())
print("전부 대문자 :"+ python.upper())
print(" 특정 지정 위치 대문자인가 true false: "+ str(python[0].isupper()) )
print ("문자열 길이 "+ str(len(python)))
print("특정문자 교환" +python.replace("Python","Java"))


index = python.index("n")

# 문자에서 n 을 찾은다음에 그 위치 숫자로 말한다  하지만 한번 찾으면 다음꺼 는 안찾는다
print( index)
# 처음 n 을 찾고 그다음 n 을 찾기 위해
index =python.index("n" , index+1)

# 원하는 값 없으면 -1
print(python.find("java"))  

# n  몇개 있는가 
print(python.count("n"))

