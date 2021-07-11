from django.urls import path, include
from .views import NoteDetail, NoteAPIView

urlpatterns = [
    #path('note/', NoteList),
    path('note/', NoteAPIView.as_view()),
    path('detail/<int:id>/', NoteDetail.as_view()),
]