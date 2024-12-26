from typing import Dict

class PhraseUpdateSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def update(self, phrase_current: str, phrase: str, translation: str, formal: bool) -> Dict:
        phrases = self.find_attributes["phrase"] = phrase
        translations = self.find_attributes["translation"] = translation
        formals = self.find_attributes["formal"] = formal

        return {"type": "Phrases", "count": 1, "attributes": [
            {
                "phrase updated": phrase_current,
                "phrase current": phrases, "translation": f"{phrases}: {translations}", "formal": formals
            }
        ]}
