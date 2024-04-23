from django.db import models

class Allergen(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    allergen = models.ForeignKey(
        Allergen,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.username

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)
    rating_id = models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Rating(models.Model):
    score = models.IntegerField()
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Rating for {self.recipe.title} by {self.user.username}"
