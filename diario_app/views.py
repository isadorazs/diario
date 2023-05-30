from django.shortcuts import render
from diario_app.models import Entry
from django.shortcuts import render, redirect


def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'diario_app/entry_list.html', {'entries': entries})

def create_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Entry.objects.create(title=title, content=content)
        return redirect('entry_list')
    return render(request, 'diario_app/create_entry.html')
