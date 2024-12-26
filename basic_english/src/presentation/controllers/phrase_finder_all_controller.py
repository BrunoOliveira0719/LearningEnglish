from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.phrase_finder import PhraseFinder as PhraseFinderInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse

class PhraseFinderAllController(ControllerInterface):
    def __init__ (self, use_case: PhraseFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.__use_case.find_all()

        return HttpResponse(status_code=200, body={"data": response})