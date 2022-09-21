from django.urls import path,include
from .views import *
from rest_framework import routers


route = routers.DefaultRouter()
route.register("about",AboutViewSet,basename="about")
route.register("brand",BrandViewSet,basename="brand")
route.register('contact',ContactViewSet,basename="contact")
route.register('experience',ExperienceViewSet,basename="experience")
route.register('skill',SkillViewSet,basename="skill")
route.register('testimonial',TestimonialViewSet,basename="testimonial")
route.register('workexperience',WorkExperienceViewSet,basename="workexperience")
route.register('work',WorkViewSet,basename="work")


urlpatterns = [
    path("",include(route.urls)),
]