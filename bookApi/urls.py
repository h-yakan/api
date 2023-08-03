from django.urls import path
from . import views

urlpatterns = [
    # path('bookCreate',views.books,name='bookCreate'),
    path('',views.books,name='index'),
    path('<int:id>',views.bookById,name='get_by_id'),
    # path('bookUpdate/<int:id>',views.bookById,name='bookUpdate'),

]
