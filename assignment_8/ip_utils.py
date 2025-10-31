# ip_utils.py

def ip_to_binary(ip_address: str) -> str:
    """Convert dotted-decimal IP (e.g. 192.168.1.1) to 32-bit binary string."""
    octets = ip_address.split(".")
    return "".join([format(int(o), "08b") for o in octets])


def get_network_prefix(ip_cidr: str) -> str:
    """Return binary network prefix from CIDR notation (e.g. 200.23.16.0/23)."""
    ip, prefix_len = ip_cidr.split("/")
    prefix_len = int(prefix_len)
    binary_ip = ip_to_binary(ip)
    return binary_ip[:prefix_len]


# Example test
if __name__ == "__main__":
    print(ip_to_binary("192.168.1.1"))
    print(get_network_prefix("200.23.16.0/23"))
