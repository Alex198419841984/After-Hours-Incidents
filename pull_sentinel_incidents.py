import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.security import SecurityCenter

# Authenticate
credential = DefaultAzureCredential()
client = SecurityCenter(credential, subscription_id=os.getenv('AZURE_SUBSCRIPTION_ID'))

# Pull incidents
incidents = client.incidents.list(resource_group_name='YourResourceGroup', workspace_name='YourWorkspaceName')

# Save incidents to a CSV file
with open('incidents_report.csv', 'w') as file:
    for incident in incidents:
        file.write(f"{incident.name},{incident.properties.title},{incident.properties.severity}\n")
