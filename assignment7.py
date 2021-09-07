# NUMBER 1 WITH DEFINED FUNCTION CALLED CASE_COUNT.
def case_count(string: str) -> dict:
  Capital = 0
  small = 0
  for char in string:
    if char.isupper():
      Capital += 1
    elif char.islower():
      small += 1
    else:
      pass

  dict = {'upper': Capital, 'lower':small}
  return dict


print(case_count("The University of Lagos"))

# NO 1 WITH NO DEFINED FUNCTION.
school = "University Of Lagos"
lowers, uppers = 0, 0
for i in school:
  if i >= 'A' and i <= 'Z':
   uppers = uppers + 1
  elif i >= 'a' and i <= 'z':
    lowers = lowers + 1

print({'upper': uppers, 'lower': lowers})