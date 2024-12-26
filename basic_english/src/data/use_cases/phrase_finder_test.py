import pytest
from basic_english.src.infrastructure.database.tests.phrases_repository import PhrasesRepositorySpy
from .phrase_finder import PhraseFinder

def test_find_phrase():
    phrase = "What's up?"
    
    repo = PhrasesRepositorySpy()
    user_finder = PhraseFinder(repo)

    response2 = user_finder.find(phrase)

    print()
    print(response2)
    print()

def test_find_all_phrase():

    repo = PhrasesRepositorySpy()
    user_finder = PhraseFinder(repo)

    response2 = user_finder.find_all()

    print()
    print(response2)