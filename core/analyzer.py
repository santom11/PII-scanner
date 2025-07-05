from presidio_analyzer import AnalyzerEngine, PatternRecognizer, RecognizerRegistry, Pattern
import yaml

class TextAnalyzer:
    def __init__(self, config_path="config/pii_patterns.yaml"):
        self.registry = RecognizerRegistry()
        self._load_patterns(config_path)
        self.analyzer = AnalyzerEngine(registry=self.registry)

    def _load_patterns(self, config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        for entry in config['patterns']:
            pattern_obj = Pattern(name=entry['name'], regex=entry['regex'], score=entry.get('score', 0.85))
            recognizer = PatternRecognizer(
                supported_entity=entry['name'],
                patterns= [pattern_obj]
            )
            self.registry.add_recognizer(recognizer)

    def analyze(self, text, language='en'):
        return self.analyzer.analyze(text=text, language=language)