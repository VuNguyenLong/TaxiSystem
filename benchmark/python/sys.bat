@echo off
start cmd /C java -jar Host.jar | start cmd /C java -jar Worker.jar packdb config/packdb.properties | start cmd /C java -jar Worker.jar packdb config/packdb1.properties | start cmd /C java -jar Worker.jar packdb config/packdb2.properties