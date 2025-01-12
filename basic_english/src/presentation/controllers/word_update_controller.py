from basic_english.src.errors.types.http_not_found import HttpNotFound
from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.word_update import WordUpdate as WordUpdateInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from typing import Dict

class WordUpdateController(ControllerInterface):
    def __init__ (self, use_case: WordUpdateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            word_current = http_request.body.get("word_current")
            word = http_request.body.get("word")
            translation = http_request.body.get("translation")
            formal = http_request.body.get("formal")
            type_word = http_request.body.get("type_word")

            if word_current == None or word_current == " ":
                return HttpNotFound(status_code=400, body={"error": "'word_current' not found."})

            response = self.__use_case.update(word_current, word, translation, formal, type_word)

        except Exception as exception:
            return HttpResponse(status_code=400, body={"error": str(exception)})

        return HttpResponse(status_code=200, body={"data": response})
