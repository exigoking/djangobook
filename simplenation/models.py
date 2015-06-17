from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from simplenation.addons import last_posted_date
from taggit.managers import TaggableManager
from registration.signals import user_registered
from django.db.models import Count

# Create your models here.

class Term(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	tags = TaggableManager()
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Term, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name

class Author(models.Model):
	user = models.OneToOneField(User)
	
	bio = models.CharField(max_length=1024)
	picture = models.ImageField(upload_to='profile_images', default = 'profile_images/default_profile_picture.png')
	slug = models.SlugField(unique=True)
	account_deletion_key = models.CharField(max_length = 64, blank = True)
	score = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
	rank = models.IntegerField(default=9999999)
	num_of_likes = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user.username)
		super(Author, self).save(*args, **kwargs)

	def ranking(self):
		aggregate = Author.objects.filter(score__gt=self.score).aggregate(ranking=Count('score'))
		return aggregate['ranking'] + 1

	def __unicode__(self):
		return self.user.username
	

class Definition(models.Model):
	author = models.ForeignKey(Author)
	term = models.ForeignKey(Term)
	body = models.TextField(max_length=512)
	likes = models.IntegerField(default=0)
	post_date = models.DateTimeField(auto_now_add=True)	
	last_posted = models.CharField(max_length=128, blank=True)
	like_text = models.CharField(max_length=128, default='Like')
	times_reported = models.IntegerField(default=0)
	reporter = models.IntegerField(default=0)


	def __unicode__(self):
		return self.term.name


class Like(models.Model):
	user = models.ForeignKey(User)
	definition = models.ForeignKey(Definition)
	liked = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username

class Report(models.Model):
	user = models.ForeignKey(User)
	definition = models.ForeignKey(Definition)
	reported = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username


# def user_registered_callback(sender, user, request, **kwargs):
# 	profile = Author(user = user)
# 	profile.bio = request.POST['bio']
# 	if 'picture' in request.FILES:
# 				profile.picture = request.FILES['picture']
# 	profile.save()

# user_registered.connect(user_registered_callback)
