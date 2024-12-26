from basic_english.src.infrastructure.database.repositories.phrases_repository import PhrasesRepository
from basic_english.src.data.use_cases.phrase_finder import PhraseFinder
from basic_english.src.presentation.controllers.phrase_finder_all_controller import PhraseFinderAllController

def phrase_finder_all_composer():
    repository = PhrasesRepository()
    use_case = PhraseFinder(repository)
    controller = PhraseFinderAllController(use_case)
    return controller.handle