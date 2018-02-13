# EmailLeaks

<h2>Learn if your Email has been hacked.</h2>

<h1>Usage:</h1>

   A)You can specify 2 arguments.<br />
     1)Argument email.<br />
     2)Argument path.<br />
     <hr />
   B)
     You can give the inputs while the program is running.
     At path input type:

      1)n     #to just display the results and don't save it to a file
      
      2)press enter  #to save it at the default path
      default path = drive/filepath/leaks.txt
      
      
<h2>Example:</h2>

        python EmailLeaks.py someEMail@someShit.com c://Somepath/somefile.txt
   

How the program works:
 
1)The program is senting a get request to the https://hacked-emails.com/ site.<br />
2)The site responds with a json file<br />
3)Finally we print the results<br />

How https://hacked-emails.com/ works:
    
   see here: https://hacked-emails.com/about
