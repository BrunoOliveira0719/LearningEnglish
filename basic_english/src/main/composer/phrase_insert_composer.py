from basic_english.src.infrastructure.database.repositories.phrases_repository import PhrasesRepository
from basic_english.src.data.use_cases.phrase_insert import PhraseInsert
from basic_english.src.presentation.controllers.phrase_insert_controller import PhraseInsertController

def phrase_insert_composer():
    repository = PhrasesRepository()
    use_case = PhraseInsert(repository)
    controller = PhraseInsertController(use_case)
    return controller.handle