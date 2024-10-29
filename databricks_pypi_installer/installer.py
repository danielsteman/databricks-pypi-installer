import subprocess
import sys
from databricks.sdk import WorkspaceClient
from databricks.sdk.dbutils import RemoteDbUtils


def get_workspace_client() -> WorkspaceClient:
    return WorkspaceClient()


def get_dbutils() -> RemoteDbUtils:
    workspace_client = get_workspace_client()
    return workspace_client.dbutils


def get_token(secret_name: str, secret_scope: str) -> str:
    dbutils = get_dbutils()
    secret = dbutils.secrets.get(secret_scope, secret_name)
    return secret


def install(package: str, extra_index_url: str | None = None) -> None:
    command = [sys.executable, "-m", "pip", "install", package]
    if extra_index_url:
        command.extend(["--extra-index-url", extra_index_url])
    subprocess.check_call(command)
