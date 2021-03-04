from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    #It should create the same hash for any order of the same agruments
    assert crypto_hash(2, "three", [1]) == crypto_hash([1], 2, "three")
    