######################################################################
# Author: Elaheh Jamali
# Username: Jamalie

# Assignment: A4: Breaking Bad Ciphers
#
# Purpose: Thia assignment explores the process for cracking different ciphers.
#
# Acknowledgement: Dr. Maiti and Emely Alfaro Zavala for giving me hints
# about the way to write the cipher on the paper
#
######################################################################
cipher = "aohpdnxnrilitxdsnefxxnogtfxxomceexxweolrxxftmyexx"


for i in cipher:
  split_cipher= cipher.split("x")  # splitting the cipher where we see x
  # print(split_cipher)
  new_list = []
  for string in split_cipher:  # getting rid of the empty strings and moving everything to new lsit
    if string:
      new_list.append(string)
  # print(new_list)
  message = ""

  each_row = len(new_list[0])
  i=0
  while i<each_row:           # to have the message we are adding first the first index then second of each big strings in the list
    for text in new_list:

      try:
        message += text[i]
      except:
        break
    i += 1

  print(message)
