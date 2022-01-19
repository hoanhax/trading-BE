import os

influxdb = {
    "url": os.environ['INFLUXDB_URL'],
    "username": os.environ['INFLUXDB_USERNAME'],
    "password": os.environ['INFLUXDB_PASSWORD'],
    "token": os.environ['INFLUXDB_TOKEN'],
    "org": os.environ['INFLUXDB_ORG'],
    "forex_bucket": os.environ['INFLUXDB_FOREX_BUCKET']
}
