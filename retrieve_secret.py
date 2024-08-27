from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault URL
key_vault_url = "https://secrets23.vault.azure.net/"

# Create a credential using the default managed identity
credential = DefaultAzureCredential()

# Create a Key Vault client
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Use the name of your secret
secret_name = "aswin2"

# Retrieve the secret from Key Vault
try:
    secret = client.get_secret(secret_name)
    print(f"Secret value: {secret.value}")
except ResourceNotFoundError:
    print(f"Secret '{secret_name}' not found in Key Vault.")
except HttpResponseError as e:
    print(f"An error occurred: {e.message}")
