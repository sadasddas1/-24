sym = 4
sym_in_line = 25
string = 50
book = 100
dics = 1.44

line = sym_in_line * sym
line_in_page = line * string
page_in_book = line_in_page * book

mb = dics * 1024 * 1024
total = mb//page_in_book

#print(page_in_book)
#print (mb)
#print(total)

print("Количество книг, помещающихся на дискету:", round(total),)
