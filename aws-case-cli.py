#!/usr/bin/python

import boto3
import json
client = boto3.client('support')


## LIST ALL OPEN CASES
def viewOpenCase( ):
  response = client.describe_cases()
  print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
  print "\n"
  return

## OPEN SUPPORT CASE
def openCase(): 
  a = raw_input("Subject: ")
  b = raw_input("Service Code: ")
  c = raw_input("Severity Code: ")
  d = raw_input("Category Code: ")
  e = raw_input("Communication Body: ")
  f = raw_input("Issue Type (customer-service / technical): ")
  g = raw_input("CC Email Address: ")
  
  print (a,b,c,d,e,f)
  response = client.create_case(
      subject= a,
      serviceCode= b,
      severityCode= c ,
      categoryCode= d,
      communicationBody= e,
      issueType= f,
      ccEmailAddresses=[
          'g',
     ])
  
  print response
  print "\n"
  return

## LIST ALL SEVERITY LEVELS - NECESSARY INFO TO OPEN CASE
def listSevLvl():
  response = client.describe_severity_levels(
    language='en'
  )
  print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
  print "\n"
  return

## LIST ALL SERVICES & CATEGORIES - NECESSARY INFO TO OPEN CASE
def listSrv ():
  response = client.describe_services(
    language='en',
  )
  with open('describe-services.out','w') as outfile:
      json.dump(response,outfile, sort_keys=True, indent=4, separators=(',', ': '))
  print "FILE WRITTEN TO FILE NAMED - describe-services.out \n"
  return

## MENU LOOP
while True:
  print "AWS Support API CLI"
  print "This script will allow you to list and open cases. "
  print("\nMenu\n (1) View Open Cases\n (2) Open a Case\n (3) Describe severity levels\n (4) List Services \n (Q)uit")
  choice = raw_input(">>> ").lower().rstrip()
  if choice=="q":
        break
  elif choice=="1":
        viewOpenCase( )
  elif choice=="2":
        openCase()
  elif choice=="3":
        listSevLvl()
  elif choice=="4":
        listSrv()
  else:
        print("Invalid choice, please choose again\n")
 
print("game over")
print(".")

