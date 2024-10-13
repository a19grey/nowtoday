import sys
import base64
import io
import pandas as pd
import boto3
from bokeh.plotting import figure
from bokeh.io import export_png

sql_query = sys.argv[1]

# Connect to Amazon Redshift via Tailscale VPN
redshift = boto3.client('redshift-data', region_name='us-east-1')

# Execute the SQL query
response = redshift.execute_statement(
    ClusterIdentifier='dc2-2',
    Database='trace',
    Sql=sql_query
)

# Fetch the result rows
result_id = response['Id']
result_response = redshift.get_statement_result(Id=result_id)
records = result_response['Records']

# Convert records to pandas DataFrame
data = []
for record in records:
    row = [value.get('stringValue') or value.get('longValue') for value in record]
    data.append(row)

columns = [metadata['name'] for metadata in result_response['ColumnMetadata']]
df = pd.DataFrame(data, columns=columns)

# Generate chart using Bokeh
p = figure(title="Sample Chart", x_axis_label='x', y_axis_label='y')
p.line(df[df.columns[0]], df[df.columns[1]], legend_label='Data', line_width=2)

# Save chart to in-memory byte buffer
buffer = io.BytesIO()
export_png(p, filename=buffer)
buffer.seek(0)

# Encode the image in base64
image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
print(image_base64)