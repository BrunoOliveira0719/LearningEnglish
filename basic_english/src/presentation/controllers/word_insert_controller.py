from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.word_insert import WordInsert as WordInsertInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest 

class WordInsertController(ControllerInterface):
    def __init__ (self, use_case: WordInsertInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            word = http_request.body["word"]
            translation = http_request.body["translation"]
            formal = http_request.body["formal"]
            type_word = http_request.body["type_word"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'word' or 'translation' or 'formal' or 'type_word'.")

        response = self.__use_case.insert(word, translation, formal, type_word)

        return HttpResponse(status_code=200, body={"data": response})