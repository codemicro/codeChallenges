import main
import jellyfish

s1 = input("String one: ")
s2 = input("String two: ")

correct_res = jellyfish.jaro_similarity(s1, s2)
this_res = main.jaro_similarity(s1, s2)

print("---- JARO SIMILARITY ----")
print("This value:", this_res)
print("Value matches Jellyfish:", correct_res == this_res)
if correct_res != this_res:
  print("Jellyfish value:", correct_res)


print("---- JARO-WINKLER SIMILARITY ----")
correct_res = jellyfish.jaro_winkler_similarity(s1, s2)
this_res = main.jaro_winkler_similarity(s1, s2)

print("This value:", this_res)
print("Value matches Jellyfish:", correct_res == this_res)
if correct_res != this_res:
  print("Jellyfish value:", correct_res)