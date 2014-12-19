#!/bin/bash

sed '1,2000!d' modely.10.output > STS.output.answers-forums.txt
sed '2001,3500!d' modely.10.output > STS.output.answers-students.txt
sed '3501,5500!d' modely.10.output > STS.output.belief.txt
sed '5501,7000!d' modely.10.output > STS.output.headlines.txt
sed '7001,8500!d' modely.10.output > STS.output.images.txt
