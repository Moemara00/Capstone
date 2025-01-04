from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BooksViewsetAdmin , CheckOutView, UnCheckOutView


router = DefaultRouter()
router.register('list',BooksViewsetAdmin,basename='list')
router.register('checkout',CheckOutView,basename='checkout')
router.register('uncheckout',UnCheckOutView,basename='uncheckout')
urlpatterns = router.urls

