# Jaro distance

http://rosettacode.org/wiki/Jaro_distance

```
Date: 07/07/2020
Language: Python
Lines: 77 (excluding test)
Status: could be improved
```

#### Problems

* I'm not entirely certain that the Jaro-Winkler similarity implemented is completely accurate
  * I was using the Jellyfish library for Python to test similarities, but the Jaro-Winkler similarity implementation in that seems to be slightly different to that described on Wikipedia.
  * Furthermore, reference 2 goes into more detail about values *![p](https://latex.codecogs.com/gif.latex?p)* and *![l](https://latex.codecogs.com/gif.latex?l)* and their constraints, specifically that *"we must have ![p <= 0.25](https://latex.codecogs.com/gif.latex?p%20%5Cleq%200.25), but that is only because [...] ![l](https://latex.codecogs.com/gif.latex?l) was constrained to be ![<= 4](https://latex.codecogs.com/gif.latex?%5Cleq%204)"*

#### Sample output (of tests)

```
codeChallenges/jaroDistance on  jaroDistance (9012ece) via 🐍 v3.7.2
❯ python .\main.py
jaro(MARTHA, MARHTA) = 0.9444444444444444
jaro(DIXON, DICKSONX) = 0.7666666666666666
jaro(JELLYFISH, SMELLYFISH) = 0.8962962962962964
```

#### References/helpful documents

1. ["Jaro–Winkler distance" *Wikipedia*](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
2. ["What is Jaro/Jaro-Winkler similarity?" *Statistical Odds & Ends*](https://statisticaloddsandends.wordpress.com/2019/09/11/what-is-jaro-jaro-winkler-similarity/)