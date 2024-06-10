CREATE TABLE fish(
	fish_class VARCHAR(15) PRIMARY KEY NOT NULL,
	fish VARCHAR(15) NOT NULL,
	daily_bag INT NOT NULL,
	min_length INT NOT NULL,
	max_length INT NOT NULL,
	possession VARCHAR(100) NOT NULL,
	exceptions VARCHAR(50),
	image_link VARCHAR (140) NOT NULL
	
);

INSERT INTO fish (fish_class, fish, daily_bag, min_length, max_length, possession, exceptions, image_link)
VALUES ('Largemouth_Bass', 'Largemouth Bass', 5, 14, 0, 'Special regulations may apply to certain waterbodies. Check exceptions to statewide limits.', 'Learn more about statewide exceptions here.', 'https://critter.science/wp-content/uploads/2020/04/lb1a-1180x520.jpg'),
('Smallmouth_Bass', 'Smallmouth Bass', 5, 14, 0, 'Special regulations may apply to certain waterbodies. Check exceptions to statewide limits.', 'Learn more about statewide exceptions here.', 'https://majorleaguefishing.com/wp-content/uploads/2023/06/05115855/Smallmouth-Bass-S-3819a-1000x500.jpg'),
('Cobia', 'Cobia', 1, 40, 0, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://www.sportfishingmag.com/uploads/2021/09/cobia-feature-13-1.jpg'),
('Black Crappie', 'Black Crappie', 25, 10, 0, 'Special regulations may apply to certain waterbodies. Check exceptions to statewide limits.', 'Learn more about statewide exceptions here.', 'https://assets.wired2fish.com/uploads/2023/02/crappie-underwater.webp'),
('King_Mackeral', 'King Mackerel', 3, 27, 0, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://www.sportfishingmag.com/uploads/2021/09/spf0513_king_5-1.jpg'),
('Red', 'Red Drum', 3, 20, 28, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://www.aces.edu/wp-content/uploads/2018/10/GettyImages-763163807.jpg'),
('Flounder', 'Flounder', 5, 15, 0, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://www.thefisherman.com/wp-content/uploads/2021/07/20210821-fluke-flounder-winter-flounder_68.jpg'),
('Trout', 'Trout', 3, 15, 20, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://paddlingmagazine-images.s3.amazonaws.com/2023/10/speckled-trout-0-jason-arnold.jpg'),
('Snook', 'Snook', 1, 24, 28, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://stuartangler.com/wp-content/uploads/2016/09/AR-150829513.jpg'),
('Tarpon', 'Tarpon', 1, 85, 0, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://cdn.shopify.com/s/files/1/0230/8793/9662/files/Picture4.jpg?v=1657734473'),
('Tripletail', 'Tripletail', 3, 17, 0, 'The possession limit is equal to double the bag limit unless otherwise noted.', '', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Lobotes_surinamensis_Gobius.jpg/1920px-Lobotes_surinamensis_Gobius.jpg');
