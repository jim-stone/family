from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Rodziny"

    def __str__(self) -> str:
        return "Rodzina " + self.name


class Member (models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(
        User, related_name='members', null=True, blank=True,
        on_delete=models.CASCADE)
    is_user = models.BooleanField()
    family = models.ForeignKey(
        Family, related_name='members',
        on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Członkowie Rodzin"


class Assessment (models.Model):
    value = models.SmallIntegerField()
    comment = models.CharField(max_length=1024)
    member_target = models.ForeignKey(
        Member, related_name='opinions_about_me', on_delete=models.CASCADE)
    member_source = models.ForeignKey(
        Member, related_name='opinions_from_me', on_delete=models.CASCADE)

    def __str__(self) -> str:
        sign = 'Minus' if self.value == -1 else 'Plus'
        from_member = self.member_source.name
        return f'{sign} od {from_member}: {self.comment}'
