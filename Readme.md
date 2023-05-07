# build

docker build -t form . 

# run

docker run -ti -p 80:80 form

open 127.0.0.1 in browser

# develop

add `-v ${PWD}/app:/opt/app` to docker run
