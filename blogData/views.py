from django.shortcuts import render, redirect
from .models import Post, Author, Tag, Comment
from django.shortcuts import get_object_or_404
from .forms import AuthorForm, PostForm, CommentForm
from django.http import HttpResponseRedirect

def index(request):
    posts = Post.objects.all().order_by("-date")[:3]

    return render(request, 'blogData/index.html',{
        'posts': posts,
    })

def post_details(request, id):
    posts = get_object_or_404(Post, id=id)
    tags = Tag.objects.all()
    comments = posts.comments.order_by("-date")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=posts,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                text=form.cleaned_data["text"]
            )
            return redirect("post_details", id=posts.id)
    else:
        form = CommentForm()

    return render(request, 'blogData/details.html', {
        'posts': posts,
        'tags': tags,
        'comments': comments,
        'form': form,
    })

def all_posts(request):
    posts = Post.objects.all()

    return render(request, 'blogData/allPosts.html',{
        'posts': posts,
    })

def for_tags(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blogData/forTags.html',{
        'posts': posts,
        'tags': tags,
    })

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        author_form = AuthorForm(request.POST)

        if post_form.is_valid() and author_form.is_valid():

            first = author_form.cleaned_data['first_name']
            last = author_form.cleaned_data['last_name']
            email = author_form.cleaned_data['email_address']

            author, created = Author.objects.get_or_create(
                email_address=email,
                defaults={
                    "first_name": first,
                    "last_name": last,
                }
            )
            image_file = request.FILES.get('image')

            post = Post.objects.create(
                title=post_form.cleaned_data['title'],
                excerpt=post_form.cleaned_data['excerpt'],
                content=post_form.cleaned_data['content'],
                image=image_file,
                author=author
            )

            post.tags.set(post_form.cleaned_data['tags'])
            return redirect('index')

    else:
        post_form = PostForm()
        author_form = AuthorForm()

    return render(request, "blogData/create_post.html", {
        "post_form": post_form,
        "author_form": author_form,
    })

def post_comments(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.order_by("-date")

    return render(request, "blogData/post_comments.html",{
        "post": post,
        "comments": comments,
    })
