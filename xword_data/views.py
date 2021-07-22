from random import randint
from django.shortcuts import render
from django.http import HttpResponse

from .models import Puzzle, Clue, Entry


def random_selector():
    maximum_id = Clue.objects.last().id
    random_id = randint(0, maximum_id)
    return Clue.objects.get(id=random_id)
    

def drill(request):
    random_clue = random_selector()
    clue_length = len(random_clue.entry.entry_text)
    clue_puzzle = random_clue.puzzle.title
    return render(request, 'xword_data/drill.html', {'clue_length': clue_length, 'clue_puzzle': clue_puzzle})

def answer(request):
    return HttpResponse('Hello from answer')