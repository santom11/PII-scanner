# PII Scanner (Presidio-Based)

A modular PII scanning and anonymization tool built in Python using Microsoft Presidio. Designed to start with unstructured `.txt` files and scale to PDF/CSV/Confluence inputs later.

## Run CLI:
```bash
python main.py --input testdata/sample_banking_input.txt --output output/output_result.json
```

## Output
- Anonymized text
- JSON report with entity details

---

Future Development:
- Add Flask or Gradio API (`api_app.py`)
- Add PDF/CSV readers under `plugins/`
- Add logging, metrics, test coverage