from django.db import models

class TestConnection(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



class Question(models.Model):
    TRAIT_CHOICES = [
        ("O", "Openness"),
        ("C", "Conscientiousness"),
        ("E", "Extraversion"),
        ("A", "Agreeableness"),
        ("N", "Neuroticism"),
    ]

    text = models.CharField(max_length=255)
    trait = models.CharField(max_length=1, choices=TRAIT_CHOICES)
    weight = models.IntegerField(default=1)
    reverse = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    

class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    scores = models.JSONField() 