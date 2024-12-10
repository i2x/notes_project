from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# List notes
def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

# View note details
def detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/detail.html', {'note': note})

# Create a new note
def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes/form.html', {'form': form, 'title': 'Create Note'})

# Update an existing note
def update(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/form.html', {'form': form, 'title': 'Update Note'})

# Delete a note
def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'notes/delete.html', {'note': note})
