programming_words = {
    'variable': 'Place where data is stored.',
    'keywords': 'reserved words.',
    'interpreter': 'translates one statement to machine code at a time.',
    'ram': 'primary memory.',
    'print': 'used to print statements.',
}

# looping using key,value pair in a dictionary
for key,value in sorted(programming_words.items()):
    print(f"{key}: {value}")


programming_words['compiler'] = 'translates whole block of code at a time.'
programming_words['api'] = 'bridge to connect a machine to programmer.'
programming_words['python'] = 'simple and easy to learn high-level ' \
                              'programming language.'
programming_words['chatgpt'] = 'conversation AI.'
programming_words['constant'] = 'variable whose value cannot be altered.'

print(f"\nThe modified Glossary is as follows:")
for key,value in sorted(programming_words.items()):
    print(f"{key}: {value}")