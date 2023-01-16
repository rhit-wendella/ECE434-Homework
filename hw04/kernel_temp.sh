#!/bin/bash

ADDR1=0x49
ADDR2=0x4a

echo tmp101 $ADDR1 > /sys/class/i2c-adapter/i2c-2/new_device
echo tmp101 $ADDR2 > /sys/class/i2c-adapter/i2c-2/new_device

TEMPERATURE1=`cat /sys/bus/i2c/devices/2-0049/hwmon/hwmon0/temp1_input`
TEMPERATURE2=`cat /sys/bus/i2c/devices/2-004a/hwmon/hwmon1/temp1_input`

echo "Temp 1 $(($TEMPERATURE1 / 1000)) degrees C"
echo "Temp 2 $(($TEMPERATURE2 / 1000)) degrees C"
echo "Temp 1 $((((($TEMPERATURE1 / 1000)*9)/5)+32)) degrees F"
echo "Temp 2 $((((($TEMPERATURE2 / 1000)*9)/5)+32)) degrees F"