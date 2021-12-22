from django.urls import path, include
from django.contrib import admin
# from movie.views import ActorApiViewSet,MovieApiViewSet
from rest_framework.routers import DefaultRouter
from movie.views import MovieListApiView,MovieRetriveApiView,MovieCreateApiView, MovieRetriveApiView, MovieUpdateApiView, MovieDestroyApiView

# router=DefaultRouter()
# router.register('actor',ActorApiViewSet)
# router.register('movie',MovieApiViewSet)
from movie.models import Movie
from movie.serializer import MovieSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('movie/', MovieListApiView.as_view(),name='movie-list'),
    path('movies/', MovieCreateApiView.as_view(),name='movie-create'),
    path('movies/<int:pk>', MovieRetriveApiView.as_view(),name='movie-get'),
    path('movies/<int:pk>', MovieUpdateApiView.as_view(),name='movie-update'),
    path('movies/<int:pk>', MovieDestroyApiView.as_view(),name='movie-delete'),
    # path('movie/', MovieCreateApiView.as_view(queryset=Movie.objects.all(), serializer_class=MovieSerializer), name='user-post')

]
