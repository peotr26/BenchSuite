#! /bin/dash

cd Programs/vkmark || exit
vkmark | grep -w "vkmark Score" > result.txt

sed -i '1s/.*vkmark Score: //' result.txt 
