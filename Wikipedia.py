import wikipedia
inp=input("emter any word that you want to search : \n ")
query=wikipedia.page(inp)
print(query.summary)