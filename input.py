#문제1 '전화번호 받기'
phone = input("전화번호를 입력하세요.")
phone_number = ''.join(phone.split()).replace("-", "").replace(".", "").replace(" ", "")
print(phone_number)

#문제2 '영어 이름 받기'
name = input("영어이름을 입력하세요.")
el_name = name.split(" ")
first_name = el_name[0].capitalize()
last_name = el_name[1].capitalize()
print("first name :", first_name, end="")
print(", last name:", last_name) 