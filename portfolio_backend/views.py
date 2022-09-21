from rest_framework import viewsets
from .models import *
from .serializers import *

class AboutViewSet (viewsets.ModelViewSet):
    queryset=About.objects.all().order_by("-id")
    serializer_class=AboutSerializers

class BrandViewSet (viewsets.ModelViewSet):
    queryset=Brand.objects.all().order_by("-id")
    serializer_class=BrandSerializers

class ContactViewSet (viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by("-id")
    serializer_class=ContactSerializers

class ExperienceViewSet (viewsets.ModelViewSet):
    queryset=Experience.objects.all().order_by("-id")
    serializer_class=ExperienceSerializers

class SkillViewSet (viewsets.ModelViewSet):
    queryset=Skill.objects.all().order_by("-id")
    serializer_class=SkillSerializers

class TestimonialViewSet (viewsets.ModelViewSet):
    queryset=Testimonial.objects.all().order_by("-id")
    serializer_class=TestimonialSerializers

class WorkExperienceViewSet (viewsets.ModelViewSet):
    queryset=WorkExperience.objects.all().order_by("-id")
    serializer_class=WorkExperienceSerializers

class WorkViewSet (viewsets.ModelViewSet):
    queryset=Work.objects.all().order_by("-id")
    serializer_class=WorkSerializers