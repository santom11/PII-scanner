'''
import os
from datetime import datetime

def write_html_report(original, anonymized, results, output_dir="output"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"report_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)

    # Build styled HTML
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PII Detection Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2C3E50; }}
        h2 {{ color: #34495E; margin-top: 30px; }}
        pre {{ background: #F8F8F8; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #DDD; padding: 10px; text-align: left; }}
        th {{ background-color: #2980B9; color: white; }}
        tr:nth-child(even) {{ background-color: #F2F2F2; }}
        .entity-label {{ font-weight: bold; color: #E74C3C; }}
    </style>
</head>
<body>
    <h1>🔒 PII Detection & Anonymization Report</h1>
    <p><em>Generated on: {datetime.utcnow().isoformat()} UTC</em></p>

    <h2>Original Text</h2>
    <pre>{original}</pre>

    <h2>Anonymized Text</h2>
    <pre>{anonymized}</pre>

    <h2>Detected PII Entities</h2>
    <table>
        <tr><th>Entity Type</th><th>Text</th><th>Confidence</th></tr>
        {''.join(f'<tr><td class="entity-label">{r.entity_type}</td><td>{original[r.start:r.end]}</td><td>{r.score:.2f}</td></tr>' for r in results)}
    </table>

    <h2>Entity Summary</h2>
    <ul>
        {''.join(f'<li><strong>{r.entity_type}</strong> at positions {r.start}-{r.end}</li>' for r in results)}
    </ul>

    <footer style="margin-top: 40px; font-size: 0.9em; color: #7F8C8D;">
        <p>Powered by Microsoft Presidio • Confidential & Proprietary</p>
    </footer>
</body>
</html>
"""
    # Write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath
'''

import os
from datetime import datetime
import json

def write_html_report(original, anonymized, results, output_dir="output"):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"report_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)

    # Prepare data for chart
    entity_counts = {}
    for r in results:
        entity_counts[r.entity_type] = entity_counts.get(r.entity_type, 0) + 1
    chart_data = json.dumps({
        'labels': list(entity_counts.keys()),
        'counts': list(entity_counts.values())
    })

    # Build styled HTML with Chart.js
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PII Detection Report</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; background: #fafafa; }}
    h1 {{ color: #2C3E50; }}
    h2 {{ color: #34495E; margin-top: 30px; }}
    pre {{ background: #F8F8F8; padding: 15px; border-radius: 5px; overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    th, td {{ border: 1px solid #DDD; padding: 10px; text-align: left; }}
    th {{ background-color: #2980B9; color: white; }}
    tr:nth-child(even) {{ background-color: #F2F2F2; }}
    .entity-label {{ font-weight: bold; }}
    .entity-row-PERSON {{ background-color: #fdecea; }}
    .entity-row-EMAIL {{ background-color: #eafaf1; }}
    .entity-row-INDIA_PAN {{ background-color: #fef9e7; }}
    /* Add more entity-specific colors as needed */
    footer {{ margin-top: 40px; font-size: 0.9em; color: #7F8C8D; }}
  </style>
</head>
<body>
  <h1>🔒 PII Detection & Anonymization Report</h1>
  <p><em>Generated on: {datetime.utcnow().isoformat()} UTC</em></p>

  <h2>Entity Distribution Chart</h2>
  <canvas id="entityChart" width="400" height="200"></canvas>
  <script>
    const ctx = document.getElementById('entityChart').getContext('2d');
    const chartInfo = {chart_data};
    new Chart(ctx, {{
      type: 'bar',
      data: {{
        labels: chartInfo.labels,
        datasets: [{{
          label: '# of Entities',
          data: chartInfo.counts,
          backgroundColor: [
            'rgba(231, 76, 60, 0.6)',
            'rgba(46, 204, 113, 0.6)',
            'rgba(241, 196, 15, 0.6)',
            'rgba(52, 152, 219, 0.6)',
            'rgba(155, 89, 182, 0.6)',
            'rgba(26, 188, 156, 0.6)'
          ],
          borderColor: [
            'rgba(231, 76, 60, 1)',
            'rgba(46, 204, 113, 1)',
            'rgba(241, 196, 15, 1)',
            'rgba(52, 152, 219, 1)',
            'rgba(155, 89, 182, 1)',
            'rgba(26, 188, 156, 1)'
          ],
          borderWidth: 1
        }}]
      }},
      options: {{ scales: {{ y: {{ beginAtZero: true }} }} }}
    }});
  </script>

  <h2>Original Text</h2>
  <pre>{original}</pre>

  <h2>Anonymized Text</h2>
  <pre>{anonymized}</pre>

  <h2>Detected PII Entities</h2>
  <table>
    <tr><th>Entity Type</th><th>Text</th><th>Confidence</th></tr>
    {''.join(f'<tr class="entity-row-{r.entity_type}"><td class="entity-label">{r.entity_type}</td><td>{original[r.start:r.end]}</td><td>{r.score:.2f}</td></tr>' for r in results)}
  </table>

  <h2>Entity Summary</h2>
  <ul>
    {''.join(f'<li><strong>{r.entity_type}</strong> at positions {r.start}-{r.end}</li>' for r in results)}
  </ul>

  <footer>
    <p>Powered by Microsoft Presidio • Confidential & Proprietary</p>
  </footer>
</body>
</html>
"""
    # Write file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath