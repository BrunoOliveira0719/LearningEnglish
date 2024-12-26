from .phrase_delete_controller import PhraseDeleteController
from basic_english.src.data.tests.phrase_delete import PhraseDeleteSpy
from ..http_types.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"phrase": "What's up?"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PhraseDeleteSpy()
    phrase_finder_controler = PhraseDeleteController(use_case)

    handle_response = phrase_finder_controler.handle(http_request_mock)
    print()
    print()
    print(handle_response.body)
    print(handle_response.status_code)

    assert isinstance(handle_response, HttpResponse)