import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")
    test_hash = crypto_hash(
        1620400961497200700,
        "genesis_hash",
        "[{'id': '6001a2e2', 'input': {'address': '*--official-mining-reward--*'}, 'output': {'0e6cc277': 50}}]",
        2,
        1
        )
    print(f"crypto_hash {test_hash}")

if __name__ == '__main__':
    main()
