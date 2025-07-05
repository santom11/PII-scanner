import argparse
from core.reader_text import read_text_file
from core.analyzer import TextAnalyzer
from core.anonymizer import TextAnonymizer
from core.writter_json import write_output


def main():
    parser = argparse.ArgumentParser(description="PII Scanner CLI")
    parser.add_argument("--input", required=True, help="Input .txt file")
    parser.add_argument("--output", default="output/output_result.json", help="Output file path")
    args = parser.parse_args()

    raw_text = read_text_file(args.input)
    analyzer = TextAnalyzer()
    anonymizer = TextAnonymizer()

    analysis_results = analyzer.analyze(raw_text)
    anonymized_text = anonymizer.anonymize(raw_text, analysis_results)

    write_output(args.input, raw_text, anonymized_text, analysis_results, args.output)


if __name__ == "__main__":
    main()