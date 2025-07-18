#01
# rc= int(input())
# pos = -1
# matrix = True
# for i in range(rc * 2):
#     e = int(input())
#     if (e == 1  and pos == -1):
#         pos = i
        
#     elif (e == 1):
#         if ( abs(pos -  (i % rc)) == 1 ):
#             pos = abs(i % rc)
#         else:
#             matrix = False
#             break

# if (matrix):
#     print("Matriz identidad")

# else:
#     print("Matriz no identidad")

#02
# rc= int(input())
# pos = -1
# matrix = True
# for i in range(rc * 2):
#     e = int(input())
#     if (e != 0  and pos == -1):
#         pos = i
        
#     elif (e != 0):
#         if ( abs(pos -  (i % rc)) == 1 ):
#             pos = abs(i % rc)
#         else:
#             matrix = False
#             break

# if (matrix):
#     print("Matriz diagonal")

# else:
#     print("Matriz no diagonal")

#03
# rc= int(input())
# pos = -1
# num = -1
# matrix = True
# for i in range(rc * rc):
#     e = int(input())
#     if (e != 0  and pos == -1):
#         pos = i
#         num = e
        
#     elif (e != 0):
#         if (e != num):
#           matrix = False
#           break
#         elif ( abs(pos -  (i % rc)) == 1 ):
#             pos = abs(i % rc)
#         else:
#             matrix = False
#             break
# if (matrix):
#     print("Matriz escalar")

# else:
#     print("Matriz no escalar")

#04
# rc= int(input())
# pos = -1
# num = -1
# not_matrix = None
# matrix_type = None
# zero_values = 0
# add = 0
# for i in range( rc * rc):
#     e = int(input())
#     if (e == 0 and i == 0):
#         not_matrix = True
#         break
#     elif (e != 0 and i == 1 ):
#        matrix_type = True
#     elif (e == 0 and i == 1):
#        matrix_type = False
       
#     if (matrix_type == True ):
#         if (i % rc == 0 or zero_values < i // rc):
            
#             zero_values += 1

#             if (e == 0):
#                 pass
#             else:
#                 not_matrix = True
#                 break
            
#         else:
#             if ((i + 1) % rc == 0):
#                 zero_values = 0

#             if (e == 0):
#                 not_matrix = True
#                 break
    
#     elif (matrix_type == False):
#        if (i % rc == 0 or zero_values > i // rc):
            
#             zero_values -= 1

#             if (e != 0):
#                 pass
#             else:
#                 not_matrix = True
#                 break
            
#        else:
#             if (e != 0):
#                 not_matrix = True
#                 break
#             elif ((i + 1) % rc == 0):
#                 zero_values = rc + add 
      
#                 add += 2
    
# if (not_matrix == True):
#     print("No es triangular superior ni inferior")
# elif (matrix_type):
#     print("Triangular superior")

# else:
#     print("Triangular inferior")

#05
# side = int(input())
# is_flag = True
# index = 0

# def check_list(l):
#     for i in l:
#         if i != "*":
#             return False
#     return True
    
# index = 0
# adder = 0
# for i in range(side):
#     flag_part = list(input())
#     flag = [e for e in flag_part if e.strip() != "" ]
    
#     if (side - index < (side // 2) + 1 ):
#         i -= adder + 2
#         adder += 2
    
#     if ((flag[i] == "0" and flag[-i -1]== "0") and check_list(flag[0:i] + flag[i+1:-i-1]+ flag[10000 if i == 0 else -i : len(flag) ])):
#         pass
        
#     else:
#         is_flag = False
#         break
#     index += 1

# if (is_flag):
#     print("Si es la bandera de Escocia")
# else:
#     print("No es la bandera de Escocia")

#06
# rows = int(input())
# columns = int(input())
# row = []
# table = []
# before = 1
# for i in range(rows*columns):
#     e = int(input())
#     if (i % columns ==0 and i != 0):
#         table.append(row)
#         row = 1
#         before = 1
#     row = e * before 
#     before = row 
    
# table.append(row)
# max_value = max(table)
# min_value = min(table)

# print(table.index(max_value))
# print(table.index(min_value))

#07
# items_input = int(input())
# items = []

# def find_item(l, n):
#     for i in l:
#         if i["name"] == n:
#             return i["price"]

# for i in range(items_input):
#     item = input()
#     item = item.split(":")
#     item_val = {
#         "name": item[0],
#         "price": item[1]
#     }
#     items.append(item_val)

# order_input  = int(input())
# total = 0
# for o in range(order_input):
#     order = input()
#     order = order.split(" ")
#     order_val = {
#         "name": order[0],
#         "amount": order[1]
#     }
#     price = find_item(items, order_val["name"])
#     price = int(int(price) * int(order_val["amount"]))
#     total += price

# if (total > 100000):
#     total = total * 0.7
# print(round(float(total),1))

#08
# words_input = int(input())
# words = []
# translated_text = []
# def find_word(l, n):
#     for i in l:
#         if i["word"] == n:
#             return i["translation"]

# for i in range(words_input):
#     word = input()
#     word = word.split(":")
#     word_val = {
#         "word": word[0],
#         "translation": word[1]
#     }
#     words.append(word_val)

# text_input  = int(input())

# for t in range(text_input):
#     row = input()
#     row = row.split(" ")
#     row_translated = []
#     for w in row:
#         word_translated = find_word(words,w)
#         row_translated.append(word_translated)
#         row_translated.append(" ")

#     row_translated.pop()
#     translated_text.append(row_translated)

# for i in translated_text:
#     print("".join(i))