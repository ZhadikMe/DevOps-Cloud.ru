Команды, которые использовались для пуша образа в регистри:

docker build -t echo-server .

docker tag echo-server zhadik/cloud:latest

docker login

docker push zhadik/cloud:latest