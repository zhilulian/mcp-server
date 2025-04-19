import os

from dotenv import load_dotenv

class TlsConfig:

    ak: str
    sk: str
    region: str
    endpoint: str
    token: str
    project_id: str
    account_id: str
    enabled_tools: list

    def __init__(self):
        self.ak = os.getenv("AK") or os.getenv("VOLC_ACCESSKEY")
        self.sk = os.getenv("SK") or os.getenv("VOLC_SECRETKEY")
        self.region = os.getenv("REGION")
        self.endpoint = os.getenv("ENDPOINT")
        self.token = os.getenv("TOKEN", "")
        self.project_id = os.getenv("PROJECT_ID")
        self.topic_id = os.getenv("TOPIC_ID")
        self.account_id = os.getenv("ACCOUNT_ID")

        self.enabled_tools = os.getenv("ENABLED_TOOLS", "all").split(",")

        self._validate()

    def _validate(self):
        self._validateAK()
        self._validateSK()
        self._validateRegion()
        self._validateEndpoint()

    def _validateAK(self):
        if not self.ak:
            raise ValueError("environment variables AK is required")

    def _validateSK(self):
        if not self.sk:
            raise ValueError("environment variables SK is required")

    def _validateRegion(self):
        if not self.region:
            raise ValueError("environment variables REGION is required")

    def _validateEndpoint(self):
        if not self.endpoint:
            raise ValueError("environment variables ENDPOINT is required")
        if not (self.endpoint.startswith("http://") or self.endpoint.startswith("https://")):
            raise ValueError(f"Invalid environment variables endpoint: {self.endpoint}. It must start with 'http://' or 'https://'.")


load_dotenv()

TLS_CONFIG = TlsConfig()