# -*- coding: utf-8 -*-
"""Suggest suitable appointment from two calendars
"""

cal1 = [(8,10),(10.5,11.5),(12,14),(16.5,17)]
cal2 = [(7.5,9),(10,12),(15,16)]

def get_intervals(calendar,starttime=7,endtime=17):
  '''Takes a calendar as list of tuples with start and end times.
  optionally takes two more parameters for the earliest startime and the latest endtime for accepting appointment suggestions. Startime and end time are
  defaulted to 7 and 17 respectively '''
  ls = []
  for i in calendar:
    if i[0]<=starttime: 
      if i[1]<starttime:
        continue       
      starttime = i[1]
      continue
    ls.append((starttime,i[0]))
    starttime = i[1]
  if i[1]<endtime:
    ls.append((i[1],endtime))
  return ls

def get_suggestions(avl1,avl2):
  ''' Takes the availabilities generated by get_intervals() function from two calendars as a list of tuples
  and returns the common free intervals in the two calendars as suggestions for booking appointments'''
  suggestions =[]

  for i in avl1:
    for j in avl2:
      if (j[0]>=i[0] and j[1]<=i[1]):
        suggestions.append(j)
      elif (j[0]>=i[0] and i[1]>j[0]):
        suggestions.append((j[0],i[1]))
      elif (j[1]>i[0] and j[1]<i[1] and i[0]>j[0]):
        suggestions.append((i[0],j[1]))
      elif (i[0]>j[0] and i[1]<j[1]):
        suggestions.append((i[0],i[1]))

  return set(suggestions)

avl1 = get_intervals(cal1,7,17)
avl2 = get_intervals(cal2)

print(get_suggestions(avl1,avl2))

cal1 = [(8,10),(12,14),(14.5,15),(16.5,17)]
cal2 = [(7,8),(9,10),(11,12),(15,16)]
avl1 = get_intervals(cal1,7,17)
avl2 = get_intervals(cal2)

print(get_suggestions(avl1,avl2))
