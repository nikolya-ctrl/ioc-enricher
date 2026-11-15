from ioc_validator import is_public_ip


def test_google_dns_is_public():
    assert is_public_ip("8.8.8.8") == True


def test_private_ip_is_not_public():
    assert is_public_ip("192.168.1.10") == False