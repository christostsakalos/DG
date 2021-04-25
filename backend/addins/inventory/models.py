from django.db import models



# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=255)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")
    def __unicode__(self):
        return self.name
    def __str__(self):
        return '%s' % self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    parent =models.ForeignKey(Category,on_delete=models.SET_NULL, related_name='sub_categories', blank=True, null=True)

    class Meta:
        verbose_name = ("subcategory")
        verbose_name_plural = ("subcategories")
    def __unicode__(self):
        return self.name
    def __str__(self):
        return '%s' % self.name



class Part(models.Model):
    name       = models.CharField(max_length=120)
    description = models.CharField(max_length=120,blank=True,null=True)
    quantity = models.FloatField(default=1)
    category    = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, related_name='parts', null=True)

    class Meta:
        verbose_name = ('part')
        verbose_name_plural = ('parts')
    def __str__(self):
        return '%s' % self.name
