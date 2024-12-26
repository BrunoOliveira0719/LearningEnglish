from basic_english.src.infrastructure.database.repositories.phrases_repository import PhrasesRepository
from basic_english.src.data.use_cases.phrase_delete import PhraseDelete
from basic_english.src.presentation.controllers.phrase_delete_controller import PhraseDeleteController

def phrase_delete_composer():
    repository = PhrasesRepository()
    use_case = PhraseDelete(repository)
    controller = PhraseDeleteController(use_case)
    return controller.handle