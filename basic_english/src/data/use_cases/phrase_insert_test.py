from basic_english.src.infrastructure.database.tests.phrases_repository import PhrasesRepositorySpy
from .phrase_insert import PhraseInsert

def test_insert_phrase():
    phrase = "What's up?"
    translation = "What's up?: E aí?!"
    formal = False

    repo = PhrasesRepositorySpy()
    user_insert = PhraseInsert(repo)

    response = user_insert.insert(phrase, translation, formal)

    print(f"\n{response}")
    print()
    print(repo.insert_phrase_attributes)
    print()
    print(repo.insert_phrase_attributes["phrase"] == phrase)
    print(repo.insert_phrase_attributes["translation"] == translation)
    print(repo.insert_phrase_attributes["formal"] == formal)