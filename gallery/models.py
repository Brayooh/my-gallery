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
    caption = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        image_category = cls.objects.filter(category__contains=search_term)

        return image_category

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    

   




