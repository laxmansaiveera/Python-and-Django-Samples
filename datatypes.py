# Different naming conventions
snake_case = "i_am_snake_case"
camelCase = "i Am Camel Case"
PascalCase = "I Am Pascal Case"
kebabcase = "i-am-kebab-case" 
mix_Style123 = "M1x st7le"
normal = "Just normal"

print([snake_case, camelCase, PascalCase, mix_Style123, normal])

#Intermediate Tasks (Manipulation & Conversion)
#1 List
players=["rohit","virat","gill","dhoni"]
players[2] = "surya"              # Replace "Gill" with "Surya"
players.append("jadeja")          # Add "Jadeja"
print(len(players))               # Print length
print(players[-2])                # Print second last player

#2 Tuple
laptop_info = ("HP", "16GB", "512GB SSD", 2024, True)
print(laptop_info[-2:])   

#3 set
countries = {"India", "USA", "India", "Canada", "UK", "USA"}
print(countries)               # Duplicates are removed automatically
countries.add("Germany")
countries.remove("UK")
print(countries)

#4 frozenset
frozen_marks = frozenset([90, 85, 75, 85])
# frozen_marks.add(100)       
# frozen_marks.remove(85)      
print(type(frozen_marks))

#Advanced Tasks
#1.dictionaries
car_info = {
    "brand" : "tesla",
    "model" : "model S",
    "price" : "1.5cr",
    "features": ["autophile","electric","sunroof"]
}
car_info["color"] = "white"
car_info["price"] = "1.7cr"
car_info["insurance"] = {"provider": "HDFC","valid_till":"2026"}
print(car_info)

#2 List Dictionaries
books = [
    {"title": "Atomic Habits", "author": "James Clear"},
    {"title": "Ikigai", "author": "Héctor García"},
    {"title": "Zero to One", "author": "Peter Thiel"}
]
books.append({"title": "Deep Work", "author": "Cal Newport"})
for book in books:
    if book["author"] == "Peter Thiel":
        print(book["title"])

#3 nested dictionary print
laptop = {
    "brand": "Apple",
    "specs": {"ram": "16GB", "storage": "1TB SSD", "chip": "M2"},
    "price": "2L"
}
print(laptop["specs"]["chip"])
print(f'{laptop["brand"]} laptop comes with {laptop["specs"]["chip"]} chip and costs {laptop["price"]}.')

#challenge task
#1movie tracker
ott_data = [
    {"platform": "Netflix", "shows": ["Stranger Things", "Wednesday"]},
    {"platform": "Prime", "shows": ["Mirzapur", "Farzi"]},
    {"platform": "Hotstar", "shows": ["Special Ops", "The Freelancer"]}
]
for platform in ott_data:
    if platform["platform"] == "Prime":
        platform["shows"].append("Panchayat")                
    if platform["platform"] == "Netflix":
        print(platform["shows"])                            


#2memorycheck
a = 500
b = 500
print(id(a), id(b))          

x = "hello"
y = "hello"
print(id(x), id(y))          
