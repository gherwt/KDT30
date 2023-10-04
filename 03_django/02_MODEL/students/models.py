from django.db import models

# Create your models here.
# id(integer) name(Char 10) address(Text) major(Char 100) age(integer) cgpa(float) 설정
# column 을 정의하는 곳이다.
# 테이블명, 컬럼명 = 데이터 타입
            
            # 상속을 받는다.           
class Student(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    cgpa =  models.FloatField()

# 새로운 값을 추가 시 default 값을 설정해줘야함
# 새로운 값 추가하면 기존 값들에는 빈값이 생기기 때문에 문제가 발생할 수 있다.
# 0001 , 0002 쌓이는 것은 버전이다. versioning 이 가능
# schema 를 설계, table 을 만든다. 설정한다.

class Professor(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=100)
    room = models.TextField()
    year = models.IntegerField()

if __name__ == '__main__':
     pass
    # CRUD

# # create

# s = Student()
# s.name = '김학생'
# s.address = '서울'
# s.major = '컴공'
# s.age = '25'
# s.cgpa = '3.7
    
# Student.objects.create(
#     name='박학생',
#     major = '경영',
#     age = 22,
#     address = '부산',
#     cgpa = 3.3
# )

# # read

# #1. 전체 조회
# Student.objects.all()

# students = Student.objects.all()
# for student in students:
#     print(student.pk, student.name, student.major)  

# #2. 단일 조회

# Student.objects.get() # Column 명 = Column 내의 값

# # get 은 중복일 경우에 오류가 발생한다.

# Student.objects.get(id = ''), Student.objects.get(pk = '')

# # 그렇기 때문에 id, pk 값을 사용해준다. id 값은 python 에서 고유 설정된 값이 있기 때문에 충돌 가능성이 있다.
# #  id = Column 명, pk = Primary Key

# s1 = Student.objects.get(pk=1)
# s1.name, s1.id, s1.pk, s1.address, s1.cgpa
    
# # 이런식으로 변수를 하나 할당해 조회할 수도 있다.

# # 수정

# s1 = Student.objects.get(pk=1)
# s1.cgpa = 4.0
# s1.save()


# # 삭제
# s1 = Student.objects.get(pk=1)
# s1.delete()