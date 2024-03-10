
import sys
# list  of lists for nutration facts of seafood [calories,protein,sugar]
seafood_nutration_facts = [[100,20,0],[130,17,0],[110,17,0],[90,20,0],[100,19,0],[100,21,0],[120,23,0],[80,17,0],[110,21,0]
                           ,[80,16,0],[100,10,0],[90,20,0],[140,20,0],[110,20,0],[130,22,0],[140,27,0],
                           [100,21,0],[120,16,0],[110,22,0],[130,26,0]]
# list of seafood names
seafood_names = ["Blue Crap","Catfish","Clams","Cod","Sole","Haddock","Halibut","Lobster","Ocean Perch"
                 ,"Orange Rought","Oysters","Pollock","Rainbow Trout","Rockfish","Salmon","Scallops",
                 "Shrimp","Swordfish","Tilapia","Tuna"]

# list  of lists for nutration facts of vegetables [calories,protein,sugar]
vegetables_nutration_facts = [[20,2,2],[25,1,4],[45,4,2],[30,1,5],[25,2,2],[15,0,2],[10,1,1],[20,1,2],
                              [25,1,3],[10,0,1],[10,1,2],[15,1,1],[20,3,0],[45,1,9],[110,3,1],
                              [10,0,2],[20,1,2],[90,4,5],[100,2,7],[25,1,3]]
#list of vegetables names
vegetables_names = ["Asparagus","Bell Pepper","Broccoli","Carrot","Cauliflower","Celery","Cucumber","Green Beans",
                    "Green Cabbage","Green Onion","Iceberg Lettuce","Leaf Lettuce","Mushrooms","Onion","Potato",
                    "Radishes","Summer Squash","Sweet Corn","Sweet Potato","Tomato"]


# list  of lists for nutration facts of fruits [calories,protein,sugar]
fruits_nuration_facts = [[130,1,25],[50,1,0],[110,1,19],[50,1,11],[60,1,11],[90,0,20],[50,1,11],[90,1,13],[15,0,2],
                         [20,0,0],[60,1,11],[80,1,14],[60,1,13],[100,1,16],[50,1,10],[70,1,16],[50,1,8],[100,1,16],
                         [50,1,9],[80,1,20]]
#list of fruits names
fruits_names = ["Apple","Avocado","Banana","Cantaloupe","Grapefruit","Grapes","Honeydew Melon","Kiwifruit","Lemon",
                "Lime","Nectarine","Orange","Peach","Pear","Pineapple","Plums","Strawberries","Sweet Cherries",
                "Tangerine","Watermelon"]
#list of everythings nutration facts
nutration_facts = seafood_nutration_facts + vegetables_nutration_facts + fruits_nuration_facts
#list of all names
names = seafood_names + vegetables_names + fruits_names

#printing options as function
def home_screen():
    print("From the options below, please select your choice:")
    print("\t 1-How many calories are there in fruit?")
    print("\t 2-How many calories,grams of sugar, and proteins are in vegetables?")
    print("\t 3-Calories, sugar, and protein content of one meal(Seafood,Fruits,Vegetables)?")
    print("\t 4-Exit")
home_screen()
while(True) :
    choice = int(input("Please type your choice Number:"))
    if choice == 1:
        print("Please write 'stop' if you want to exit.")
        while(True) :
            fruit = input("Please type your fruit: ")
            if fruit == "stop" :
                print("\n\n")
                home_screen()
                break
            check = None
            for fr in range(len(fruits_names)) :
                if fruit == fruits_names[fr]:
                    print("Calories for "+fruits_names[fr]+" is "+str(fruits_nuration_facts[fr][0]))
                    check = 1
                if check == None and fr == 19:
                    print("Kindly select another fruit or double-check your spelling")
    if choice == 2:
        print("Please write 'stop' if you want to exit.")
        while(True) :
            vegetable = input("Please type your vegetables: ")
            if vegetable == "stop" :
                print("\n\n")
                home_screen()
                break
            check = None
            for vege in range(len(vegetables_names)) :
                if vegetable == vegetables_names[vege]:
                    print("Calories for "+vegetables_names[vege]+" : "+str(vegetables_nutration_facts[vege][0])+
                          ", sugar:"+str(vegetables_nutration_facts[vege][2])+", protein:"+str(vegetables_nutration_facts[vege][1]))
                    check = 1
                if check == None and vege == 19:
                    print("Kindly select another vegetable or double-check your spelling")
    if choice == 3:
        print("If you wish to stop please write exit \n  Onse you've selected your meal items and you want"+
              " to see the nutration information for it, type cal")
        
        calories = 0
        sugar = 0
        protein = 0
        while(True) :
            food = input("Please type your fruit/vegetables/seafood: ")
            check = None
            if food == "exit" :
                print("\n\n")
                home_screen()
                break
            elif food == "cal" :
                check = 1 
                print("Total Calories for your meal is : "+str(calories)+
                  ", total sugar:"+str(sugar)+", total protein:"+str(protein))
                
                y_n = input("Would you like to calculate again? (y/N)")
                if y_n == "N":
                    home_screen()
                    break
                else : 
                    calories = 0
                    sugar = 0
                    protein = 0
                    continue                         
            elif not(food == "cal" or food == "exit") : 
               
                for f in range(len(names)) :
                    if food == names[f]:
                        calories += nutration_facts[f][0]
                        sugar += nutration_facts[f][2]
                        protein += nutration_facts[f][1]
                        check = 1
                                           
                    
                        
               
                    
                    if check == None and f== 59:
                        print("Kindly select another fruit/vegetables/seafood or double-check your spelling")
    if choice == 4 :
        sys.exit()
