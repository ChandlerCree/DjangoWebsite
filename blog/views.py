from django.shortcuts import render

posts = [
	{
		'author': 'DavidCree',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'February 6, 2020'
	},
	{
		'author': 'ChloeHasund',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'February 4, 2020'
	}
]


def home(request):
	context = {
		'post_dict': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})	