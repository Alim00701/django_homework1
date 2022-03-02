from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "OTHER")
    )
    OCUP_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE")
    )
    phone_number = models.CharField("phone_number", max_length=60, unique=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    age = models.IntegerField()
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)
    mothers_maiden_name = models.CharField("mothers_maiden_name", max_length=60)
    best_friend_name = models.CharField("best_friend_name", max_length=50)
    place_of_residence = models.CharField("place_of_residence", max_length=30)
    favorite_song = models.CharField("favorite_song", max_length=50)
    first_book = models.CharField("first_book", max_length=45)
