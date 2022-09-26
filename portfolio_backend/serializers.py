from rest_framework import serializers
from .models import *

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class WorkExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"

class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Work
        depth=1
        fields = "__all__"

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"