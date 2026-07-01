import time
import json
import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def call_weather_api(city):
    """
    Simulasi API call yang lambat.
    Anggap ini seperti mengambil data dari API asli.
    """
    time.sleep(2)

    return {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }


def get_weather(city):
    """
    Fungsi ini menggunakan Redis caching.
    Jika data ada di cache, data langsung diambil dari Redis.
    Jika tidak ada, program akan mengambil data dari API,
    lalu menyimpannya ke Redis selama 300 detik.
    """

    cache_key = f"weather:{city.lower()}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Data diambil dari Redis cache")
        return json.loads(cached_data)

    print("Cache kosong, mengambil data dari API...")
    weather_data = call_weather_api(city)

    redis_client.set(cache_key, json.dumps(weather_data))
    redis_client.expire(cache_key, 300)

    return weather_data