from typing import Dict

class PhraseFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, phrase: str) -> Dict:
        phrases = self.find_attributes["phrase"] = phrase

        return {"type": "Phrases", "count": 1, "attributes": [
            {
                "phrase": phrases, "translation": "Hello World!: Olá Mundo!", "formal": False
            }
        ]}
