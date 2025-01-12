from basic_english.src.infrastructure.database.repositories.words_repository import WordsRepository
from basic_english.src.data.use_cases.word_insert import WordInsert
from basic_english.src.presentation.controllers.word_insert_controller import WordInsertController

def word_insert_composer():
    repository = WordsRepository()
    use_case = WordInsert(repository)
    controller = WordInsertController(use_case)
    return controller.handle