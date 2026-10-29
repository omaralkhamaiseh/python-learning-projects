import json 
try:
   with open('movies.json','r') as file:
      watchList=json.load(file)
except FileNotFoundError:
    watchList={}
while True:
   print("1.Add Movie")
   print("2.View Watchlist")
   print("3.Delete Movie")
   print("4.Update Movie")
   print("5.Exit")
   choice= int(input("Enter what you want to do ? "))
   if choice == 1:
      title=input("Enter movie name:")
      rating=int(input("Enter rating (out of 100):"))
      watched=input("Have you watch it (yes/no):")
      watchList[title]={"rating":rating,"watched":watched}
      print(f"{title} has been added!")
      with open('movies.json','w') as file:
         json.dump(watchList,file, indent=4)
   elif choice == 2:
        print("\n--- My Watchlist ---")
        print(watchList)
        print("--------------------\n")
   elif choice == 3:
      delete_title=input("Enter the movie name to delete:")
      if delete_title in watchList:
         del watchList[delete_title]
         with open('movies.json','w') as file:
            json.dump(watchList,file,indent=4)
         print(f"{delete_title} has been deleted!")
      else:
         print("Movie not found in watchlist.")                  
   elif choice == 4:
      update_title=input("Enter the movie name to update: ")
      if update_title in watchList:
         new_rating = int(input("Enter new rating (out of 100): "))
         new_watched = input("Have you watched it now? (yes/no): ")
         watchList[update_title]={"rating":new_rating,"watched":new_watched}
         with open('movies.json','w') as file:
            json.dump(watchList,file,indent=4)
         print(f"{update_title} has been successfully updated!")
      else:
         print("Movie not found in watchlist.")      
   elif choice == 5:
      break