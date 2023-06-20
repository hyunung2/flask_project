# 1.# 유저 닉네임 등록
# - git config user.name "닉네임"
#
# 2. 유저 이메일 등록
# - git config user.email "email"
#
# 3. 내가 이력 저장하고 싶은 대상 폴더를 정하기.
# - work1 폴더가 있는 경로로 이동
# - cd C:\gittest
#
# 4. git이 사용할 이력 저장 폴더 만들기
# - git init
#
# 5. git 관리 현황 확인하기
# - git status
#
# 6. 이력 관리할 폴더 및 파일 선택
# - git add work1
# - work1 폴더만 추가
# - git add.
# - 모든 파일 및 폴더 추가
#
# 7. 잘  추가 되었는지 현황 확인
# - git status
#
# 8. 실제로 이력을 저장
# - git commit - m "첫번째 버전"
#
# 9. 저장(commit) 된 이력 확인
# - git log
#
# 10. 첫번째 버전으로 되돌리기
# - git checkout 커밋번호
#
# 11. 다시 원래 최신으로 되돌리기
# - git checkout master
#
# 12. 원격저장소 등록
# - git remote add[원격지 이름] [원격지 주소]
#
# 13. 현재 내 이력 파일을 원격저장소에 밀어넣기
# - git push[원격지 이름] master
# - 로그인 창 뜨면 본인 계정으로 로그인 진행
#
# 14. 새로운 작업 폴더 생성하고 git 저장소 만들기
# - 작업 폴더 생성 후
# - git init
#
# 15. 새로운 작업 폴더에 원격저장소 등록
# - git remote add[원격지 이름] [원격지 주소]
#
# 16. 새로운 작업 폴더에 원격지 파일 당겨오기.
# - git pull[원격지 이름] master
#
# 복사: 컨트롤 + 쉬프트 + insert
# 붙여넣기: 쉬프트 + insert


## 클래스 객체
# 객체 = 데이터 + 함수

# 사람 정보 표현
age = 20
name = "홍길동"

print(f"{age}살 {name}입니다.") # 실행안되면 Ctrl + shift + F10 으로 실행


age2 = 22
name2 = "이순신"
print(f"{age2}살 {name2}입니다.") # 실행안되면 Ctrl + shift + F10 으로 실행

# 같은 형식이므로 함수로

def introduce(age, name):
    print(f"{age}살 {name}입니다.")

introduce(age, name)
introduce(age2, name2)

# age, name 헷갈리면 뒤죽박죽 될수도 있다
# 정보가 여러개면 사람별로 묶자 -> 클래스
class Person:
    def __init__(self):
        self.age = 22
        self.name = "이순신"
a1 = Person()
print(a1.age)
print(a1.name)

#매번 클래스를 만들수 없으므로 클래스 틀만 만든다
class Person1:
    def __init__(self, age, name):
        self.age = age
        self.name = name
p1 = Person1(20, "홍길동")
print(p1.age)
print(p1.name)

p2 = Person1(22, "이순신")

p3 = Person1(32, "황진이")

introduce(p1.age, p1.name)
introduce(p2.age, p2.name)
introduce(p3.age, p3.name)

#introduce 를 객체에 넣어버리면 따로 함수를 출력할 필요가 없다
class Person2:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def introduce(self):
         print(f"{self.age}살 {self.name}입니다.")

p1 = Person2(20, "홍길동")
p2 = Person2(22, "이순신")
p3 = Person2(32, "황진이")

p1.introduce()
p2.introduce()
p3.introduce()