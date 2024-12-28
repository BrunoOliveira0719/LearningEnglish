from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.phrase_finder import PhraseFinder as PhraseFinderInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest 

class PhraseFinderAllTypePhraseController(ControllerInterface):
    def __init__ (self, use_case: PhraseFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            phrase = http_request.body["type_phrase"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'phrase'.")

        response = self.__use_case.find_all_type_phrase(phrase)

        return HttpResponse(status_code=200, body={"data": response})