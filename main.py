import comon.common as util
import json

def print_hi(name):
  print(f'Hi, {name}')

def less_than(item):
  return item < 50

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

  # string util
  #[)
  text = "Doan .pdfan com Toi.pdf"
  text2 = "Doan an com Toi"
  # lowcase
  print(text.lower())
  # uppercase
  print(text.upper())
  # substring
  print(text[0:text.index(" ")])
  # extension lastIndexOf
  print(text[text.rindex(".") + 1 : len(text)])
  # string -> array.
  print(text2.split(" "))
  # replace
  print(text2.replace("Doan", "Khang"))
  # contain
  if('Doan' in text2):
    print("Doan ne")
  else:
    print("Khang ne")
  # check startWith, endWith
  if(text.endswith(".pdf")):
    print("Supported PDF Format")
  else:
    print("No support this file")

  text3 = "2023-10-02_Document.pdf"
  if(text3.startswith("2023")):
    print("Process file in 2023")
  else:
    print("No support this file")

  # join all items of list into single string by delimiter
  print(" ".join(personList))

  # array utils
  array = [1, 2, 50, 10, 4]
  # filter array
  result = [x for x in array if x < 50]
  print(result)
  # add item into array
  array.append(6)
  print(array)
  # insert between
  array.insert(3, 18)
  print(array)
  # remove item by value
  array.remove(50)
  print(array)
  # seperate array most like substring.
  print(array[0:3])

  # dict utils mapPersonById
  # check constain.
  if(mapPersonById.__contains__("12")):
    print("Found key")
  else:
    print("Not Found")
  # add key-value
  mapPersonById['13'] = "Thuan"
  # delete key
  del mapPersonById['12']
  #mapPersonById.__delitem__("12")
  print(mapPersonById)
  # add duplcate key.
  mapPersonById['11'] = "Thang"
  print(mapPersonById)


  # read file and parse json
  f = open("./doc/example.json", "r")
  # json string into dict
  # call GET API.
  response = json.loads(f.read())
  listOfAction = response['menu']['popup']['menuitem']
  response['menubar'] = "abc"
  print("asdsad")

  # convert dict to json String.
  # call POST, PUT
  requestBody = json.dumps(response)
  print(requestBody)








