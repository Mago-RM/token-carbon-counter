import tiktoken

encoding = tiktoken.get_encoding("o200k_base")

print()
prompt = input("Enter a prompt: ")
wc = prompt.split()
words = len(wc)
tokens = encoding.encode(prompt)

print()
print("Number of Tokens in this Prompt: "+ str(len(tokens)))

#Too Much text
if len(tokens) > 500:
    print(f"⚠️ Warning: High token count. Check for redundant constraints.")

#Repetitive words
for i in range(words-1):
    if wc[i] == wc[i+1]:
        print(f"⚠️ Warning: Repetitive words. Check for redundant constraints.")
        break
    

#rep Characters. Go word for worf..go char by char INSIDE word
flag = False
for word in wc:
    if not flag:
        for i in range(len(word)-2):
            if word[i]==word[i+1]==word[i+1+1]:
                print(f"⚠️ Warning: Repetitive characters. Check for redundant constraints.")
                flag = True
                break

print()
# Model Price
print("Model selected:  OpenAi GPT-5.6 Luna")
print("Date consulted: October 6th, 2026")
print("Input Price: $0.20 per 1,000,000 tokens")
price = (0.20/1000000)*len(tokens)
print(f"The price for this prompt is: ${price:.8f}")

print()
#co2 Waste
print("CO₂ assumption: 0.5 mg per token")
co2 = 0.5*len(tokens)
print("Estimated CO2 cost: " +str(co2) +"mg")

print()
print("Tokens: ")
for token in tokens:
    print(token, encoding.decode([token]))

