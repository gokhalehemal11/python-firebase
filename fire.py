from firebase import firebase 
import datetime

firebase= firebase.FirebaseApplication('https://btapp-2a08c.firebaseio.com/')

result= firebase.get('/logged_in',None)
got_it= list(result.values())[0]
print(list(result.values())[0])


'''db=firebase.database()
already_issued= db.child('/issued_books'+got_it+'/').get()
print("al",already_issued)
'''


data={0:"Harry potter and the Chamber of Secrets",
1:"J K Rowling",
2:"fantasy",
3:"https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png",
4:"15:79:53:C3:FC",
5:str(datetime.datetime.now().time())}
nxt= firebase.post('/issued_books/'+got_it+'/',data)
print("Added")


already_issued= firebase.get('/issued_books/'+got_it+'/', None)
#print(already_issued)
for key, val_list in already_issued.items():
	if(val_list[4]== "15:79:53:C3:FC"):
		firebase.delete('/issued_books/'+got_it+'/'+key+'/',None)
		print("Removed")

