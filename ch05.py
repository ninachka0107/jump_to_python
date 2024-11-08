#1. 자식 클래스 만들고 메서드 추가하기
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 2. 클래스 상속받고 메서드 추가하기2
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        super().add(val)
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)


# 3. 참과 거짓 예측하기
a = all([1,2,abs(-3)-3])
print(a)

b = chr(ord('a'))=='a'
print(b)

# 4. 음수 제거하기
c = [1, -2, 3, -5, 8, -3]
pos_num = filter(lambda x: x > 0, c)
print(list(pos_num))

# 5. 16진수를 10진수로 변경하기
십진수 = int(hex(234), 16)
print(십진수)

# 6. 리스트 항목마다 3 곱하여 리턴하기
d = [1, 2, 3, 4]
mul_by_3 = map(lambda x: x *3, d)
print(list(mul_by_3))

# 7. 최댓값과 최솟값의 합
e = [-8, 2, 7, 5, -3, 5, 0, 1]
sum = max(e) + min(e)
print(max(e))
print(min(e))
print(sum)

# 8. 소수점 반올림하기
f = round(17/3,4)
print(f)

# 9. 디렉터리 이동하고 파일목록 출력하기
import os

current_directory = os.getcwd()
print(current_directory)
# /Users/mzc01-nkoe/Desktop/python_study

dir_cont = dir()
print(dir_cont)
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'current_directory', 'os']

# 10. 파일 확장자가 .py인 파일만 찾기
import os

current_directory = os.getcwd()
print(current_directory)


import glob

files = glob.glob('*.py')
print(files)
# ['ch02.py', 'ch03.py', 'mod1.py', 'mod2.py', 'ch04.py', 'modtest.py', 'ch05.py']


# 현재 및 하위 디렉터리까지 확장자가 .py인 파일 찾기
all_files = glob.glob('**/*.py', recursive=True)
print(all_files)
#['ch02.py', 'ch03.py', 'mod1.py', 'mod2.py', 'ch04.py', 'modtest.py', 'ch05.py', 'game/__init__.py', 'game/graphic/render.py', 'game/graphic/__init__.py', 'game/sound/__init__.py', 'game/sound/echo.py']


# 11. 날짜 표시하기
import time

g = time.strftime("%Y/%m/%d %H:%M:%S")
print(g)


# 12. 로또 번호 생성하기
import random

lotto_num = random.sample(range(1,46), 6)
print(lotto_num)


# 복수선택 허용
selected_num = random.choices(range(1,46), k=6)
print(selected_num)


# 13. 누나는 수원이보다 며칠 더 먼저 태어났을까? 누나는 1990년 2월 11일이고, 수원이의 생일은 1992년 6월 13일이다. 수원이 누나는 수원이보다 며칠 더 먼저 태어났을까?
from datetime import date

nicole_day = date(1990,2,11)
soowon_day= date(1992,6,13)

date_difference = soowon_day - nicole_day

print("수원이 누나는 수원이보다", date_difference.days,"일 더 먼저 태어남")


# 14. 기록순으로 정렬하기 PASS


# 15. 교육가는 2명 뽑기. 다음 5명 중 2명을 뽑는 경우의 수를 모두 나열하시오
from itertools import combinations

candidates = ['회창','민수','민지','희영','유진']
combinations_of_candidates = list(combinations(candidates, 2))

for combo in combinations_of_candidates:
    print(combo)

# 16. 문자열 나열하기
from itertools import permutations

word = "abcd"
permutations_list = permutations(word)

# list내 element가 된 알파벳 다시 붙이기
for perm in permutations_list:
    print(''.join(perm))


# 17. 5명에게 할 일 부여하기
import random

candidates = ['회창','민수','민지','희영','유진']
tasks = ['티켓대응','넷마블미팅참석','이벤트참석']

random.shuffle(candidates)

assignments = {}
for i in range(3):
    assignments[candidates[i]]=tasks[i]

for i in range(3,5):
    assignments[candidates[i]]="대휴"

for candi, task in assignments.items():
    print(f"{candi}:{task}")

#  18. 벽에 타일 붙이기. 가로 길이 200, 세로 길이 80. 되도록 큰 정사각형 모양의 타일... PASS