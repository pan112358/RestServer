# RestServer

This is a simple restful server with mysql as data storage.
Before you start, you should deploy a mysql server first, and get the access information ,including:

MYSQL_HOST

MYSQL_USER

MYSQL_PASSWORD

MYSQL_PORT

MYSQL_DB_NAME                            #the container can also create one, you can use the existing DB or a new one

MYSQL_TABLE_NAME                         #the container can also create one, you can use the existing table or a new one

SERVICE_KEYS                             #table structure, different keys are seperated by a space.

You should assign correct value for the above ENV parameters to your container when you create it.

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





这是一个简单的restful服务器，mysql作为数据存储。在开始之前，您应首先部署一个mysql服务器，并获取访问信息，包括：

MYSQL_HOST

MYSQL_USER

MYSQL_PASSWORD

MYSQL_PORT

MYSQL_DB_NAME                     #容器也可以创建一个，你可以使用现有的DB或指定一个新的DB名称

MYSQL_TABLE_NAME                  #容器也可以创建一个，您可以使用现有表或新表

SERVICE_KEYS                      #数据库表结构，不同的键由空格分隔。


在创建容器时，应将上述环境变量参数的正确值分配给容器。

服务端口5000用于容器中，并且支持下面的操作

#########创建/更新记录###########

方法：POST/PUT

API：/api/targets/$targetID

正文：使用form-data键值对（ENV SERVICE_KEYS中的一个或多个键）

################################################## ####

#########查询记录###############################

方法：GET

API：/api/targets/$targetID/$key

################################################## ####

#########删除记录###############################

方法：DELETE

API：/api/targets/$targetID

################################################## ####
