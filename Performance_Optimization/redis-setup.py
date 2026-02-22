import redis
r = redis.Redis(host = 'localhost' ,port = 6379,db=0)

try:
    if r.ping():
        print("Conneted to Redis!!")
except redis.ConnectionError:
    print("Redis Connectionf failed!!")
finally:
    print()

r.set('framework','FastAPI')
value = r.get('framework')
print(f"Stored values for framework is  : {value.decode()}")