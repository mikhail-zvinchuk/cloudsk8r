import os

from azure.storage.blob import BlobServiceClient


class AzureAdapter:

    @staticmethod
    def get_azure_blob_client(account_base_link=None, access_key=None):
        if account_base_link is None:
            account_base_link = os.environ.get('account_base_link')
        if access_key is None:
            access_key = os.environ.get('access_key')
            # Should there be error handling here?

        return BlobServiceClient(account_url=account_base_link, credential=access_key)

    @staticmethod
    def list_containers(client: BlobServiceClient):
        container_list = client.list_containers()
        for container in container_list:
            print(container.name)
