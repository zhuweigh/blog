#from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from django.contrib.syndication.views import Feed 
from django.shortcuts import render, redirect
from artical.models import Artical
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
#	post_list = Artical.objects.all() 
#	return render(request,'home.html',{'post_list' : post_list})


#def detail(request, my_args):
#	#return HttpResponse("You're looking at my_args %s." % my_args)
#	post = Artical.objects.all()[int(my_args)]
#	str = ("title = %s, category = %s, date_time = %s, content = %s" 
#			% (post.title, post.category, post.date_time, post.content))
#	return HttpResponse(str)
def detail(request,id):
	#try:
	post = Artical.objects.get(id=str(id))
	#except Artical.DoesNotExist:
	#	pass
	return render(request, 'post.html', {'post' : post})
def archives(request) :
	try:
		post_list = Artical.objects.all()
	except Artical.DoesNotExist :
		raise Http404
	return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def about_me(request) :
	    return render(request, 'aboutme.html')
def search_tag(request, tag) :
	try:
		post_list = Artical.objects.filter(category__iexact = tag) #contains
	except Artical.DoesNotExist :
		raise Http404
	return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
	if 's' in request.GET:
		s = request.GET['s']
		if not s:
			return render(request,'home.html')
		else:
			post_list = Artical.objects.filter(title__icontains = s)
			if len(post_list) == 0 :
				return render(request,'archives.html', {'post_list' : post_list,'error' : True})
			else :
				return render(request,'archives.html', {'post_list' : post_list,'error' : False})
	return redirect('/')
#def test(request):


class RSSFeed(Feed):
	title = "RSS feed - article"
	link = "feeds/posts/"
	description = "RSS feed - blog posts"
	def items(self):
		return Artical.objects.order_by('-date_time')
	def item_title(self, item):
		return item.title
	def item_pubdate(self, item):
		return item.add_date
	def item_description(self, item):
		return item.content


def home(request):
	posts = Artical.objects.all()  
	paginator = Paginator(posts, 2) 
	page = request.GET.get('page')
	print(page)
	#print(paginator)
	#try :
	post_list = paginator.page(1)
	print(post_list)
	#except PageNotAnInteger :
	#	post_list = paginator.page(1)
	#except EmptyPage :
	#	post_list = paginator.paginator(paginator.num_pages)
	return render(request, 'home.html', {'post_list' : post_list})
