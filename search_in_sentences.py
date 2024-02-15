sentence = "The quick brown fox jumped over the lazy dog"

query_one = sentence.find("brows")
query_two = sentence.index("brown")
query_three = "fox" in sentence

print(query_one)
print(query_two)
print(query_three)

sentence_two = sentence.replace("fox", "cat")

print(sentence_two)