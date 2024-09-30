#1. 평균 점수 구하기
#Scores
scores = {
    "국어": 80,
    "영어": 75,
    "수학": 55
}
#Average
average_scores = sum(scores.values()) / len(scores)
print (f"평균 점수는 {average_scores} 입니다\n")

#2. 홀수, 짝수 판별하기
number = 13
if number%2 == 1:
    print (f"{number}은/는 홀수 입니다\n")
else:
    print (f"{number}은/는 짝수 입니다\n")

#3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(f"주민등록번호의 생년월일은 {yyyymmdd} 입니다\n")
print(f"주민등록번호의 고유번호는 {num} 입니다\n")

#4. 주민등록번호 인덱싱
pin = "881120-1068234"
print(f"주민등록번호의 성별을 나타내는 숫자는 {pin[7]} 입니다 \n")

#5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "%")
print(f"다음은 {a}의 문자열을 중 : 를 % 로 바꾼 {b}입니다\n")

#6. 리스트 역순 정렬하기
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7. 리스트를 문자열로 만들기
a = ['Life','is','too','short']
result = " ".join(a)
print(result)

#8. 튜플 더하기
a = (1,2,3)
a = a + (4,)
print(a)

#9. 딕셔너리의 키
a = dict()
a['name'] = 'python'
a[('a,')] = 'python'
a[[1]] = 'python'
a[250] = 'python'
print("a[[1]]='python'의 경우, unhashable type:list 발생. 문자열, 튜플, 정수와 같은 불변자료형은 key가 될 수 있음. 불변자료형은 해시값을 가질 수 있음. 즉, hashable하다고 말할 수 있음. 리스트는 가변자료형으로 해시값을 가질 수 없음. 이에 unhashable type이라고 뜸")

#10. 딕셔너리 값 추출하기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11. 리스트에서 중복 제거하기
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
aList = aSet
print(aList)

#12. 파이썬 변수
a = b = [1,2,3]
a[1] = 4
print(b)
print("동일한 값에 여러 변수 선언 가능하므로 b의 요소도 바뀐다")