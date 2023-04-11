from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewset, LoginView, Varify_User, Transaction_Records

router = DefaultRouter()

router.register('register', RegisterViewset, basename='register')
router.register('login', LoginView, basename='login')
router.register('varify', Varify_User, basename='varify')
router.register('transactions', Transaction_Records, basename='transactions')
# router.register('varify', Varify_User, basename='varify')

urlpatterns = [
    path('', include(router.urls)),
    
]
