from basic_english.src.infrastructure.database.repositories.phrases_repository import PhrasesRepository
from basic_english.src.data.use_cases.phrase_finder import PhraseFinder
from basic_english.src.presentation.controllers.phrase_finder_all_type_phrase_controller import PhraseFinderAllTypePhraseController

def finder_all_type_phrase_composer():
    repository = PhrasesRepository()
    use_case = PhraseFinder(repository)
    controller = PhraseFinderAllTypePhraseController(use_case)
    return controller.handle