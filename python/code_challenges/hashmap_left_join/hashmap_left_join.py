
def left_join(hash1, hash2):
    build = []
    output = []

    for key in hash1:
        build = [key, hash1.get(key), hash2.get(key)]

        output.append(build)
    return output

# test code
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

output = left_join(hash1, hash2)

print(output)
