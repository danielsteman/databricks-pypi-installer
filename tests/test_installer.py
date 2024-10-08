from databricks_pypi_installer.installer import install


def test_installer() -> None:
    install("numpy")
