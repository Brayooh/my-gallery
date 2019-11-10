from django.db import models

class image(models.Model):
    image = models.ImageField(upload_to='images')
    image_name = models.CharField(max_length=50)
    caption = models.CharField()
    image_location = models.CharField(max_length=60)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)



class category(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
