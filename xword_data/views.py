from random import randint
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from .models import Puzzle, Clue, Entry
from .forms import WordForm


def random_selector():
    maximum_id = Clue.objects.last().id
    random_clue = None
    while random_clue is None:
        random_id = randint(0, maximum_id)
        try:
            random_clue = Clue.objects.get(id=random_id)
        except Clue.DoesNotExist:
            continue
    else:
        return random_clue
    

def drill(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            clue_id = request.POST.get('clue_id')
            random_clue = Clue.objects.get(id=clue_id)
            clue_length = len(random_clue.entry.entry_text)
            clue_puzzle = random_clue.puzzle.title
            if answer.upper() == random_clue.entry.entry_text:
                return redirect(reverse('xword-answer', args=(clue_id,)))
            else:
                return render(request, 'xword_data/drill.html', {'clue_length': clue_length, 'clue_puzzle': clue_puzzle, 'clue_id':random_clue.id, 'form':form, 'message':'not correct'})
    else:
        random_clue = random_selector()
        form = WordForm()
        clue_length = len(random_clue.entry.entry_text)
        clue_puzzle = random_clue.puzzle.title
        return render(request, 'xword_data/drill.html', {'clue_length': clue_length, 'clue_puzzle': clue_puzzle, 'clue_id':random_clue.id, 'form':form})
        

def answer(request, clue_id):
    clues = Clue.objects.all().select_related("entry")
    clues_count = clues.count()
    return render(request, 'xword_data/answer.html', {'clues_count': clues_count, 'clues': clues})