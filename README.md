# Cert Check Script

## Overview
This script fetches data from a crt.sh and processes the entries to find SSL certificates registered within the last 30 days. It outputs the results into a JSON file, listing domains & sub-domains that have been registered or updated in the past month.

## Features
- **Data Fetching**: Retrieves data from a configurable URL. crt.sh doesn't have API documentation, however if you append "&output=json" to the end of the URL this formats the data into JSON objects for simplified, programatic interactions.
- **Date Filtering**: Filters entries to find domains registered or updated within the last 30 days.
- **Output**: Saves the filtered results into a JSON file in a readable format.

## Requirements
- Python 3.x
- `requests` library
- Internet connection to access the URL

## Configuration
Replace `[url_here]` in the script with the actual URL of the API endpoint you intend to query:
```python
url = "[url_here]"  # Replace [url_here] with the actual URL
```

## Usage
Run the script with Python from your terminal:
```bash
python crtsh.py
```

## Output
- The script generates a file named `domain_check_results.json` in the current directory, containing domains registered or updated within the last 30 days.
- If there is an error in fetching data, the script will output an error message indicating the HTTP status code and any additional error information.

## Error Handling
Errors in data fetching result in console output that describes the issue, typically related to network issues or access permissions for the API.