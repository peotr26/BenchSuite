#! /bin/dash

cd Programs/glmark2 || exit
glmark2 | grep -w "glmark2 Score" > result.txt

sed -i '1s/.*glmark2 Score: //' result.txt