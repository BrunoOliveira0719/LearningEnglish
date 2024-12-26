from .phrase_update_controller import PhraseUpdateController
from basic_english.src.data.tests.phrase_update import PhraseUpdateSpy
from ..http_types.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"phrase_current": "Hello World!", "phrase": "Hello People!", "translation": "Olá Mundo!", "formal": False}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PhraseUpdateSpy()
    phrase_update_controler = PhraseUpdateController(use_case)

    handle_response = phrase_update_controler.handle(http_request_mock)
    print()
    print()
    print(handle_response.body)
    print(handle_response.status_code)

    assert isinstance(handle_response, HttpResponse)
    assert handle_response.status_code == 200
    assert handle_response.body["data"] is not None and type(handle_response.body["data"]) is dict