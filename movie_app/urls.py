from django.urls import path
from .views import (
    DirectorListCreateView,
    DirectorDetailView,
    MovieListCreateView,
    MovieDetailView,
    MovieReviewsView,
    ReviewListCreateView,
    ReviewDetailView
)

urlpatterns = [
    path('directors/', DirectorListCreateView.as_view()),
    path('directors/<int:id>/', DirectorDetailView.as_view()),
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<int:id>/', MovieDetailView.as_view()),
    path('movies/reviews/', MovieReviewsView.as_view()),
    path('reviews/', ReviewListCreateView.as_view()),
    path('reviews/<int:id>/', ReviewDetailView.as_view()),
]