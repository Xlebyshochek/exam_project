import pytest


@pytest.fixture(scope="module")
def notification():
    print("Start test")
    yield
    print("Finish test")
