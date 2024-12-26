from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.phrase_delete import PhraseDelete as PhraseDeleteInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest
from abc import abstractmethod

class PhraseDeleteController(ControllerInterface):
    def __init__ (self, use_case: PhraseDeleteInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            phrase = http_request.body["phrase"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'phrase'.")

        response = self.__use_case.delete(phrase)

        response, status_code = self.__verification_response(response, phrase)

        return HttpResponse(status_code=status_code, body={"data": response})
    
    def __verification_response(cls, response, phrase):
        if cls.__verify(response):
            return response, 201
        return f"phrase: {phrase} deleted with success", 200

    def __verify(cls, response) -> bool:
        return response != True