from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Actor, Movie
from .serializer import ActorSerializer, MovieSerializer


class ActorApiViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    filter_backends = [OrderingFilter,SearchFilter]
    ordering_fields = ["name","gender","birth_date"]
    search_fields =["name","birth_date"]

    @action(methods=["GET"], detail=True, url_path='actor')
    def get_actor(self, request, *args, **kwargs):
        artist = self.get_object()
        albums = Actor.objects.filter(artist=artist)
        ser = ActorSerializer(albums, many=True)
        return Response(ser.data)

    # @action(methods=["POST"], detail=True, url_path='actor')
    # def post_s(self, request, *args, **kwargs):
    #     artist = self.get_object()
    #     album = request.data
    #     album["artist"] = artist.id
    #     ser = SongSerializer(data=album)
    #     if ser.is_valid():
    #         ser.save()
    #     return Response(ser.data)
# class MovieApiViewSet(ModelViewSet):
#     serializer_class = MovieSerializer
#     queryset = Movie.objects.all()
#     filter_backends = [OrderingFilter, SearchFilter]
#     ordering_fields = ["title", "genre", "date"]
#     search_fields = ["title", "date"]
#
#     @action(methods=["GET"], detail=True, url_path='actor')
#     def get_movie(self, request, *args, **kwargs):
#         artist = self.get_object()
#         albums = Movie.objects.filter(artist=artist)
#         ser = MovieSerializer(albums, many=True)
#         return Response(ser.data)
class MovieListApiView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateApiView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetriveApiView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateApiView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDestroyApiView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer