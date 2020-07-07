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

  if s1 == s2:
    return 1.0

  match_distance_requirement = int((s1_len if s1_len > s2_len else s2_len) / 2) - 1
  print(match_distance_requirement)

  matches = 0
  transpositions = 0

  # Find matches
  s1_matches = [False] * s1_len
  s2_matches = [False] * s2_len

  for i in range(s1_len):
    lower_bound = max(0, i - match_distance_requirement)
    upper_bound = min(s2_len, i + match_distance_requirement)
    
    for x in range(lower_bound, upper_bound):
      print(lower_bound, "-", upper_bound, "@", x, s1[i], s2[x], s1[i] == s2[x])
      if s2_matches[x]:  # Already matched to something, so cannot use
        continue
        print("This triggered")
      elif s1[i] == s2[x]:
        s1_matches[i] = True
        s2_matches[x] = True

        print(s1_matches, s2_matches)

        matches += 1

        break  # match found, no need to keep iterating

  print(s1_matches, s2_matches)

  # Find number of transpositions
  for i in range(s1_len):
    if not s1_matches[i]:
      continue

    for x in range(s2_len):
      if s2_matches[x]:
        if s1[i] != s2[x]:
          transpositions += 1
        s2_matches[x] = False

  transpositions /= 2

  # Calulate similarity
  sim = 1/3*((matches/s1_len) + (matches/s2_len) + ((matches-transpositions)/matches)) if matches != 0 else 0.0
  
  return sim
