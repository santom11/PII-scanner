import json
from datetime import datetime

def write_output(input_path, original_text, anonymized_text, analysis_results, output_path):
    output = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_file": input_path,
        "detected_entities": [
            {
                "entity_type": r.entity_type,
                "start": r.start,
                "end": r.end,
                "score": r.score,
                "text": original_text[r.start:r.end]
            } for r in analysis_results
        ],
        "anonymized_text": anonymized_text
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)