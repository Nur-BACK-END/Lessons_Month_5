from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    def average_rating(self):
            reviews = self.reviews.all()
            if reviews:
                total_stars = sum(review.stars for review in reviews)
                return round(total_stars / len(reviews), 2)  
            return 0


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text    
    