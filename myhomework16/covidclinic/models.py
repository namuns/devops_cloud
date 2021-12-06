from django.core.validators import RegexValidator
from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='병원 이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    weekdaytime = models.CharField(max_length=30, verbose_name='평일 운영시간')
    sattime = models.CharField(max_length=30, verbose_name='토요일 운영시간')
    hdaytime = models.CharField(max_length=30, verbose_name='일요일/공휴일 운영시간')
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{2,3,4}-?\d{3,4}-?\d{4}$", message="전화번호를입력해주세요."),
                                 ], verbose_name='대표 전화번호')
    controlcenter = models.CharField(max_length=30, verbose_name='관할보건소')
    centertel = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{2,3,4}-?\d{3,4}-?\d{4}$", message="전화번호를입력해주세요."),
                                 ], verbose_name='관할보건소 전화번호')
    afdp = models.TextField(blank=True, verbose_name='장애인 편의사항')
