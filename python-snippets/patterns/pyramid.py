def pyramid(symbol, rows):
    for i in range(rows):
      print(symbol * (i+1))
pyramid("?", 10)