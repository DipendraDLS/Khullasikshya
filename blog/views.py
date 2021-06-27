from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from .models import Blog, BlogComment
from django.shortcuts import render, redirect
from admin_home.decorators import admin_required
from .forms import AdminBlogForm
import sweetify
from django.db.models import Q
from django.contrib import messages


# Create your views here.


################################## Frontend View ##################################################################
def blog(request):
    query = request.GET.get('search')
    if query:
        page_obj = Blog.objects.filter(Q(blog_title__icontains=query) | Q(blog_content__icontains=query)).distinct()
        context = {'page_obj': page_obj, 'query': query}
        return render(request, 'blog/frontend/blog.html', context)

    show = Blog.objects.filter().order_by('-id')
    paginator = Paginator(show, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, }

    return render(request, 'blog/frontend/blog.html', context)


def blogDetail(request, id):
    blog_content = Blog.objects.get(id=id)
    latest_blog = Blog.objects.filter().order_by('-id')
    comments = BlogComment.objects.filter(blog_id=id, parent=None).order_by('-id')
    replies = BlogComment.objects.filter(blog_id=id).exclude(parent=None)  # Jati pani BlogComment model ko parent field ma null cha tyo sab lai exclude garera query nikalcha. So thath it's only the replies.
    replyDict = {}  # Blank replyDict vanni dictonary banayeko.
    for reply in replies:  # sabai replies lai itterate gareko.
        if reply.parent.id not in replyDict.keys():  # This is only for the 1st reply of a comment(NOTE: 1st time kunai comment ma reply gardai cha vani tyo comment ko id ni basalna parcha so 'not in' jahiley 1st time comment garni bela true huncha)....replyDict ma yesari data  basos ki ... key chai comment ko hos(i.e paren.id which is the field in BlogComment Model and it is self foreignkey) and values chai tei comment ko replies haru hos.
                                                     # Eg: yedi 14 no. gareko id ko comment ma reply diyeko cha vani replyDict = {14: [<BlogComment: BlogComment object (15)>]}  yesari key, value banera baseko huncha.
            replyDict[reply.parent.id] = [reply]
        else:                                        # yo else part le chai yedi kunai comment ko 2nd, 3rd, 4th jati ni aru reply haru huncha same comment ko  teslai handle garcha.
                                                     # i.e if it's 2nd reply of same comment then it has already parent.id so we need to only append the replies to that key.

            replyDict[reply.parent.id].append(reply)

    # print(replyDict)
    context = {'blog_content': blog_content,
               'latest_blog': latest_blog,
               'comments': comments,
               'replyDict': replyDict,
               }
    return render(request, 'blog/frontend/blog_details.html', context)


def blogComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        blogId = request.POST.get("blogId")
        blog = Blog.objects.get(pk=blogId)
        commentId = request.POST.get("commentId")
        if commentId == "":
            comment = BlogComment(comment=comment, user=user,
                                  blog=blog)  # blod=blogId yesari direct assign garna mildaina 'Blog' model kai through refrence vayeko huna parcha.
        else:
            parent = BlogComment.objects.get(id=commentId)
            comment = BlogComment(comment=comment, user=user, blog=blog, parent=parent)
        comment.save()

    return redirect('blogDetail', blogId)


################################## Backend View ##################################################################
@admin_required
def adminBlog(request):
    form = AdminBlogForm()
    if request.method == 'POST':
        form = AdminBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_title = form.cleaned_data['blog_title']
            blog_content = form.cleaned_data['blog_content']
            blog_image = form.cleaned_data['blog_image']
            user = request.user
            blog = Blog(blog_title=blog_title, blog_content=blog_content, blog_image=blog_image, user=user)
            blog.save()
            sweetify.success(request, 'Blog added successfully!',
                             text='Good job! You have successfully added Blog.',
                             persistent='ok')
            return redirect('adminBlog')

    blogs = Blog.objects.all().order_by('-id')

    context = {'form': form, 'blogs': blogs}
    return render(request, 'blog/backend/admin_blog.html', context)


@admin_required
def adminBlogDelete(request, id):
    if request.method == 'POST':
        delete_blog = Blog.objects.get(pk=id)
        delete_blog.delete()
        sweetify.success(request, 'Blog deleted successfully!',
                         text='Good job! You have successfully deleted Blog.',
                         persistent='ok')
        return redirect('adminBlog')


@admin_required
def adminBlogEdit(request, id):
    form = AdminBlogForm()

    if request.method == 'POST':
        edit_record = Blog.objects.get(pk=id)
        form = AdminBlogForm(request.POST or None, request.FILES or None,
                             instance=edit_record)  # request.FILES is needed for updating the image field as well and while saving form we need to do this => edit = form.save(commit=False) and then only edit.save()
        if form.is_valid:
            edit = form.save(commit=False)
            edit.save()
            sweetify.success(request, 'Blog edited successfully!',
                             text='Good job! You have successfully edited Blog.',
                             persistent='ok')

        return redirect('adminBlog')
    else:
        edit_record = Blog.objects.get(pk=id)
        form = AdminBlogForm(instance=edit_record)
    return render(request, 'blog/backend/edit.html', {'form': form})
