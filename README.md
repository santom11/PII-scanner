# PII Scanner (Presidio-Based)

A modular PII scanning and anonymization tool built in Python using Microsoft Presidio. Designed for unstructured `.txt` files

### 1. Command-Line Scanner
## Run CLI:
```bash
python3 main.py --input testdata/sample_banking_input.txt --output output/output_result.json
```
- `--input`: Path to source `.txt` file
- `--output`: Path for JSON report (default `output/output_result.json`)
## Output
- Anonymized text
- JSON report with entity details

---

### 2. REST API Service

1. **Start the Flask API**
   ```bash
   python api_app.py
   ```
   
2. **Send a curl command**
    ```commandline
    curl -X POST http://localhost:5000/analyze   -H "Content-Type: application/json"   -d '{"text": "Rahul Mehta, PAN: APLPM4356H, Phone: +91-9876543210"}'
    ```

3. **Retrieve HTML report**
   - Response includes `report_url`, e.g. `/report/report_20250705120000.html`
   - Open in browser:
   ```
   http://localhost:5000/report/report_20250705120000.html
   ```