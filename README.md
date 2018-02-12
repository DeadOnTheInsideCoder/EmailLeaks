# EmailLeaks

Learn if your Email has been hacked.

usage:

   1)You can specify 2 arguments.
   Argument 1 email.
   Argument 2 path.
   example. python EmailLeaks.py someEMail@someShit.com c://Somepath/somepath
   
   2)You can give the inputs while the program is running.
   At path input type:
      1)n     #to just display the results and don't save it to a file
      
      2)press enter  #to save it at the default path,default path = drive/filepath/leaks.txt
   

How the program works:
 
1)The program is senting a get request to the https://hacked-emails.com/ site.
2)The site responds with a json file
3)Finally we print the results

How https://hacked-emails.com/ works:
    
    see here: https://hacked-emails.com/about
