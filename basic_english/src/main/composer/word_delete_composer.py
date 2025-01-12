from basic_english.src.infrastructure.database.repositories.words_repository import WordsRepository
from basic_english.src.data.use_cases.word_delete import WordDelete
from basic_english.src.presentation.controllers.word_delete_controller import WordDeleteController

def word_delete_composer():
    repository = WordsRepository()
    use_case = WordDelete(repository)
    controller = WordDeleteController(use_case)
    return controller.handle