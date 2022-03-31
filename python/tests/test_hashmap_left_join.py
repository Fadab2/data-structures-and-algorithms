from code_challenges.hashmap_left_join.hashmap_left_join import left_join


def test_complet_list():
    hash1 = {
        'diligent': 'employed',
        'fond': 'enamored',
        'wrath': 'anger',
        'outfit': 'garb',
    }
    hash2 = {
        'diligent': 'idle',
        'fond': 'averse',
        'wrath': 'delight',
        'flow': 'jam',
    }

    actual = left_join(hash1, hash2)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], [
        'wrath', 'anger', 'delight'], ['outfit', 'garb', None]]
    
    assert actual == expected


def test_empty_hashmaps():
    hash1 = {

    }
    hash2 = {

    }

    actual = left_join(hash1, hash2)
    expected = []
    assert actual == expected
