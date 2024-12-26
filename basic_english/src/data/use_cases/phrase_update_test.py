from basic_english.src.infrastructure.database.tests.phrases_repository import PhrasesRepositorySpy
from .phrase_update import PhraseUpdate

def test_update_phrase():
    phrase_courrent = "What's up?"

    repo = PhrasesRepositorySpy()
    user_update = PhraseUpdate(repo)

    response = user_update.update(phrase_courrent, phrase="What's new?")

    print(f"\n{response}")