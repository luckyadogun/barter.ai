# import uuid

# from django.db import models
# from django.utils.text import slugify

# from taggit.managers import TaggableManager

# from .profile_models import Profile



# class Comment(models.Model):
#     commentor = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     body = models.TextField()

#     def __str__(self):
#         return f'{self.commentor}

# # before saving a users pitch, parse the text to find email n url
#  class Pitch(models.Model):
#     slug = models.SlugField()
#     entrepreneur = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, blank=False, null=True)
#     body = models.TextField()
#     skills_needed = TaggableManager()

#     def __str__(self):
#         return self.title


# # Feeds
# p = Pitch.objects.filter(entrepreneur__user_skills__contains=request.user_skills)
# # My Connects
# c = Comment.objects.filter(commentor=request.user.implementer)