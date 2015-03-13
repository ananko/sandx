from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from sandbox.forms import NewNoteForm
from sandbox.models import Note

@login_required
def overview(request):
    return render(request, 'sandbox/overview.html', {})

@login_required
def profile(request):
    return render(request, 'sandbox/profile.html', {})

@login_required
def notes(request):
    notes = request.user.notes.all()
    errors = []
    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content'].strip()
            if content:
                user = request.user
                Note.create(user, content)
            else:
                errors.append('Note content cannot be empty')
        else:
            errors.extend(form.errors)
    else:
        form = NewNoteForm()
    return render(request, 'sandbox/notes.html', {'notes': notes, 'newNoteForm': form, 'errors': errors})

@login_required
def delete_note(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.delete()
    return redirect('sandbox:notes')
 
