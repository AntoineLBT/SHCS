DROP TABLE IF EXISTS Possess;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Clothe;

CREATE TABLE `Possess` (
	`Customer_ID`	INTEGER NOT NULL,
	`Clothe_ID`	INTEGER NOT NULL UNIQUE
);
CREATE TABLE `Customer` (
	`Customer_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Money`	INTEGER,
	`Last_Name`	TEXT,
	`First_Name`	INTEGER,
	`Contact`	TEXT
);

CREATE TABLE `Clothe` (
	`Clothe_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Color`	TEXT,
	`Size`	CHAR[4],
	`Date`	DATE,
	`Type`	TEXT,
	`Price`	INTEGER
);

INSERT INTO Clothe VALUES (1, "BLACK", 'L', '2018-04-18', 'Pant', 20);
INSERT INTO Clothe (Color, Size, Date, Type, Price) VALUES ("YELLOW", 'L', '2018-04-18', 'T-Shirt', 10);
INSERT INTO Clothe (Color, Size, Date, Type, Price) VALUES ("WHITE", 'S', '2018-04-18', 'T-Shirt', 5);
INSERT INTO Clothe (Color, Size, Date, Type, Price) VALUES ("PINK", 'XS', '2018-04-18', 'T-Shirt', 30);
INSERT INTO Clothe (Color, Size, Date, Type, Price) VALUES ("BLACK", 'XXL', '2018-04-18', 'Hat', 50);
INSERT INTO Clothe (Color, Size, Date, Type, Price) VALUES ("MULTI", 'L', '2018-04-18', 'HAT', 100);

INSERT INTO Customer VALUES (1, 0, 'Jean', 'Dujardin', '15 rue du chou fleur');
INSERT INTO Customer (Money, Last_Name, First_Name, Contact) VALUES (0, 'Jean', 'Briac', '8 rue du potiron');

INSERT INTO Possess VALUES (1, 1);
INSERT INTO Possess VALUES (1, 2);
INSERT INTO Possess VALUES (1, 3);
INSERT INTO Possess VALUES (2, 4);
INSERT INTO Possess VALUES (2, 5);
INSERT INTO Possess VALUES (2, 6);

COMMIT;
