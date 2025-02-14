import re
import pandas as pd

# Define the log file path
log_file_path = "server.log"

# Define a regex pattern to extract structured information
log_pattern = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<log_level>INFO|ERROR|WARNING) "
    r"(?P<message>.+?) "
    r"(- (?P<details>.+))?"
)

# Read the log file and extract structured data
structured_data = []

with open(log_file_path, "r") as file:
    for line in file:
        match = log_pattern.match(line.strip())
        if match:
            structured_data.append(match.groupdict())

# Convert the structured data into a Pandas DataFrame
df = pd.DataFrame(structured_data)

# Display the first few rows
print(df.head())
