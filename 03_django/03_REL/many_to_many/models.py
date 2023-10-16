from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return f'{self.pk} => {self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    # 하나의 movie에 여러명 actor가 포함되어 있기 때문에
    # 아래의 ActorMovie 클래스 정의를 이 한 줄로 대체 가능하다. 중개 테이블을 생성함.
    actors = models.ManyToManyField(Actor, related_name= 'movies')
    # movie => actors로 접근 / actor => movies 로 접근



# class ActorMovie(models.Model):
#     actor = models.ForeignKey(Actor)
#     movie = models.ForeignKey(Movie)

if __name__ == '__main__':
    # python manage.py shell_plus
    m1 = Movie.objects.get(pk = 1)
    m2 = Movie.objects.get(pk = 2)
    m3 = Movie.objects.get(pk = 3)
    m4 = Movie.objects.get(pk = 4)
    m5 = Movie.objects.get(pk = 5)

    a1 = Actor.objects.get(pk = 1)
    a2 = Actor.objects.get(pk = 2)
    a3 = Actor.objects.get(pk = 3)
    a4 = Actor.objects.get(pk = 4)
    a5 = Actor.objects.get(pk = 5)


    # M:N 관계 추가
    # 영화에 배우 추가
    m1.actors.add(a1)
    m1.actors.add(a2, a4)
    # 배우에 영화 추가
    a2.movies.add(m3, m4)
    a2.movies.add(3, 4, 5)
    # 관계는 2번 추가되지 않고 1번만 추가된다.
    # 앞뒤가 바뀌어도 동등한 관계이다.

    # M:N 관계 삭제 코드(아래 2개 중 택 1)
    a2.movies.remove(m3)
    m3.actors.remove(a2)

    # M:N 조회 코드
    a3.movies.all()
    m5.actors.all()

    # m3의 출연진 중 첫번째 출연진의 필모
    # 인덱스 적용이 가능하다.

    m3.actors.all()[0].movies.all()

    pass