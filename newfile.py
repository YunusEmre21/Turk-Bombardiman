import requests
While True:
        kime = input("Hedef")
        kim = input("Gönderilecek Mesaj: ")
        if "" in kime or mesaj =="":
            break
 
resp.requests.pots("https://textbelt.com/test", {
    'phone': '{}'.format(kime)
     'message':'{}'.format(mesaj)
     'key':'textbelt'
  } )
  
  print("İslem:{} kalan hakkiniz{}".format('Basarili if resp.json()[success]=='True'
      else 'Basarisiz', resp.json()['quotaRemaining']
  ")
  
  c = input(" 'exit()' or 'Enter' ")
  if c == "exit()":
       break
 else
 pass