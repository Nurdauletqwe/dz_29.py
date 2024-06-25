# этот код для дб
'''CREATE TABLE food (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price int, 
	rating int
);
insert into food(name, price, rating) values('burger', 2000, 10)
select * from food'''


import psycopg2
conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='postgres', user='postgres', password='12345')
cursor = conn.cursor()
def __init__(self, id, name, price, rating):
    self.id = id
    self.name = name
    self.price = price
    self.rating = rating
    
def add_food():
        name = input('Enter name of food: ')
        price = int(input('Enter price of food: '))
        rating = int(input('Enter rating of food: '))
        insert_query = f"INSERT INTO food (name, price, rating) VALUES ('{name}', {price}, {rating})"
        cursor.execute(insert_query)
        conn.commit()
        print('Food added successfully!')

def view_food():
        select_query = "SELECT * FROM food"
        cursor.execute(select_query)
        foods = cursor.fetchall()
        for food in foods:
            print(food)

def update_food():
        food_id = int(input('Enter food ID to update: '))
        new_price = int(input('Enter new price: '))
        update_query = f"UPDATE food SET price = {new_price} WHERE id = {food_id}"
        cursor.execute(update_query)
        conn.commit()
        print('Food updated successfully!')

def delete_food():
        food_id = int(input('Enter food ID to delete: '))
        delete_query = f"DELETE FROM food WHERE id = {food_id}"
        cursor.execute(delete_query)
        conn.commit()
        print('Food deleted successfully!')

while True:
        print("\n1. Add food\n2. View food\n3. Update food\n4. Delete food\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_food()
        elif choice == 2:
            view_food()
        elif choice == 3:
            update_food()
        elif choice == 4:
            delete_food()
        elif choice == 5:
            break
        else:
            print("Choose only from 1 to 5!")

cursor.close()
conn.close()