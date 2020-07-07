def is_match_present(source_char, search_list, current_index, dist):
  lower_bound = current_index - dist
  upper_bound = current_index + dist + 1  # Ensure value at current_index is included

  # Prevent IndexErrors
  if lower_bound < 0:
    lower_bound = 0
  if upper_bound > len(search_list):
    upper_bound = len(search_list)

  for i, c in enumerate(search_list):
    if i < lower_bound or i >= upper_bound:
      continue
    elif source_char == c:
      search_list.pop(i)
      return True

  return False

def pad_arrays(l1, l2):
  l1_len = len(l1)
  l2_len = len(l2)

  if l1_len > l2_len:
    for _ in range(l1_len-l2_len):
      l2.append(None)
  elif l2_len > l1_len:
    for _ in range(l2_len-l1_len):
      l1.append(None)


def jaro_similarity(s1:str, s2:str) -> float:
  s1_len = len(s1)
  s2_len = len(s2)

  if s1_len == 0 and s2_len == 0:
    return 0.0

  match_distance_requirement = int((s1_len if s1_len > s2_len else s2_len) / 2) - 1
  print(match_distance_requirement)

  matches = 0
  transpositions = 0

  # Convert strings to lists
  s1 = [c for c in s1]
  s2 = [c for c in s2]

  # Pad shortest list to length of longest list
  # Needed?
  pad_arrays(s1, s2)

  # Find matches
  # The lists will always have the same content in a different order
  s1_matches = []
  s2_matches = []

  for i, (s1c, s2c) in enumerate(zip(s1, s2)):
    if is_match_present(s1c, s2, i, match_distance_requirement):
      s1_matches.append(s1c)

    if is_match_present(s2c, s1, i, match_distance_requirement):
      s2_matches.append(s2c)

  print(s1_matches, s2_matches)

  m = len(s1_matches)

  # Find number of transpositions
  t = 0
  for _, (s1m, s2m) in enumerate(zip(s1_matches, s2_matches)):
    if s1m != s2m:
      t += 1
  t /= 2

  # Calulate similarity
  sim = 1/3*((m/s1_len) + (m/s2_len) + ((m-t)/m)) if m != 0 else 0.0
  
  return sim
