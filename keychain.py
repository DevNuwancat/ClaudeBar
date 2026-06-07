import keyring

SERVICE_NAME = "Claude Bar"
USERNAME = "session_token"

# Save token 
def save_token(token:str):
    keyring.set_password(SERVICE_NAME, USERNAME, token)

# Load Token 
def get_token():
    return keyring.get_password(SERVICE_NAME, USERNAME)

# Delete Token 
def delete_token():
    try:
        keyring.delete_password(SERVICE_NAME, USERNAME)
    except keyring.errors.PasswordDeleteError:
        pass