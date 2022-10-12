"""summit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from summitapi.views.climb import ClimbView
from summitapi.views.climb_type import ClimbTypeView
from summitapi.views.deactivate import DeactivateView
from summitapi.views.demote import DemoteView
from summitapi.views.grade import GradeView
from summitapi.views.hike import HikeView
from summitapi.views.my_hike import MyHikeView
from summitapi.views.profile import ProfileView
from summitapi.views.tag import TagView
from summitapi.views.auth import login_user, register_user
from summitapi.views.hike_skill_levels import HikeSkillLevelView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'climb_types', ClimbTypeView, 'climb_type')
router.register(r'climbs', ClimbView, 'climb')
router.register(r'grades', GradeView, 'grade')
router.register(r'hike_skill_levels', HikeSkillLevelView, 'hike_skill_level')
router.register(r'deactivates', DeactivateView, 'deactivate')
router.register(r'demotes', DemoteView, 'demote')
router.register(r'hikes', HikeView, 'hike')
router.register(r'my_climbs', ClimbView, 'my_climb')
router.register(r'my_hikes', MyHikeView, 'my_hike')
router.register(r'profiles', ProfileView, 'profile')
router.register(r'tags', TagView, 'tag')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
