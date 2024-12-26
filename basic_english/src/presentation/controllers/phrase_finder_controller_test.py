from .phrase_finder_controller import PhraseFinderController
from basic_english.src.data.tests.phrase_finder import PhraseFinderSpy
from ..http_types.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"phrase": "Hello World!"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PhraseFinderSpy()
    phrase_finder_controler = PhraseFinderController(use_case)

    handle_response = phrase_finder_controler.handle(http_request_mock)
    print()
    print()
    print(handle_response.body)
    print(handle_response.status_code)

    assert isinstance(handle_response, HttpResponse)
    assert handle_response.status_code == 200
    assert handle_response.body["data"] is not None and type(handle_response.body["data"]) is dict