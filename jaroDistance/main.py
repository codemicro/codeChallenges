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
    upper_bound = min(s2_len, i + match_distance_requirement + 1)
    
    for x in range(lower_bound, upper_bound):
      print(lower_bound, "-", upper_bound, "@", x, f"({i})", s1[i], s2[x], s1[i] == s2[x])
      if s2_matches[x]:  # Already matched to something, so cannot use
        continue
      elif s1[i] == s2[x]:
        s1_matches[i] = True
        s2_matches[x] = True
        matches += 1
        break  # match found, no need to keep iterating

  print(s1, s1_matches, s2, s2_matches)

  # Find number of transpositions
  x = 0
  for i in range(s1_len):
    if not s1_matches[i]:
      continue

    # We shouldn't ever start iterating over s2 again, so we continue from where we left off in the previous iteration.
    # This while loop waits for a match to occur in s2 before continuning 
    while not s2_matches[x]:
      x += 1
    
    if s1[i] != s2[x]:
      # If the program ends up here, it means that that a match was found within the allowable range of match_distance_requirement,
      # but NOT exactly in line
      transpositions += 1

    x += 1

  transpositions /= 2

  print("m", matches, "t", transpositions)

  # Calulate similarity
  sim = 1/3*((matches/s1_len) + (matches/s2_len) + ((matches-transpositions)/matches)) if matches != 0 else 0.0
  
  return sim
