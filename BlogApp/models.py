from django.db import models
from django.utils import timezone 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=30000)
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse("post_detail",kwargs={'pk':self.pk})

	def approve_comments(self):
		return self.comments.filter(approve_comment=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey('BlogApp.Post',related_name='comments',on_delete=models.CASCADE)
	author = models.CharField(max_length=200)
	create_date = models.DateTimeField(default=timezone.now(),null=True)
	approve_comment = models.BooleanField(default=False)
	text = models.TextField()

	def approve(self):
		self.approved_comments=True
		self.save()

	def get_absolute_url(self):
		return reverse("post_list")