<<<<<<< HEAD
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustoomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError("You must provide and email address")

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name, first_name, password, **other_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustoomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ranking")
    points = models.IntegerField(default=0)
    distance_km = models.IntegerField(default=0)
    max_speed_kmh = models.IntegerField(default=0)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Articles(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    tags = models.ManyToManyField(Tag)


class ArticlesComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_comments")
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    thumbnail_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    youtube_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to="videos/", blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="videos")
    tags = models.ManyToManyField('Tag')


class VideoComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="video_comments")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)


class Slopes(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    level_green = models.BooleanField()
    level_blue = models.BooleanField()
    level_red = models.BooleanField()
    level_black = models.BooleanField()
    status = models.BooleanField()
=======
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustoomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError("You must provide and email address")

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name, first_name, password, **other_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustoomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name


class Ranking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ranking")
    points = models.IntegerField(default=0)
    distance_km = models.IntegerField(default=0)
    max_speed_kmh = models.IntegerField(default=0)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Articles(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    tags = models.ManyToManyField(Tag)


class ArticlesComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_comments")
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    thumbnail_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    youtube_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to="videos/", blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="videos")
    tags = models.ManyToManyField('Tag')


class VideoComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="video_comments")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)


class Slopes(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    level_green = models.BooleanField()
    level_blue = models.BooleanField()
    level_red = models.BooleanField()
    level_black = models.BooleanField()
    status = models.BooleanField()
>>>>>>> ab63734 (Dodanie aplikacji Django + React)
