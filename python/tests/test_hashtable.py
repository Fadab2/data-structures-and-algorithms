
from code_challenges.hashtable.hashtable import HashTable

def test_set_key_value_function():
    hashed = HashTable()
    hashed.set("apple", "juicy")

    assert hashed.get("apple") == "juicy"


def test_get_non_existent_key():
    hashed = HashTable()
    hashed.set("apple", "juicy")

    assert hashed.get("cat") == None


def test_contains_an_existent_key():
    hashed = HashTable()
    hashed.set("apple", "juicy")

    assert hashed.get("apple") == True


def test_get_all_unique_keys():
    hashed = HashTable()
    hashed.set("apple", "juicy")
    hashed.set("strawberry", "red")
    hashed.set("lime", "green")

    assert hashed.keys() == None
