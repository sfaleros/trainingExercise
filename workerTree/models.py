from django.db import models


class Workers(models.Model):
    full_name= models.CharField("name", max_length=30)
    salary= models.IntegerField("salay")
    boss= models.ForeignKey("self", on_delete=models.DO_NOTHING, default=None, blank=True,null=True)

    def __str__(self) :
        return self.full_name


# Create your models here.
