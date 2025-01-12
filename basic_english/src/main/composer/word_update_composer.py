from basic_english.src.infrastructure.database.repositories.words_repository import WordsRepository
from basic_english.src.data.use_cases.word_update import WordUpdate
from basic_english.src.presentation.controllers.word_update_controller import WordUpdateController

def word_update_composer():
    repository = WordsRepository()
    use_case = WordUpdate(repository)
    controller = WordUpdateController(use_case)
    return controller.handle