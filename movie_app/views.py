from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, MovieSerializer, 
                          MovieDetailSerializer, ReviewSerializer,
                          ReviewDetailSerializer)


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Директор не найден'},
                        status=status.HTTP_404_NOT_FOUND)
    
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Фильм не найден'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_reviews_api_view(request):
    movies = Movie.objects.all()
    data = []
    for movie in movies:
        movie_data = MovieSerializer(movie).data
        movie_data['rating'] = movie.average_rating()  
        movie_data['reviews'] = ReviewSerializer(movie.reviews.all(), many=True).data
        data.append(movie_data)
    
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review не найдено'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)
