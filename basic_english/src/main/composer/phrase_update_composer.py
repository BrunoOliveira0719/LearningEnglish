from basic_english.src.infrastructure.database.repositories.phrases_repository import PhrasesRepository
from basic_english.src.data.use_cases.phrase_update import PhraseUpdate
from basic_english.src.presentation.controllers.phrase_update_controller import PhraseUpdateController

def phrase_update_composer():
    repository = PhrasesRepository()
    use_case = PhraseUpdate(repository)
    controller = PhraseUpdateController(use_case)
    return controller.handle