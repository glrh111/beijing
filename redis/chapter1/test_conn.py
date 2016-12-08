import redis

conn = redis.StrictRedis(host='redis')

print conn.set('heihei', 1)

print conn.get('heihei')

