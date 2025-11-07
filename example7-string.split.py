#!python3
"""
(method) def split(
    sep: LiteralString | None = None,
    maxsplit: SupportsIndex = -1
) -> list[LiteralString]
Return a list of the substrings in the string, using sep as the separator string.

sep
  The separator used to split the string.

  When set to None (the default value), will split on any whitespace
  character (including \n \r \t \f and spaces) and will discard
  empty strings from the result.
maxsplit
  Maximum number of splits (starting from the left).
  -1 (the default value) means no limit.
"""

sentence = "The quick brown fox"
myList = sentence.split(" ")
print(myList)
print(f"The first word (with key index 0) is {myList[0]}")
print(f"The second word (with key index 1) is {myList[1]}")