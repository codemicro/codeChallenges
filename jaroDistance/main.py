import jaro

test_cases = [
  ("MARTHA", "MARHTA"),
  ("DIXON", "DICKSONX"),
  ("JELLYFISH", "SMELLYFISH")
  ]

for case in test_cases:
  print(f"jaro({case[0]}, {case[1]}) =", jaro.jaro_similarity(case[0], case[1]))