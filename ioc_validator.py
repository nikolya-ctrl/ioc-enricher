import ipaddress


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