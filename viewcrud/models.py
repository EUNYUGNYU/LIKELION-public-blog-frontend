from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField('data published')
    body=models.TextField()

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title