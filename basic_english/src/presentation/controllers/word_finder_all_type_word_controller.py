from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.word_finder import WordFinder as WordFinderInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from basic_english.src.errors.types import HttpBadRequest 

class WordFinderAllTypeWordController(ControllerInterface):
    def __init__ (self, use_case: WordFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            word = http_request.body["type_word"]

        except KeyError:
            HttpBadRequest("The attribute input not is 'word'.")

        response = self.__use_case.find_all_type_word(word)
        print(response)

        return HttpResponse(status_code=200, body={"data": response})