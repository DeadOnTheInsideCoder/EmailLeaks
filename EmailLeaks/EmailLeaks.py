#/usr/bin/python3

import sys,os
import requests
import time 



def intro():

    print("[!]Email Leak.")
    print("[!]Has your email been hacked?\n")



def GetInfo():

    GetEmail()
    GetPath()


    
def GetEmail():

    
    global email
    try:
      
       argv = sys.argv[1]
       if argv == "-h":

             print("[!]Usage example: \n[!]python EmailLeak.py somemail@hotmail.com somepath/somepath")
             sys.exit()
       else:
              
             email = sys.argv[1]

    except IndexError:
        
       try:
           
        email = str(input("[?]Enter email: "))

       except KeyboardInterrupt:

         print("\n[!]You pressed ctrl+x")
         print("[*]Exiting!")
         sys.exit()
         
    except Exception as e:

        print(str(e))
        sys.exit()
        


def GetPath():

    global path
    try:
      
       path = sys.argv[2]

    except IndexError:
        
       try:
           
        path = str(input("[?]Enter path 'n' for no path: "))
        if path == "":
            
           path = os.path.dirname(__file__)+"\leaks.txt"
          
        elif path == "n" :

             path = "n"
            
       except KeyboardInterrupt:

         print("\n[!]You pressed ctrl+x")
         print("[*]Exiting!")
         sys.exit()
         
    except Exception as e:

        print(str(e))
        sys.exit()



    
def hackedEmails():

    global email
    global res
    global path
    
    url = "https://hacked-emails.com/api?q="+str(email)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        
      req = requests.get(url, headers=headers)
      res = req.json()
      if res["status"] == "badsintax":
        
        print("\n[!]Error: Bad syntax.")
        print("[!]Email has wrong syntax.")
        print("[!]Email: ",email)
        sys.exit()

      elif res["status"] == "notfound":

        print("\n[*]Congratulations website: hacked-emails.com didn't found leaks!")
        print(">>Total Leaks: ",res["results"])
        print(">>Email: ",res["query"])
        print(">>Status: ",res["status"])
        print(">>Data: ",res["data"])

      elif res["status"] == "found":
          
        print("\n[!]Website: hacked-emails.com found ",res["results"]," leaks!\n")
        print(">>Status: ",res["status"])
        print(">>Email: ",res["query"])
        print(">>Total Leaks: ",res["results"])
        print(">>Path: ",path)
        print("[*]Press enter to show details")
        input()
        WriteDataToFile()

    except Exception as e:

    
        print("[!]Error:\n",str(e))
        sys.exit()

    except KeyboardInterrupt:

        print("\n[!]You pressed ctrl+x")
        print("[*]Exiting")
        sys.exit()


def WriteDataToFile():

        
        global res
        global path
        count = 0
        if path == "n":
            print("[!]Website: hacked-emails.com found "+str(res["results"])+" leaks!\nEmail:"+res["query"]+"\n\n")
            while count < int(res["results"]):
               
               print(">>Leak",str(count+1),":\n")
               print("\t>>Source Url: ",res["data"][count]["source_url"])
               print("\t>>Lines: ",res["data"][count]["source_lines"])
               print("\t>>Size: ",res["data"][count]["source_size"])
               print("\t>>Source Network: ",res["data"][count]["source_network"])
               print("\t>>Source Provider: ",res["data"][count]["source_provider"])
               print("\t>>Verified: ",res["data"][count]["verified"])
               print("\t>>Title: ",res["data"][count]["title"])
               print("\t>>Author: ",res["data"][count]["author"])
               print("\t>>Date Created: ",res["data"][count]["date_created"])
               print("\t>>Date Leaked: ",res["data"][count]["date_leaked"])
               print("\t>>Emails Found: ",res["data"][count]["emails_count"])
               print("\t>>Details: ",res["data"][count]["details"]+"\n")
               count +=1


        else:
            
          file = open(path,"w")
          file.write("[!]Website: hacked-emails.com found "+str(res["results"])+" leaks!\nEmail:"+res["query"]+"\n\n")
          while count < int(res["results"]):

            try:
                 
              
              file.write(">>Leak "+str(count+1)+":\n")
              file.write("\t>>Source Url: "+str(res["data"][count]["source_url"])+"\n")
              file.write("\t>>Lines: "+str(res["data"][count]["source_lines"])+"\n")
              file.write("\t>>Size: "+str(res["data"][count]["source_size"])+"\n")
              file.write("\t>>Source Network: "+str(res["data"][count]["source_network"])+"\n")
              file.write("\t>>Source Provider: "+str(res["data"][count]["source_provider"])+"\n")
              file.write("\t>>Verified: "+str(res["data"][count]["verified"])+"\n")
              file.write("\t>>Title: "+str(res["data"][count]["title"])+"\n")
              file.write("\t>>Author: "+str(res["data"][count]["author"])+"\n")
              file.write("\t>>Date Created: "+str(res["data"][count]["date_created"])+"\n")
              file.write("\t>>Date Leaked: "+str(res["data"][count]["date_leaked"])+"\n")
              file.write("\t>>Emails Found: "+str(res["data"][count]["emails_count"])+"\n")
              file.write("\t>>Details: "+str(res["data"][count]["details"])+"\n\n")
              print(">>Leak",count,":\n")
              print("\t>>Source Url: ",res["data"][count]["source_url"])
              print("\t>>Lines: ",res["data"][count]["source_lines"])
              print("\t>>Size: ",res["data"][count]["source_size"])
              print("\t>>Source Network: ",res["data"][count]["source_network"])
              print("\t>>Source Provider: ",res["data"][count]["source_provider"])
              print("\t>>Verified: ",res["data"][count]["verified"])
              print("\t>>Title: ",res["data"][count]["title"])
              print("\t>>Author: ",res["data"][count]["author"])
              print("\t>>Date Created: ",res["data"][count]["date_created"])
              print("\t>>Date Leaked: ",res["data"][count]["date_leaked"])
              print("\t>>Emails Found: ",res["data"][count]["emails_count"])
              print("\t>>Details: ",res["data"][count]["details"]+"\n")
              count +=1


        
            except KeyboardInterrupt:

                print("[!]You pressed ctr+x")
                print("[!]Exiting...")
                file.close()
                sys.exit()

        
def main():

    intro()
    GetInfo()
    hackedEmails()
    
main()
