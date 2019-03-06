To execute this program:
docker-compose up -d <br>
Writes into file called "text.txt" in Consumer. To see this write: <br>
docker exec -it $(docker ps | grep consumer | grep -Po "[0-9a-z]{12}") bash <br>
(In case of error --- wait for 10 sec and write again) <br>
watch cat text.txt
