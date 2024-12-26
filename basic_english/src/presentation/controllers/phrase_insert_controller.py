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

        except KeyError:
            HttpBadRequest("The attribute input not is 'phrase' or 'translation' or 'formal'.")

        response = self.__use_case.insert(phrase, translation, formal)

        return HttpResponse(status_code=200, body={"data": response})