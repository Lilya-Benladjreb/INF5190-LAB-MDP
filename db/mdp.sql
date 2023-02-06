create table user (
  id integer primary key,
  nom varchar(25),
  prenom varchar(25),
  courriel varchar(100),
  inscription date,
  salt varchar(32),
  hash varchar(128)
);

