import pytest
import yaml

def test_environment_setup():
    """
    A foundational test to verify that the environment, pytest,
    and required tools (like PyYAML) are working as expected.
    """
    sample_yaml = """
    status: running
    environment: ci-pipeline
    """
    data = yaml.safe_load(sample_yaml)
    
    assert data["status"] == "running"
    assert data["environment"] == "ci-pipeline"
