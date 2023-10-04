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