import ipaddress
import re

def is_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def is_public_ip(value):
    try:
        ip = ipaddress.ip_address(value)
        return ip.is_global
    except ValueError:
        return False

def is_sha256(value):
    return re.fullmatch(r"[a-fA-F0-9]{64}", value) is not None

def refang(value):
    return value.strip().replace("[.]", ".")