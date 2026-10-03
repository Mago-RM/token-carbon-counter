import tiktoken

encoding = tiktoken.get_encoding("o200k_base")

prompt = input("Enter a prompt: ")

tokens = encoding.encode(prompt)

print(len(tokens))
print("Tokens: ")
for token in tokens:
    print(token, encoding.decode([token]))