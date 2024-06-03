# python-service-zk
Connect to ZK Devices, download Users and Events and send to JSON-API over HTTP

usage: python-service-zk [-h] [--port PORT] [--timeout TIMEOUT] [--password PASSWORD] [--UDP | --no-UDP] [--ping | --no-ping] [--serial | --no-serial]
         [--time | --no-time] [--users | --no-users] [--records | --no-records]
         host URL


* Generate event id using event UNIXTime + USERId in 64bit int number
* Add device serial, time, timeOffset to adjust timeStamps
* Sync device time
