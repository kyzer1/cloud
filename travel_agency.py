import redis
import json

redis_connection = redis.Redis("localhost", "6379", charset="utf-8", decode_responses=True, db=4)


def user_creator(name, phone_number, age):
    redis_connection.hset(f"user:{name}",mapping={"name":name,"phonenumber":phone_number,"age":age})
    print("done!!!")


def trip_creator(start, destination, time, vehicle, users):
    passengers = {}

    while True:
        i = 0
        for elm in users.split(","):
                passengers[i] = redis_connection.hgetall(f"user:{elm}")
                i+=1
        else:
            break
        
    redis_connection.hset(f"trip:{start}:{destination}:{time}",mapping={"start":start,"destination":destination,
    "time":time,"vehicle":vehicle,"user":json.dumps(passengers)})

    print("done!!!")


def tour_creator(leader, users, days, price, start, destination, details):
    passengers = {}

    while True:
        i = 0
        for elm in users.split(","):
                passengers[i] = redis_connection.hgetall(f"user:{elm}")
                i+=1
        else:
            break

    redis_connection.hset(f"tour:{leader}:{start}:{destination}", mapping={"leader":leader, "user":json.dumps(passengers), "days":days,"price":price,
    "start":start, "destination":destination, "details":details})

    print("done!!!")


def show_user(name):

    return (redis_connection.hgetall(f"user:{name}"))


def show_trip(start, destination, time):
    return (redis_connection.hgetall(f"trip:{start}:{destination}:{time}"))

def show_tour(start, destination, leader):
    return (redis_connection.hgetall(f"tour:{leader}:{start}:{destination}"))
        