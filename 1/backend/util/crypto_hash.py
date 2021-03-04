import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given agruments
    """

    str_data = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(str_data)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(crypto_hash([1, 'test', [3]]))

if __name__ == "__main__":
    main()