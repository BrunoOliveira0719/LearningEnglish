from basic_english.src.infrastructure.database.repositories.words_repository import WordsRepository
from basic_english.src.data.use_cases.word_finder import WordFinder
from basic_english.src.presentation.controllers.word_finder_all_type_word_controller import WordFinderAllTypeWordController

def finder_all_type_word_composer():
    repository = WordsRepository()
    use_case = WordFinder(repository)
    controller = WordFinderAllTypeWordController(use_case)
    return controller.handle