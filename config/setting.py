import os

influxdb = {
    "url": os.environ['INFLUXDB_URL'],
    "username": os.environ['INFLUXDB_USERNAME'],
    "password": os.environ['INFLUXDB_PASSWORD'],
    "token": os.environ['INFLUXDB_TOKEN'],
    "org": os.environ['INFLUXDB_ORG'],
    "forex_bucket": os.environ['INFLUXDB_FOREX_BUCKET']
}

mongodb = {
    "host": os.environ['MONGO_HOST'],
    "username": os.environ['MONGO_USERNAME'],
    "password": os.environ['MONGO_PASSWORD'],
    "database": os.environ['MONGO_DATABASE'],
    "port": os.environ['MONGO_PORT'],
    "collection": os.environ['MONGO_COLLECTION'],
    "symbol": os.environ['MONGO_SYMBOL']
}
