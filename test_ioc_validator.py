from ioc_validator import is_public_ip, is_sha256


def test_google_dns_is_public():
    assert is_public_ip("8.8.8.8") == True


def test_private_ip_is_not_public():
    assert is_public_ip("192.168.1.10") == False


def test_real_sha256_is_detected():
    assert is_sha256("1F1F8EB800EE0FC11271C2B3D60E44A317368B1C269868405BC4C258E0051871") == True


def test_YOUR_NAME_HERE():
    assert is_sha256("YOUR-NOT-A-HASH-EXAMPLE") == False