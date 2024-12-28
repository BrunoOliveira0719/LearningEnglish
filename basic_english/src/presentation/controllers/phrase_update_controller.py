from basic_english.src.errors.types.http_not_found import HttpNotFound
from ..interfaces.controller_interface import ControllerInterface
from basic_english.src.domain.use_cases.phrase_update import PhraseUpdate as PhraseUpdateInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse
from typing import Dict

class PhraseUpdateController(ControllerInterface):
    def __init__ (self, use_case: PhraseUpdateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            phrase_current = http_request.body.get("phrase_current")
            phrase = http_request.body.get("phrase")
            translation = http_request.body.get("translation")
            formal = http_request.body.get("formal")
            type_phrase = http_request.body.get("type_phrase")

            if phrase_current == None or phrase_current == " ":
                return HttpNotFound(status_code=400, body={"error": "'phrase_current' not found."})

            response = self.__use_case.update(phrase_current, phrase, translation, formal, type_phrase)

        except Exception as exception:
            return HttpResponse(status_code=400, body={"error": str(exception)})

        return HttpResponse(status_code=200, body={"data": response})
