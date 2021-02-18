from django.shortcuts import render

posts = [
		{
		'author' : 'Andrew C',
		'title': 'how to learn python',
		'content': 'first lessons content',
		'date_posted': 'August 24, 2020'

		}

		{
		'author' : 'Chris C',
		'title': 'how to learn html',
		'content': 'first lessons content',
		'date_posted': 'August 25, 2020'

		}
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
		}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')


 