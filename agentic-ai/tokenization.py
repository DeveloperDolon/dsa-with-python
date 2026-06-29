import tiktoken;

enc = tiktoken.encoding_for_model("gpt-4o");

text = "Hey There! My name is Dolon Roy";

tokens = enc.encode(text);
print(f"Tokens: {tokens}")

decoded = enc.decode(tokens);
print("Decoded: ", decoded)