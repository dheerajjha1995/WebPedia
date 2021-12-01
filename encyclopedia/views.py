from django.shortcuts import render, redirect
import markdown as md
from random import randint
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        content = "Yet to be discovered! Help us grow"
    content = md.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        'content': content, 'title': title
    })

def add(request):
    entries = util.list_entries()

    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title=='':
            return render(request, 'encyclopedia/error.html',{'message': 'Title was left empty'})
        
        if title in entries:
            return render(request, 'encyclopedia/error.html',{'message': 'Title already exists TRY anything else'})

        if content=='':
            return render(request, 'encyclopedia/error.html',{'message': 'Content was left empty'})

        util.save_entry(title, content)
        return render(request, 'encyclopedia/add.html')
    
    return render(request, 'encyclopedia/add.html')

def edit(request, title):
    content = util.get_entry(title)
    
    if request.method == 'POST':
        content = request.POST.get("content")
        if content=='':
            return render(request, 'encyclopedia/error.html',{'message': 'Content was left empty'})
        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, 'encyclopedia/edit.html',{'content': content, 'title': title})

def random(request):
    entries = util.list_entries()
    random_title = entries[randint(0, len(entries)-1)]
    return redirect("entry", title=random_title)

def find(request):
    entries = util.list_entries()
    q = request.GET.get('q').upper()
    entries_upper = [x.upper() for x in entries]
    if q in entries_upper:
        return redirect("entry", title=q)
    res = [i for i in entries_upper if q in i]
    
    return render(request, "encyclopedia/find.html", {
        "entries": res
    })
