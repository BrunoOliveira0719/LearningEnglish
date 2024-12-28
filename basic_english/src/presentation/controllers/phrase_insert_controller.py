from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.phrase_insert import PhraseInsert as PhraseInsertInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest 

class PhraseInsertController(ControllerInterface):
    def __init__ (self, use_case: PhraseInsertInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            phrase = http_request.body["phrase"]
            translation = http_request.body["translation"]
            formal = http_request.body["formal"]
            type_phrase = http_request.body["type_phrase"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'phrase' or 'translation' or 'formal' or 'type_phrase'.")

        response = self.__use_case.insert(phrase, translation, formal, type_phrase)

        return HttpResponse(status_code=200, body={"data": response})