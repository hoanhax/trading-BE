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
docker-compose exec influxdb influx write -b forex \
  -o ukkc \
  -t 5Uq0C50lYpE9_SjCCDjMG3HF_1MpNm3627YUG0wU87mMQ27tG9oAyuxuwlRLZzWdcs0Qj7BsR2Vg1f3LIyEjFA== \
  -f /home/influxdb/data/EURUSD5.csv

### Install package
pip install package && pip freeze > requirements.txt

### Server information
- InfluxDB: http://localhost:8086
- websocket: http://localhost:8585


### Add new package
- Need to rebuild image to avoid missing package
  - docker-compose build server
