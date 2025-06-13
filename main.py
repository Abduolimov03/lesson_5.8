### 1 CSV representation of array
# def to_csv_text(array):
#     return "\n".join([','.join(map(str, row)) for row in array])

### 2 Define a card suit
# from preloaded import DECK
#
# def define_suit(card):
#     suits = {
#         'C':'clubs',
#         'D':'diamonds',
#         'H':'hearts',
#         'S':'spades'
#     }
# return suits(card[-1])

### 3 Remove First and Last Character Part Two
# def remove_the_ends(string):
#     parts = string.split(',')
#     if len(parts) <= 2:
#         return None
#     return ' '.join(parts[1:-1])


# ### 4 Reversing Words in a String
# def reverse(st):
#     return ' '.join(st.strip().split()[::-1])

### 5 Alan Partridge II - Apple Turnover
# def apple(x):
#     return "It's hotter than the sun!!" if int(x) ** 2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


### 6
# def sonlar_generator():
#     for i in range(1, 11):
#         yield i
#
# gen = sonlar_generator()
#
# for son in gen:
#     print(son)

### 7
# def cheksiz_natural_sonlar():
#     son = 1
#     while True:
#         yield son
#         son += 1
#
# gen = cheksiz_natural_sonlar()
#
# for _ in range(5):
#     print(next(gen))

### 8
# def fibbonach_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# gen = fibbonach_generator()
#
# for _ in range(10):
#     print(next(gen))

### 9
# def fayl_qator_generator(fayl_nomi):
#     try:
#         with open('data.txt', 'r') as f:
#             for qator in f:
#                 yield qator.strip()
#     except FileNotFoundError:
#         print(f"Xato: '{fayl_nomi}' fayli topilmadi.")
#     except Exception as e:
#         print(f"Faylni o'qishda kutilmagan xato yuz berdi: {e}")
#
#
# with open('data.txt', 'w') as f:
#     f.write("Bu birinchi qator.\n")
#     f.write("Ikkinchi qator shu.\n")
#     f.write("Uchinchi qator ham bor.\n")
#
# print("Fayl qatorlari:")
# for qator in fayl_qator_generator('data.txt'):
#     print(qator)

### 10
# def juft_sonlar_generator(ketma_ketlik):
#     for son in ketma_ketlik:
#         if son % 2 == 0:
#             yield son
#
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Boshlang'ich ketma-ketlik: {sonlar}")
#
# print("Faqat juft sonlar:")
# for juft_son in juft_sonlar_generator(sonlar):
#     print(juft_son)
#
# boshqa_sonlar = [11, 22, 33, 44, 55]
# print(f"\nBoshqa ketma-ketlik: {boshqa_sonlar}")
# print("Faqat juft sonlar:")
# for juft_son in juft_sonlar_generator(boshqa_sonlar):
#     print(juft_son)

### 11
# def takrorlanuvchi_elementlar_generator(ketma_ketlik):
#     ko_rilgan_elementlar = set()
#     takrorlangan_elementlar = set()
#
#     for element in ketma_ketlik:
#         if element in ko_rilgan_elementlar:
#             if element not in takrorlangan_elementlar:
#                 yield element
#                 takrorlangan_elementlar.add(element)
#         else:
#             ko_rilgan_elementlar.add(element)
#
# sonlar = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 8]
# print(f"Boshlang'ich ketma-ketlik: {sonlar}")
#
# print("Takrorlanuvchi elementlar:")
# for takrorlangan in takrorlanuvchi_elementlar_generator(sonlar):
#     print(takrorlangan)
#
# harflar = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'f']
# print(f"\nBoshqa ketma-ketlik (harflar): {harflar}")
# print("Takrorlanuvchi elementlar:")
# for takrorlangan in takrorlanuvchi_elementlar_generator(harflar):
#     print(takrorlangan)

# ### 12
# def birlashtiruvchi_generator(ketma_ketlik1, ketma_ketlik2):
#     min_len = min(len(ketma_ketlik1), len(ketma_ketlik2))
#
#
#     for i in range(min_len):
#         yield ketma_ketlik1[i]
#         yield ketma_ketlik2[i]
#
#     for i in range(min_len, len(ketma_ketlik1)):
#         yield ketma_ketlik1[i]
#
#     for i in range(min_len, len(ketma_ketlik2)):
#         yield ketma_ketlik2[i]
#
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(f"Ketma-ketlik 1: {list1}")
# print(f"Ketma-ketlik 2: {list2}")
#
# print("Birlashtirilgan natija:")
# for element in birlashtiruvchi_generator(list1, list2):
#     print(element)
#
# print("-" * 20)
#
# list3 = [10, 20, 30, 40, 50]
# list4 = ['x', 'y', 'z']
# print(f"Ketma-ketlik 3: {list3}")
# print(f"Ketma-ketlik 4: {list4}")
#
# print("Birlashtirilgan natija (turli uzunlikdagi):")
# for element in birlashtiruvchi_generator(list3, list4):
#     print(element)
#
# print("-" * 20)

### 14
# def arifmetik_progressiya_generator(boshlangich_qiymat, qadam, soni):
#     if soni <= 0:
#         return
#
#     hozirgi_qiymat = boshlangich_qiymat
#     for _ in range(soni):
#         yield hozirgi_qiymat
#         hozirgi_qiymat += qadam
#
#
# print("Misol 1: boshlangich=1, qadam=2, soni=5")
# for x in arifmetik_progressiya_generator(1, 2, 5):
#     print(x)
