from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class image(models.Model):
    image = models.ImageField(upload_to='images')
    image_name = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)


     @classmethod
    def search_by_title(cls, search_term):
        image = cls.objects.filter(description__contains=search_term)

        return image

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

   




