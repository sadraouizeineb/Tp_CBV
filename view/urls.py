from django.urls import path
from view.views import BlogView,BlogCreateWithFields,blogUpdateView,blogDeleteView,BlogCreateWithForm
app_name="Posts"
urlpatterns = [
    path('liste',BlogView.as_view(),name='listhtml'),
    path('create',BlogCreateWithFields.as_view(),name='createhtml'),
        path('create2',BlogCreateWithForm.as_view(),name='createhtml'),

    path('update/<int:pk>',blogUpdateView.as_view(),name='updatehtml'),
    path('delete/<int:pk>',blogDeleteView.as_view(),name='deletehtml'),
    ]