from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Director, Movie, Review
from .serializers import (
    DirectorSerializer,
    DirectorDetailSerializer,
    MovieSerializer,
    MovieDetailSerializer,
    ReviewSerializer,
    ReviewDetailSerializer,
    MovieValidateSerializer,
    MovieReviewSerializer
)

class DirectorListCreateView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
    lookup_field = 'id'

class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieValidateSerializer
        return MovieSerializer

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

class MovieReviewsView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer

class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'













































# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'Директор не найден'},
#                         status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         data = DirectorSerializer(director, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(director, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         with transaction.atomic():
#             movie = Movie.objects.create(
#                 title=serializer.validated_data.get('title'),
#                 description=serializer.validated_data.get('description'),
#                 duration=serializer.validated_data.get('duration'),
#                 director_id=serializer.validated_data.get('director_id'),
#             )
#         return Response(data=MovieDetailSerializer(movie).data,
#                         status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Фильм не найден'},
#                         status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         data = MovieDetailSerializer(movie, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data=serializer.errors)
#         with transaction.atomic():
#             movie.title = serializer.validated_data.get('title')
#             movie.description = serializer.validated_data.get('description')
#             movie.duration = serializer.validated_data.get('duration')
#             movie.director_id = serializer.validated_data.get('director_id')
#             movie.save()
#         return Response(data=MovieDetailSerializer(movie).data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializer(reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Review не найдено'},
#                         status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         data = ReviewDetailSerializer(review, many=False).data
#         return Response(data=data)
        
#     elif request.method == 'PUT':
#         serializer = ReviewDetailSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def movie_reviews_api_view(request):
#     movies = Movie.objects.all()
#     data = []
#     for movie in movies:
#         reviews = movie.reviews.all()
#         total_stars = sum(review.stars for review in reviews)
#         avg_rating = total_stars / len(reviews) if reviews else 0
#         movie_data = MovieSerializer(movie).data
#         movie_data['rating'] = round(avg_rating, 2)
#         movie_data['reviews'] = ReviewSerializer(reviews, many=True).data
#         data.append(movie_data)
#     return Response(data=data)