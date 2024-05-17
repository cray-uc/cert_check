import requests
import json
from datetime import datetime, timedelta

url = "[url_here]"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current_date = datetime.now()
    thirty_days_ago = current_date - timedelta(days=30)

    domain_check_results = []

    for entry in data:
        common_name = entry.get('common_name')
        entry_timestamp_str = entry.get('entry_timestamp')

        if common_name and entry_timestamp_str:
            entry_timestamp = datetime.fromisoformat(entry_timestamp_str.replace('T', ' '))

            if entry_timestamp >= thirty_days_ago:
                domain_info = {
                    'common_name': common_name,
                    'entry_timestamp': entry_timestamp.isoformat()
                }
                domain_check_results.append(domain_info)

    with open('domain_check_results.json', 'w') as json_file:
        json.dump(domain_check_results, json_file, indent=4)

else:
    print(f"Error: {response.status_code} - {response.text}")