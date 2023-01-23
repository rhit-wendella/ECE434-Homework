#!/bin/bash


TEMPERATURE1=`cat /sys/class/hwmon/hwmon0/temp1_input`
TEMPERATURE2=`cat /sys/class/hwmon/hwmon1/temp1_input`
TEMPERATURE3=`cat /sys/class/hwmon/hwmon2/temp1_input`

echo "Temp 1 $(($TEMPERATURE1 / 1000)) degrees C"
echo "Temp 2 $(($TEMPERATURE2 / 1000)) degrees C"
echo "Temp 2 $(($TEMPERATURE3 / 1000)) degrees C"
echo "Temp 1 $((((($TEMPERATURE1 / 1000)*9)/5)+32)) degrees F"
echo "Temp 2 $((((($TEMPERATURE2 / 1000)*9)/5)+32)) degrees F"
echo "Temp 2 $((((($TEMPERATURE3 / 1000)*9)/5)+32)) degrees F"
