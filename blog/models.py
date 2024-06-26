from django.db import models
from django.utils.text import slugify


class TagModel(models.Model):
	name = models.CharField(unique=True, max_length=20)



class BlogModel(models.Model):
	tag = models.ForeignKey('TagModel', on_delete=models.CASCADE, related_name='blogs')
	title = models.CharField(unique=True, max_length=100)
	slug = models.SlugField(unique=True, editable=False, max_length=40)
	caption = models.TextField()
	content = models.TextField()
	cover = models.URLField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-updated_at', )
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)


class CommentModel(models.Model):
	blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=100)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created_at', )


class ImageModel(models.Model):
	imagelink = models.URLField()



class SpecialblogModel(models.Model):
	blog = models.OneToOneField('BlogModel', null=True, blank=True, on_delete=models.CASCADE, related_name='special_blog')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

