from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.word_delete import WordDelete as WordDeleteInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest
from abc import abstractmethod

class WordDeleteController(ControllerInterface):
    def __init__ (self, use_case: WordDeleteInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            word = http_request.body["word"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'word'.")

        response = self.__use_case.delete(word)

        response, status_code = self.__verification_response(response, word)

        return HttpResponse(status_code=status_code, body={"data": response})
    
    def __verification_response(cls, response, word):
        if cls.__verify(response):
            return response, 201
        return f"word: {word} deleted with success", 200

    def __verify(cls, response) -> bool:
        return response != True