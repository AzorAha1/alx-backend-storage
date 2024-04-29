read me file for no sql


Then you can directly replace this with (though note the recommendation below):

wget -qO- https://myrepo.example/myrepo.asc | sudo tee /etc/apt/trusted.gpg.d/myrepo.asc
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo tee /etc/apt/trusted.gpg.d/server-4.2.asc