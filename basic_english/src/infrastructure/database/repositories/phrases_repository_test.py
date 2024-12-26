from .phrases_repository import PhrasesRepository
import pytest

@pytest.mark.skip(reason="Sensive test")
def test_insert_phrase():
    mocked_phrase = "What's up?"
    mocked_translation = "What's up?: E aí?!"
    mocked_formal = False

    phrases_repository = PhrasesRepository()
    phrases_repository.insert_phrase(mocked_phrase, mocked_translation, mocked_formal)

    print(phrases_repository.read_specific_phrase(mocked_phrase))

@pytest.mark.skip(reason="Sensive test")
def test_read_specific_phrase():
    mocked_phrase = "What's up?"

    phrases_repository = PhrasesRepository()
    response = phrases_repository.read_specific_phrase(mocked_phrase)
    response = f"\n{response}"

    print(response)
    return response

@pytest.mark.skip(reason="Sensive test")
def test_read_all_phrases():
    phrases_repository = PhrasesRepository()
    response = phrases_repository.read_all_phrases()
    response = f"\n{response}"

    print(response)
    return response

@pytest.mark.skip(reason="Sensive test")
def test_update_phrase():
    mocked_phrase = "What's up?"
    mocked_translation = "What's up?: E aí?!"
    mocked_formal = False

    phrases_repository = PhrasesRepository()
    phrases_repository.update_phrase(mocked_phrase, mocked_translation, mocked_formal)

    print(phrases_repository.read_specific_phrase(mocked_phrase))

@pytest.mark.skip(reason="Sensive test")
def test_delete_phrase():
    mocked_phrase = "What's up?"

    phrases_repository = PhrasesRepository()
    phrases_repository.delete_phrase(mocked_phrase)

    print(phrases_repository.read_specific_phrase(mocked_phrase))