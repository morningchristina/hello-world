#!/bin/bash
clear
echo "knowledge is power";

r=$(( $RANDOM % 10 +40));
echo $r;

test=$(curl "google.com")
echo $test
