import pytest
import random
import string
from seam import Seam
from seam.auth import SeamHttpInvalidTokenError
from test.constants import TEST_API_KEY


def test_seam_client_from_api_key_returns_instance_authorized_with_api_key(
    test_endpoint,
):
    seam = Seam.from_api_key(TEST_API_KEY, endpoint=test_endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


def test_seam_client_constructor_returns_instance_authorized_with_api_key(
    test_endpoint,
):
    seam = Seam(api_key=TEST_API_KEY, endpoint=test_endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


def test_seam_client_constructor_interprets_single_string_argument_as_api_key():
    seam = Seam(TEST_API_KEY)

    assert seam is not None

    with pytest.raises(SeamHttpInvalidTokenError, match=r"api_key"):
        Seam(api_key="some-invalid-key-format")


def test_seam_client_checks_api_key_format():
    with pytest.raises(SeamHttpInvalidTokenError, match=r"Unknown"):
        Seam.from_api_key("some-invalid-key-format")

    with pytest.raises(SeamHttpInvalidTokenError, match=r"JWT"):
        Seam.from_api_key("ey")

    with pytest.raises(SeamHttpInvalidTokenError, match=r"Client Session Token"):
        Seam.from_api_key("seam_cst_token")

    with pytest.raises(SeamHttpInvalidTokenError, match=r"Access Token"):
        Seam.from_api_key("seam_at")
