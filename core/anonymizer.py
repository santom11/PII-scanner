from presidio_anonymizer import AnonymizerEngine

class TextAnonymizer:
    def __init__(self):
        self.anonymizer = AnonymizerEngine()

    def anonymize(self, text, analyzer_results):
        result = self.anonymizer.anonymize(text=text, analyzer_results=analyzer_results)
        return result.text