from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member (models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(
        User, related_name='members', null=True, blank=True,
        on_delete=models.CASCADE)
    is_user = models.BooleanField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Członkowie Rodzin"


class Family(models.Model):
    name = models.CharField(max_length=250)
    members = models.ManyToManyField(Member, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Rodziny"

    def __str__(self) -> str:
        return "Rodzina " + self.name
