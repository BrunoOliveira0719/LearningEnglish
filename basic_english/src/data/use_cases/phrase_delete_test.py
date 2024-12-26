from basic_english.src.infrastructure.database.tests.phrases_repository import PhrasesRepositorySpy
from .phrase_delete import PhraseDelete

def test_delete_phrase():
    phrase_courrent = "What's up?"

    repo = PhrasesRepositorySpy()
    user_update = PhraseDelete(repo)

    response = user_update.delete(phrase_courrent)

    print(f"\n{response}")