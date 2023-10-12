from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Car:

    def __init__(self,db_data):
        self.id = db_data['id']
        self.user_id = db_data['user_id']
        self.price = db_data['price']
        self.model = db_data['model']
        self.make = db_data['make']
        self.year = db_data['year']
        self.description = db_data['description']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO cars (user_id, price, model, make, year, description) 
                VALUES (%(user_id)s, %(price)s, %(model)s, %(make)s, %(year)s, %(description)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars left join users ON cars.user_id = users.id;"
        results =  connectToMySQL(DATABASE).query_db(query)
        all_cars = []
        for row in results:
            cars = ( cls(row) )
            cars.seller = f"{row['first_name']} {row['last_name']}"
            all_cars.append(cars)
        return all_cars
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars left join users on cars.user_id = users.id where cars.id= %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results[0])
        return ( results[0] )
    

    @classmethod
    def update(cls, data):
        query = """UPDATE cars SET price=%(price)s, model=%(model)s, make=%(make)s, 
                year=%(year)s, description=%(description)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_car(car):
        is_valid = True
        if int(car['price']) <= 0:
            is_valid = False
            flash("price must be greater than zero","car")
        if len(car['model']) < 2:
            is_valid = False
            flash("model must be at least 2 characters","car")
        if len(car['make']) < 2:
            flash("make must be at least 2 characters","car")
            is_valid = False
        if int(car['year']) <= 0:
            flash("year must be greater than zero","car")
            is_valid = False
        if len(car['description']) < 3:
            flash("Description must be at least 3 characters","car")
            is_valid = False
        return is_valid