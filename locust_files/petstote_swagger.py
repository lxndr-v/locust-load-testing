from locust import HttpUser, task, between

import random


statuses = ["available", "pending", "sold"]
categories = ["dogs", "cats", "birds"]
tags_numbers = [42, 87, 15, 63, 29, 55, 91, 37, 10, 78, 52, 24, 68, 19, 36]

funny_animals = [
    'Fluffy McFlufferson',
    'Wigglesnort',
    'Squigglepaws',
    'Snickerdoodle',
    'Banana Buns',
    'Noodle the Poodle',
    'Whiskerface',
    'Sir Quacksalot',
    'Fuzzy Wuzzy',
    'Bumblebee Butt',
    'Silly Goose',
    'Cheesy Meowster',
    'Wobblebottom',
    'Sausage the Squirrel',
    'Mr. Bubbles'
]
user_names = [
    ('Bubbles McSnort Snorty'),
    ('Silly Pants Pantsy'),
    ('Wobblebottom McGiggles Wobbly'),
    ('Flapdoodle McFiddlesticks Doodle'),
    ('Cheesy McSneeze Sneezy'),
    ('Wacky Wobble Wacky'),
    ('Snickerdoodle McFluff Snicker'),
    ('Bananarama Jones Banana'),
    ('Dr. Quackenstein Quacky'),
    ('Scooby Doozy Doozy'),
    ('Ticklemeister Smith Tickles'),
    ('Gigglepants McGee Giggles'),
    ('Noodle Noodleman Noodle'),
    ('Funky Monkey Funky'),
    ('Whoopee Cushion Whoopee')
]

telephone_numbers = [
    '555-1234',
    '555-5678',
    '555-9876',
    '555-4321',
    '555-2468',
    '555-1357',
    '555-8642',
    '555-3141',
    '555-6767',
    '555-0909',
    '555-7878',
    '555-2323',
    '555-4040',
    '555-8181',
    '555-9393'
]

first_names = [
    'Silly',
    'Wobblebottom',
    'Bubbles',
    'Flapdoodle',
    'Cheesy',
    'Wacky',
    'Snickerdoodle',
    'Bananarama',
    'Drake',
    'Scooby',
    'Ticklemeister',
    'Gigglepants',
    'Noodle',
    'Funky',
    'Whoopee'
]
second_names= [
    'Pants',
'McGiggles',
'McSnort',
'McFiddlesticks',
'McSneeze',
'Wobble',
'McFluff',
'Jones',
'Quackenstein',
'Doozy',
'Smith',
'McGee',
'Noodleman',
'Monkey',
'Cushion'
]
nicks= [
     'Pantsy',
 'Wobbly',
 'Snorty',
 'Doodle',
 'Sneezy',
 'Wacky',
 'Snicker',
 'Banana',
 'Quacky',
 'Doozy',
 'Tickles',
 'Giggles',
 'Noodle',
 'Funky',
 'Whoopee'
]







class HelloWorldUser(HttpUser):

    def on_start(self):
        self.pet_id = 1000
        self.user_id = 1000
        self.cust_wait_time = 900000
    
    @task
    def add_pet_post(self):
        pet_data = {
            "id": self.pet_id,
            "name": random.choice(funny_animals),
            "category": {
                "id": 1,
                "name": random.choice(categories)
            },
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": random.choice(tags_numbers),
                "name": "string"
                }
            ],
            "status": "available"
            }
        with self.client.post("/pet", json=pet_data, timeout=5, catch_response=True) as responce:
            if responce.elapsed.microseconds > self.cust_wait_time:
                responce.failure("Request took too long time!")
            else:
                print(responce.content)
                self.pet_id += 1
        wait_time = between(3, 20)


    @task
    def add_user_post(self):
        nickname=random.choice(nicks)
        user_data = {
            "id": 0,
            "username": nickname,
            "firstName": random.choice(first_names),
            "lastName": random.choice(second_names),
            "email": f"{nickname}@test.ua",
            "password": "test123",
            "phone": "none",
            "userStatus": 0
            }
        with self.client.post("/user", json=user_data, timeout=3, catch_response=True) as responce:
            if responce.elapsed.microseconds > self.cust_wait_time:
                responce.failure("Request took too long time!")
            else:
                print(responce.content)
                self.user_id += 1
        wait_time = between(5, 10)
        

    
    # @task
    # def update_user_put(self):
    #     nickname=random.choice(nicks)
    #     user_data = {
    #         "phone": random.choice(telephone_numbers),
    #         "userStatus": 0
    #         }
    #     with self.client.put(f"/user/{nickname}", json=user_data, timeout=7, catch_response=True) as responce:
    #         if responce.elapsed.microseconds > self.cust_wait_time:
    #             responce.failure("Request took too long time!")
    #         elif responce.status_code == 400:
    #             responce.failure("Invalid user supplied")
    #         elif responce.status_code == 404:
    #             responce.failure("User not found")
    #         else:
    #             print(responce.content)
                
    #     wait_time = between(2, 39)
        
    @task
    def delete_user(self):
        nickname=random.choice(nicks)
        with self.client.delete(f"/user/{nickname}", timeout=9, catch_response=True) as responce:
            if responce.elapsed.microseconds > self.cust_wait_time:
                responce.failure("Request took too long time!")
            elif responce.status_code == 400:
                responce.failure("Invalid user supplied")
            elif responce.status_code == 404:
                responce.failure("User not found")
            else:
                print(responce.content)
                
        wait_time = between(4, 36)


    # @task
    # def get_user(self):
    #     nickname=random.choice(nicks)
    #     with self.client.get(f"/user/{nickname}", catch_response=True) as responce:
    #         if responce.elapsed.microseconds > self.cust_wait_time:
    #             responce.failure("Request took too long time!")
    #         elif responce.status_code == 400:
    #             responce.failure("Invalid user supplied")
    #         elif responce.status_code == 404:
    #             responce.failure("User not found")
    #         else:
    #             print(responce.content)
                
    #     wait_time = between(1, 5)

    # @task
    # def get_pet_by_id(self):
    #     pet_id_to_find = random.choice(random.randrange(1000, self.pet_id))
    #     with self.client.get(f"/pet/{pet_id_to_find}", catch_response=True) as responce:
    #         if responce.elapsed.microseconds > self.cust_wait_time:
    #             responce.failure("Request took too long time!")
    #         elif responce.status_code == 400:
    #             responce.failure("Invalid ID supplied")
    #         elif responce.status_code == 404:
    #             responce.failure("Pet not found")
    #         else:
    #             print(responce.content)
                
    #     wait_time = between(1, 4)