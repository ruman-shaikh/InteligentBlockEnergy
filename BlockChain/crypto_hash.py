import hashlib

def crypto_hash(data):
    """
    Return a sha-256 hash of the given data
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('test'): {crypto_hash('test')}")

if __name__ == '__main__':
    main()