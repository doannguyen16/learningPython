import comon.common as util
def print_hi(name):
  print(f'Hi, {name}')

if __name__ == '__main__':
  print_hi('PyCharm')

  # comment

  '''
  comment block code.
  line 2
  '''

  # append String.
  print("Line {}.{}".format(1,1))
  print("Line {}".format(2))

  # init variable.
  count = 0
  flag = True

  # None -> null java.
  person = None

  # ArrayList => dynamic  -> ArrayList
  personList = ["DOAN", "KHANG", "THUAN"]
  index = personList[0]

  # Tuple => immutable, read only.  => String[]
  statusList = ("PEND", "COMPLETE", "TESTING")
  status = statusList[0]

  # Dictionary
  # init dictionary empty.
  mapPersonById = {}
  mapPersonById['12'] = "Khang"
  mapPersonById['11'] = "DOAN"
  # access by KEY.
  personName = mapPersonById['12']

  # init dictionary
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }

  # for, if else, switch case/while, try catch
  for p in personList:
    if (p == 'THUAN'):
      print("HELLO THU AN {}".format(p))
    else:
      print("HELLO ANH TRAI {}".format(p))

  switcher = {
    0: print_hi("DOAN"),
    1: "one",
    2: "two",
  }

  switcher.get(0, "nothing")

  i = 1
  while i < 6:
    print(i)
    i += 1

  # Exception -> childException(DivisionZeroError, OutOfIndexArrayError)
  try:
    count = 0
    so = 5 / 0
    print("RUNIIINNNN")
  except ZeroDivisionError as e1:
    print("ZeroDivisionError: " + str(e1))
  except Exception as e:
    print("Unknown error" + str(e))

  # dictionary, default loop key
  for x in mapPersonById:
    print("Key={}, Value={}".format(x, mapPersonById[x]))

  # sleep, file handling, seperate function.

