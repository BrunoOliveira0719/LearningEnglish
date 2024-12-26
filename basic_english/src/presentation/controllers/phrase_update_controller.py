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
            phrase_current = http_request.body["phrase_current"]
            phrase = http_request.body["phrase"]
            translation = http_request.body["translation"]
            formal = http_request.body["formal"]

        except KeyError:
            if phrase_current != None and phrase_current != " ":
                if "phrase" not in http_request.body or not http_request.body["phrase"]:
                    phrase = None
                if "translation" not in http_request.body or not http_request.body["translation"]:
                    translation = None
                if "formal" not in http_request.body or not http_request.body["formal"]:
                    formal = None
            else:
                return HttpNotFound(status_code=400, body={"error": "'phrase_current' not found or Parameters invalids 'KeyError'."})

            response = self.__use_case.update(phrase_current, phrase, translation, formal)
        
        return HttpResponse(status_code=200, body={"data": response})
