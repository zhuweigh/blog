from django.db import models
from django.core.urlresolvers import reverse
class Artical(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length= 50,blank = True)
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField(blank=True,null=True)

	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id':self.id})
	#	print (path)
		return "http://192.168.19.153:9000%s" % path

	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-date_time']
