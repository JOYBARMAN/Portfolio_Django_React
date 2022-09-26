from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="protfolio/about/")

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="protfolio/brand/")


    def __str__(self):
        return self.name


class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Experience (models.Model):
    year = models.CharField(max_length=100)
    work = models.TextField()

    def __str__(self):
        return self.year


class Skill (models.Model):
    name = models.CharField(max_length=255)
    bgColor = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="protfolio/skill/")

    def __str__(self):
        return self.name


class Testimonial (models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    image = models.ImageField(upload_to="protfolio/testimonial/")
    feedback = models.TextField()
    
    def __str__(self):
        return self.name


class WorkExperience (models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Tag (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Work (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    projectLink = models.CharField(max_length=255)
    codeLink = models.CharField(max_length=255)
    image = models.ImageField(upload_to="protfolio/work/")
    tag_name = models.OneToOneField(Tag,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title