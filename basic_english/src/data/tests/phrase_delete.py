from typing import Dict

class PhraseDeleteSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def delete(self, phrase: str) -> Dict:
        phrases = self.find_attributes["phrase"] = phrase

        return {"type": "Phrases", "count": 0, "attributes": [
            {

            }
        ]}
