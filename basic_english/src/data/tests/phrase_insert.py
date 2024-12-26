from typing import Dict

class PhraseInsertSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def insert(self, phrase: str, translation: str, formal: bool) -> Dict:
        phrases = self.find_attributes["phrase"] = phrase
        translations = self.find_attributes["translation"] = translation
        formals = self.find_attributes["formal"] = formal

        return {"type": "Phrases", "count": 1, "attributes": [
            {
                "phrase": phrases, "translation": f"{phrases}: {translations}", "formal": formals
            }
        ]}
