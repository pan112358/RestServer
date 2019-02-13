# RestServer

This is a simple restful server with mysql as data storage.
Before you start, you should deploy a mysql server first, and get the access information ,including:

MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_PORT
MYSQL_DB_NAME
MYSQL_TABLE_NAME
SERVICE_KEYS  #table structure, different keys are seperated by a space.

You should assign correct value for the above ENV parameters to your container when you create it.

When start the container, you should use /opt/FlaskServer/start.sh command as the start command.

Port 5000 is used in the container, and below operation are supported


#########Create/Update records###########

Method: POST/PUT

API: /api/targets/$targetID

Body: with form-data key,value pairs(one or multipule keys from ENV SERVICE_KEYS)

######################################################

#########Query records###############################

Method: GET

API: /api/targets/$targetID/$key


######################################################



#########Delete records###############################

Method: DELETE

API: /api/targets/$targetID


######################################################
