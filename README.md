adev runserver

## Import data
### Add header for csv file (on top of file)
  ```
  #constant measurement,forex
  #constant tag,symbol,EURUSD
  #constant tag,base,EUR
  #constant tag,quote,USD
  #datatype dateTime:2006-01-02 15:04,double,double,double,double,double
  time,open,high,low,close,volume

  .....
  2019-05-15 02:05,1.12052,1.12056,1.12038,1.12049,618
  ```
### Import data command
docker-compose exec influxdb influx write -b forexx \
  -o ukkc \
  -t 5Uq0C50lYpE9_SjCCDjMG3HF_1MpNm3627YUG0wU87mMQ27tG9oAyuxuwlRLZzWdcs0Qj7BsR2Vg1f3LIyEjFA== \
  -f /home/influxdb/data/EURUSD5.csv

docker-compose exec influxdb influx bucket create -n forexx \
  -o ukkc \
  -t 5Uq0C50lYpE9_SjCCDjMG3HF_1MpNm3627YUG0wU87mMQ27tG9oAyuxuwlRLZzWdcs0Qj7BsR2Vg1f3LIyEjFA==

### Install package
pip install package && pip freeze > requirements.txt

### Server information
- InfluxDB: http://localhost:8086
- websocket: http://localhost:8585


### Add new package
- Need to rebuild image to avoid missing package
  - docker-compose build server


### Mongodb import
mongoimport --host=127.0.0.1 --port=27020 --username=root --password 4yW9wCsNYNc3RYqh \
   --db=market --collection=forex --type=csv --upsertFields=datetime\
   --columnsHaveTypes --mode=upsert \
   --fields="datetime.date(2006-01-02 15:04),open.double(),high.double(),low.double(),close.double(),volume.double()" \
   --file=./data/EURUSD5_mongo.csv
