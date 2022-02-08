from django.db import models


class City(models.Model):
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}, {self.country}'


class Post(models.Model):
    title = models.CharField(max_length=500)
    owner = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='posts')
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    safety = models.IntegerField()

    def __str__(self):
        return self.title


class Discussion(models.Model):
    title = models.CharField(max_length=500)
    owner = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='discussions')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='discussions')
    content = models.TextField()

    def __str__(self):
        return self.title


class Picture(models.Model):
    name = models.CharField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='pictures')
    url = models.TextField()

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='places')
    address = models.TextField()

    def __str__(self):
        return self.name


class Do(models.Model):
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, related_name='dos', primary_key=True)
    is_do = models.BooleanField()
