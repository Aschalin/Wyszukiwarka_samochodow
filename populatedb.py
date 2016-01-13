#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

def marki():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_marki` (
                    `id` int(11) NOT NULL  AUTO_INCREMENT,
                    `Marka` varchar(30) NOT NULL,
                    `Kraj` varchar(30) NOT NULL,
                    `WWW` varchar(200) NOT NULL,
                    PRIMARY KEY (id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """)
    cur.execute("""INSERT INTO `wyszukiwarka_marki` (`id`, `Marka`, `Kraj`, `WWW`) VALUES
                    (1, 'Audi', 'Niemcy', 'www.audi.pl'),
                    (2, 'Ford', 'USA', 'www.ford.pl');
                    """)

def samochody():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_samochody` (
                    `id` int(11) NOT NULL,
                    `Model` varchar(30) NOT NULL,
                    `Rocznik` int(11) NOT NULL,
                    `Cena` int(11) NOT NULL,
                    `idMarka` int(11) NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY (idMarka) REFERENCES wyszukiwarka_marki(id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """);
    cur.execute("""INSERT INTO `wyszukiwarka_samochody` (`id`, `Model`, `Rocznik`, `Cena`, `idMarka`) VALUES
                    (12, 'Tourneo Courier', 2015, 57503, 2),
                    (11, 'Tourneo Connect', 2015, 70602, 2),
                    (10, 'S-Max', 2015, 106600, 2),
                    (9, 'Mustang', 2015, 148400, 2),
                    (8, 'Mondeo', 2015, 90000, 2),
                    (7, 'Kuga', 2015, 101800, 2),
                    (6, 'Ka', 2015, 30700, 2),
                    (5, 'Galaxy', 2015, 111400, 2),
                    (4, 'Focus', 2015, 63690, 2),
                    (3, 'Fiesta', 2015, 40780, 2),
                    (2, 'C-Max', 2015, 68100, 2),
                    (1, 'B-Max', 2015, 54950, 2),
                    (13, 'A1', 2015, 76300, 1),
                    (14, 'A3', 2015, 90300, 1),
                    (15, 'A4', 2015, 130800, 1),
                    (16, 'A5', 2015, 137600, 1),
                    (17, 'A6', 2015, 180800, 1),
                    (18, 'A7', 2015, 224300, 1),
                    (19, 'A8', 2015, 365600, 1),
                    (20, 'Q3', 2015, 123000, 1),
                    (21, 'Q5', 2015, 145700, 1),
                    (22, 'Q7', 2015, 270200, 1),
                    (23, 'TT', 2015, 161600, 1),
                    (24, 'R8', 2015, 790800, 1);
                    """)

def nadwozia():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_nadwozia` (
                    `id` int(11) NOT NULL,
                    `Rodzaj` varchar(30) NOT NULL,
                    `Oplata` int(11) NOT NULL,
                    `idSamochod` int(11) NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY (idSamochod) REFERENCES wyszukiwarka_samochody(id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """)

    cur.execute("""INSERT INTO `wyszukiwarka_nadwozia` (`id`, `Rodzaj`, `Oplata`, `idSamochod`) VALUES
                    (25, 'A1 Sportback', 0, 13),
                    (24, '5-drzwiowe', 0, 12),
                    (23, 'Standard', 0, 11),
                    (22, 'Grand', 7749, 11),
                    (21, 'MiniVan', 0, 10),
                    (20, 'Fastback', 0, 9),
                    (19, 'Convertible', 17000, 9),
                    (18, 'Sedan', 39700, 8),
                    (17, 'Kombi', 4000, 8),
                    (16, 'Hatchback', 0, 8),
                    (15, '5-drzwiowe', 0, 7),
                    (14, '3-drzwiowe', 0, 6),
                    (13, 'MiniVan', 0, 5),
                    (12, 'ST Kombi', 55310, 4),
                    (11, 'ST', 52310, 4),
                    (10, 'Sedan', 1000, 4),
                    (9, 'Kombi', 3000, 4),
                    (8, 'Hatchback 5d', 0, 4),
                    (7, 'Van', 0, 3),
                    (6, 'ST', 34620, 3),
                    (5, 'Hatchback 5d', 5320, 3),
                    (4, 'Hatchback 3d', 4320, 3),
                    (3, 'MiniVan', 0, 2),
                    (2, 'Grand', 4050, 2),
                    (1, 'MiniVan', 0, 1),
                    (27, 'Cabriolet', 44100, 14),
                    (28, 'Hatchback 3d', 0, 14),
                    (29, 'Limousine', 13600, 14),
                    (30, 'RS3 Sportback', 166700, 14),
                    (31, 'S3 ', 72800, 14),
                    (32, 'S3 Cabriolet', 111700, 14),
                    (33, 'S3 Limousine', 79000, 14),
                    (34, 'S3 Sportback', 76800, 14),
                    (35, 'Sportback 5d', 4100, 14),
                    (36, 'Sportback e-tron', 82000, 14),
                    (37, 'Limuzyna', 0, 15),
                    (38, 'Avant', 16300, 15),
                    (39, 'Cabrio', 34500, 16),
                    (40, 'Coupe', 13800, 16),
                    (41, 'RS5 Cabriolet', 312000, 16),
                    (42, 'RS5 Coupe ', 255800, 16),
                    (43, 'S5 Cabrio', 162100, 16),
                    (44, 'S5 Coupe', 154600, 16),
                    (45, 'S5 Sportback', 150300, 16),
                    (46, 'Sportback', 0, 16),
                    (47, 'Limousine', 0, 17),
                    (48, 'Allroad quattro', 94400, 17),
                    (49, 'Avant', 11600, 17),
                    (50, 'RS6 Avant', 352100, 17),
                    (51, 'S6 Avant', 224200, 17),
                    (52, 'S6 Limousine', 209200, 17),
                    (53, 'A7 Sportback', 0, 18),
                    (54, 'RS7 Sportback', 333600, 18),
                    (55, 'S7 Sportback', 197100, 18),
                    (56, 'Lang', 23100, 19),
                    (57, 'S8', 194300, 19),
                    (58, 'Sedan', 0, 19),
                    (59, 'W12 Lang', 278200, 19),
                    (60, 'SUV', 0, 20),
                    (61, 'RS Q3', 122000, 20),
                    (62, 'SUV', 0, 21),
                    (63, 'SQ5', 139000, 21),
                    (64, 'Terenowy', 0, 22),
                    (65, 'Coupe', 0, 23),
                    (66, 'Coupe TTS', 51000, 23),
                    (67, 'Roadster', 13500, 23),
                    (68, 'Roadster TTS', 64500, 23),
                    (26, '2-drzwiowe', 0, 24);
                    """)

def silniki():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_silniki` (
                    `id` int(11) NOT NULL,
                    `Rodzaj` varchar(10) NOT NULL,
                    `Paliwo` varchar(1) NOT NULL,
                    `Pojemnosc` double NOT NULL,
                    `KM` int(11) NOT NULL,
                    PRIMARY KEY (id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """)
    cur.execute("""INSERT INTO `wyszukiwarka_silniki` (`id`, `Rodzaj`, `Paliwo`, `Pojemnosc`, `KM`) VALUES
                    (1, 'TFSI ultra', 'B', 1, 95),
                    (2, 'TFSI', 'B', 1.2, 110),
                    (3, 'TFSI', 'B', 1.4, 125),
                    (4, 'TFSI', 'B', 1.4, 150),
                    (5, 'TFSI CoD', 'B', 1.4, 150),
                    (6, 'TFSI CoD u', 'B', 1.4, 150),
                    (7, 'TFSI', 'B', 1.8, 144),
                    (8, 'TFSI', 'B', 1.8, 170),
                    (9, 'TFSI', 'B', 1.8, 180),
                    (10, 'TFSI', 'B', 1.8, 190),
                    (11, 'TFSI ultra', 'B', 1.8, 190),
                    (12, 'TFSI', 'B', 2, 180),
                    (13, 'TFSI ultra', 'B', 2, 190),
                    (14, 'TFSI', 'B', 2, 220),
                    (15, 'TFSI', 'B', 2, 225),
                    (16, 'TFSI', 'B', 2, 252),
                    (17, 'TFSI', 'B', 3, 272),
                    (18, 'TFSI', 'B', 3, 310),
                    (19, 'TFSI', 'B', 3, 333),
                    (20, 'TFSI', 'B', 4, 435),
                    (21, 'TSI', 'B', 2, 230),
                    (22, 'EcoBoost', 'B', 1, 100),
                    (23, 'EcoBoost', 'B', 1, 125),
                    (24, 'EcoBoost', 'B', 1, 140),
                    (25, 'EcoBoost', 'B', 1.5, 150),
                    (26, 'EcoBoost', 'B', 1.5, 160),
                    (27, 'EcoBoost', 'B', 1.5, 182),
                    (28, 'EcoBoost', 'B', 2, 203),
                    (29, 'EcoBoost', 'B', 2, 240),
                    (30, 'EcoBoost', 'B', 2.3, 317),
                    (31, 'Ti-VCT', 'B', 1.6, 85),
                    (32, 'Ti-VCT', 'B', 1.6, 105),
                    (33, 'Ti-VCT', 'B', 1.6, 125),
                    (34, 'Ti-VCT', 'B', 5, 421),
                    (35, 'Duratec', 'B', 1.2, 69),
                    (36, 'Duratec', 'B', 1.25, 60),
                    (37, 'Duratec', 'B', 1.25, 82),
                    (38, 'Duratec', 'B', 1.4, 90),
                    (39, 'Duratec', 'B', 1.4, 96),
                    (40, 'Duratec', 'B', 1.6, 105),
                    (41, 'Duratec Ti', 'B', 1.6, 105),
                    (42, 'Duratec', 'D', 1.25, 60),
                    (43, 'Duratorq T', 'D', 1.5, 75),
                    (44, 'Duratorq T', 'D', 1.6, 95),
                    (45, 'TDCi', 'D', 1.5, 95),
                    (46, 'TDCi', 'D', 1.5, 120),
                    (47, 'TDCi', 'D', 1.6, 95),
                    (48, 'TDCi', 'D', 1.6, 115),
                    (49, 'TDCi', 'D', 2, 150),
                    (50, 'TDCi', 'D', 2, 170),
                    (51, 'TDCi', 'D', 2, 180),
                    (52, 'TDCi ECOne', 'D', 1.5, 105),
                    (53, 'TDCi ECOne', 'D', 1.5, 120),
                    (54, 'TDCi ECOne', 'D', 1.6, 115),
                    (55, 'TDCi ECOne', 'D', 2, 150),
                    (56, 'TDCi Bi-Tu', 'D', 2, 210),
                    (57, 'Hybrid', 'D', 2, 187),
                    (58, 'TDI ultra', 'D', 1.4, 90),
                    (59, 'TDI ultra', 'D', 1.6, 110),
                    (60, 'TDI clean ', 'D', 1.6, 110),
                    (61, 'TDI', 'D', 1.6, 116),
                    (62, 'TDI', 'D', 2, 120),
                    (63, 'TDI', 'D', 2, 136),
                    (64, 'TDI ultra', 'D', 2, 136),
                    (65, 'TDI', 'D', 2, 150),
                    (66, 'TDI ultra', 'D', 2, 150),
                    (67, 'TDI clean ', 'D', 2, 150),
                    (68, 'TDI ultra', 'D', 2, 163),
                    (69, 'TDI', 'D', 2, 177),
                    (70, 'TDI', 'D', 2, 184),
                    (71, 'TDI ultra', 'D', 2, 184),
                    (72, 'TDI clean ', 'D', 2, 184),
                    (73, 'TDI', 'D', 2, 190),
                    (74, 'TDI ultra', 'D', 2, 190),
                    (75, 'TDI clean ', 'D', 2, 190),
                    (76, 'TDI', 'D', 3, 204),
                    (77, 'TDI ultra', 'D', 3, 218),
                    (78, 'TDI clean ', 'D', 3, 218),
                    (79, 'TDI', 'D', 3, 245),
                    (80, 'TDI clean ', 'D', 3, 245),
                    (81, 'TDI clean ', 'D', 3, 258),
                    (82, 'TDI', 'D', 3, 272),
                    (83, 'TDI clean ', 'D', 3, 272),
                    (84, 'TDI clean ', 'D', 3, 320),
                    (85, 'TDI compet', 'D', 3, 326),
                    (86, 'TDI clean ', 'D', 4.2, 435),
                    (87, 'EcoBoost', 'B', 1, 80),
                    (88, 'EcoBoost', 'B', 2, 250),
                    (89, 'TDCi', 'D', 2, 185),
                    (90, 'EcoBoost', 'B', 1.6, 150),
                    (91, 'Duratorq T', 'D', 1.6, 75),
                    (92, 'Duratorq T', 'D', 1.6, 115),
                    (93, 'TDCi', 'D', 1.5, 75),
                    (94, 'V10', 'B', 5.2, 540),
                    (95, 'V10 Plus', 'B', 5.2, 610),
                    (96, 'TFSI', 'B', 2.5, 367),
                    (97, 'TFSI', 'B', 2, 300),
                    (98, 'TFSI etron', 'B', 1.4, 204),
                    (99, 'FSI', 'B', 4.2, 450),
                    (100, 'TFSI', 'B', 4, 560),
                    (101, 'TFSI', 'B', 4, 450),
                    (102, 'TDI Clean', 'D', 4.2, 385),
                    (103, 'TFSI', 'B', 4, 520),
                    (104, 'FSI', 'B', 6.3, 500),
                    (105, 'TFSI', 'B', 2.5, 340),
                    (106, 'TDI', 'D', 3, 313),
                    (107, 'TFSI', 'B', 2, 310);
                    """)

def silnikiNadwozia():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_silniki_nadwozia` (
                    `id` int(11) NOT NULL,
                    `Spalanie` double NOT NULL,
                    `Przyspieszenie` double NOT NULL,
                    `VMax` int(11) NOT NULL,
                    `Oplata` int(11) NOT NULL,
                    `idNadwozie` int(11) NOT NULL,
                    `idSilnik` int(11) NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY (idNadwozie) REFERENCES wyszukiwarka_nadwozia(id),
                    FOREIGN KEY (idSilnik) REFERENCES wyszukiwarka_silniki(id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """)
    cur.execute("""INSERT INTO `wyszukiwarka_silniki_nadwozia` (`id`, `Spalanie`, `Przyspieszenie`, `VMax`, `Oplata`, `idNadwozie`, `idSilnik`) VALUES
                    (106, 7.3, 7.9, 240, 45700, 16, 29),
                    (105, 7.3, 8.7, 232, 38300, 16, 28),
                    (104, 5.8, 9.2, 222, 3300, 16, 26),
                    (103, 5.2, 9.2, 202, 22150, 15, 51),
                    (102, 4.7, 10.1, 194, 8650, 15, 49),
                    (101, 7.4, 10.1, 200, 18650, 15, 27),
                    (100, 6.2, 9.7, 195, 0, 15, 25),
                    (109, 4.4, 9.3, 215, 13300, 16, 49),
                    (99, 4.9, 13.2, 159, 0, 14, 35),
                    (98, 5.5, 8.5, 214, 43200, 13, 56),
                    (97, 5, 10.8, 195, 12000, 13, 49),
                    (96, 5, 10.8, 195, 18000, 13, 51),
                    (95, 7.9, 8.4, 222, 25000, 13, 29),
                    (94, 6.5, 9.9, 190, 0, 13, 26),
                    (93, 4.2, 8.1, 217, 1500, 12, 89),
                    (92, 6.8, 6.5, 248, 0, 12, 88),
                    (91, 4.2, 8.1, 217, 1500, 11, 89),
                    (90, 6.8, 6.5, 248, 0, 11, 88),
                    (89, 4.1, 8.9, 210, 20750, 9, 49),
                    (88, 4.2, 10.9, 193, 14000, 9, 48),
                    (87, 4.2, 12.6, 180, 11000, 9, 45),
                    (86, 3.8, 10.5, 193, 16450, 9, 46),
                    (85, 3.4, 12.1, 187, 13300, 9, 52),
                    (84, 3.8, 12.1, 180, 12700, 9, 45),
                    (83, 5.9, 10.9, 190, 6000, 9, 33),
                    (82, 6, 12.3, 180, 3000, 9, 32),
                    (81, 6, 15, 170, 0, 9, 31),
                    (80, 5.9, 8.8, 222, 19650, 9, 27),
                    (79, 5.6, 9.1, 210, 11450, 9, 25),
                    (78, 4.8, 11.1, 195, 8500, 9, 23),
                    (77, 4.8, 12.6, 187, 5000, 9, 22),
                    (76, 4.1, 8.9, 210, 20750, 8, 49),
                    (75, 4.2, 10.9, 193, 14000, 8, 48),
                    (74, 4.2, 12.5, 180, 11000, 8, 47),
                    (73, 3.8, 10.5, 193, 16450, 8, 46),
                    (72, 3.4, 12.1, 187, 13300, 8, 52),
                    (71, 3.8, 12.0, 180, 12700, 8, 45),
                    (70, 5.9, 10.9, 190, 6000, 8, 33),
                    (69, 6, 12.3, 180, 3000, 8, 32),
                    (68, 6, 15, 170, 0, 8, 31),
                    (67, 5.9, 8.8, 222, 19650, 8, 27),
                    (66, 5.6, 9.1, 210, 11450, 8, 25),
                    (65, 4.8, 11.1, 195, 8500, 8, 23),
                    (64, 4.8, 12.6, 187, 5000, 8, 22),
                    (63, 4.1, 8.9, 210, 20750, 10, 49),
                    (62, 4.2, 10.9, 193, 14000, 10, 48),
                    (61, 4.2, 12.6, 180, 11000, 10, 47),
                    (60, 3.8, 10.5, 193, 16450, 10, 46),
                    (59, 3.4, 12.1, 187, 13300, 10, 52),
                    (58, 3.8, 12.1, 180, 12700, 10, 45),
                    (57, 5.9, 10.9, 190, 6000, 10, 33),
                    (56, 6, 12.3, 180, 3000, 10, 32),
                    (55, 6, 15, 170, 0, 10, 31),
                    (54, 5.9, 8.8, 222, 19650, 10, 27),
                    (53, 5.6, 9.1, 210, 11450, 10, 25),
                    (52, 4.8, 11.1, 195, 8500, 10, 23),
                    (51, 4.8, 12.6, 187, 5000, 10, 22),
                    (50, 3.6, 11.7, 181, 6890, 7, 44),
                    (49, 3.7, 13.5, 167, 5790, 7, 43),
                    (48, 5.2, 13.3, 168, 0, 7, 37),
                    (47, 4.3, 14.9, 165, 5170, 7, 87),
                    (46, 5.9, 6.9, 223, 0, 6, 27),
                    (45, 3.6, 11.7, 181, 12000, 5, 44),
                    (44, 3.7, 13.5, 167, 8650, 5, 43),
                    (43, 4.2, 14.9, 162, 0, 5, 42),
                    (42, 5.9, 10.5, 184, 15100, 5, 40),
                    (41, 5.7, 12.2, 175, 5150, 5, 39),
                    (40, 5.2, 13.3, 168, 2500, 5, 37),
                    (39, 4.3, 9.4, 196, 17050, 5, 23),
                    (38, 4.5, 11.2, 180, 7200, 5, 22),
                    (37, 3.6, 11.7, 181, 12000, 4, 44),
                    (36, 3.7, 13.5, 167, 8650, 4, 43),
                    (35, 5.9, 10.5, 184, 15100, 4, 40),
                    (34, 5.7, 12.2, 175, 5150, 4, 39),
                    (33, 5.2, 13.3, 168, 2500, 4, 37),
                    (32, 5.2, 16.9, 152, 0, 4, 36),
                    (31, 4.5, 9, 201, 22450, 4, 24),
                    (30, 4.3, 9.4, 196, 17050, 4, 23),
                    (29, 4.5, 11.2, 180, 7200, 4, 22),
                    (28, 5, 8.8, 209, 40450, 2, 50),
                    (27, 4.6, 9.8, 202, 20750, 2, 49),
                    (26, 4.4, 12.3, 180, 16450, 2, 53),
                    (25, 3.8, 12.1, 184, 13600, 2, 52),
                    (24, 4.4, 14.3, 166, 12700, 2, 45),
                    (23, 5.5, 12.3, 185, 6000, 2, 33),
                    (22, 6.4, 15.7, 165, 0, 2, 31),
                    (21, 6.8, 9.5, 211, 26250, 2, 27),
                    (20, 6.3, 9.7, 202, 12450, 2, 25),
                    (19, 5.2, 12.2, 185, 8500, 2, 23),
                    (18, 5.2, 13.6, 172, 5500, 2, 22),
                    (17, 4.8, 8.5, 212, 40450, 3, 50),
                    (16, 4.4, 9.2, 204, 20750, 3, 49),
                    (15, 4.1, 11.3, 184, 16450, 3, 53),
                    (14, 3.8, 12.1, 184, 13600, 3, 52),
                    (13, 4.1, 13.3, 170, 12700, 3, 45),
                    (12, 5.5, 11.5, 188, 6000, 3, 33),
                    (11, 6.4, 15.7, 165, 0, 3, 31),
                    (10, 6.5, 9.2, 213, 26250, 3, 27),
                    (9, 6.1, 9.4, 204, 12450, 3, 25),
                    (8, 5.1, 11.4, 187, 8500, 3, 23),
                    (7, 5.1, 12.6, 174, 5500, 3, 22),
                    (6, 4, 13.9, 173, 15200, 1, 44),
                    (5, 4.1, 16.5, 157, 8500, 1, 43),
                    (4, 6.4, 12.1, 180, 15200, 1, 40),
                    (3, 6, 13.8, 171, 0, 1, 38),
                    (2, 4.9, 11.2, 189, 8800, 1, 23),
                    (1, 5.1, 13.2, 175, 1100, 1, 22),
                    (107, 5.1, 12, 200, 0, 16, 23),
                    (108, 3.6, 12.1, 192, 9300, 16, 54),
                    (110, 4.1, 9.4, 215, 19900, 16, 55),
                    (111, 4, 11.5, 192, 24100, 16, 46),
                    (112, 3.6, 11.7, 192, 27000, 16, 53),
                    (113, 4.8, 7.9, 233, 51700, 16, 56),
                    (114, 5.9, 9.3, 217, 3300, 17, 26),
                    (115, 7.5, 8.8, 227, 38300, 17, 28),
                    (116, 7.5, 8, 235, 45700, 17, 29),
                    (117, 5.1, 12, 200, 0, 17, 23),
                    (118, 4.5, 9.4, 210, 13300, 17, 49),
                    (119, 4.1, 9.4, 215, 19900, 17, 55),
                    (120, 4.5, 8.4, 220, 23000, 17, 51),
                    (121, 4, 11.5, 192, 9300, 17, 46),
                    (122, 3.6, 11.7, 192, 12200, 17, 53),
                    (123, 4.2, 9.2, 187, 0, 18, 57),
                    (124, 8.2, 0, 234, 0, 19, 30),
                    (125, 13.6, 0, 250, 21000, 19, 34),
                    (126, 8, 0, 234, 0, 20, 30),
                    (127, 13.5, 0, 250, 21000, 20, 34),
                    (128, 6.5, 9.9, 200, 0, 21, 26),
                    (129, 7.9, 8.4, 226, 25000, 21, 29),
                    (130, 5, 13.4, 186, 6000, 21, 46),
                    (131, 5, 10.8, 198, 12000, 21, 49),
                    (132, 5, 9.7, 211, 18000, 21, 51),
                    (133, 5.5, 8.8, 218, 41200, 21, 56),
                    (134, 8, 10.9, 173, 8672, 22, 90),
                    (135, 4, 17.8, 145, 0, 22, 91),
                    (136, 4, 14.7, 160, 5597, 22, 44),
                    (137, 4, 13, 165, 7319, 22, 92),
                    (138, 5.6, 14, 165, 0, 23, 22),
                    (139, 8, 10.9, 173, 12731, 23, 90),
                    (140, 4, 14.7, 160, 9656, 23, 44),
                    (141, 4.8, 14.8, 165, 11378, 23, 92),
                    (142, 4.9, 0, 0, 0, 24, 22),
                    (143, 3.9, 0, 0, 4305, 24, 93),
                    (144, 3.8, 0, 0, 12880, 24, 47),
                    (145, 4.2, 11.1, 186, 0, 25, 1),
                    (146, 5.1, 8.9, 204, 10300, 25, 3),
                    (147, 4.7, 7.9, 215, 18200, 25, 5),
                    (148, 3.4, 11.4, 182, 8100, 25, 58),
                    (149, 3.5, 9.5, 200, 15000, 25, 61),
                    (150, 0, 0, 0, 0, 26, 94),
                    (151, 0, 0, 0, 105000, 26, 95),
                    (152, 5.3, 10.2, 211, 0, 27, 3),
                    (153, 6, 7.7, 242, 14600, 27, 9),
                    (154, 4.2, 8.9, 224, 16800, 27, 67),
                    (155, 4.3, 7.9, 241, 26400, 27, 72),
                    (156, 4.9, 9.9, 198, 0, 28, 2),
                    (157, 5.1, 9.2, 206, 5000, 28, 3),
                    (158, 4.7, 8.1, 220, 8800, 28, 6),
                    (159, 5.8, 7.1, 235, 16600, 28, 9),
                    (160, 3.8, 10.5, 200, 9800, 28, 60),
                    (161, 4.1, 8.5, 218, 18800, 28, 67),
                    (162, 4.1, 7.3, 234, 18500, 28, 72),
                    (163, 5.1, 9.4, 212, 0, 29, 3),
                    (164, 4.7, 8.2, 224, 5100, 29, 6),
                    (165, 5.8, 7.2, 242, 15700, 29, 9),
                    (166, 3.8, 10.7, 203, 9100, 29, 60),
                    (167, 4, 8.6, 224, 18000, 29, 67),
                    (168, 4.2, 7.4, 241, 28500, 29, 72),
                    (169, 0, 0, 0, 0, 30, 96),
                    (170, 7, 5.2, 250, 0, 31, 97),
                    (171, 7.1, 5.4, 250, 0, 32, 97),
                    (172, 7, 5.3, 250, 0, 33, 97),
                    (173, 7, 5, 250, 0, 34, 97),
                    (174, 4.9, 10.1, 198, 0, 35, 2),
                    (175, 5.1, 9.4, 206, 4900, 35, 3),
                    (176, 4.7, 8.2, 220, 8800, 35, 6),
                    (177, 5.8, 7.2, 235, 19600, 35, 9),
                    (180, 4.1, 8.6, 218, 21800, 35, 67),
                    (178, 3.8, 10.7, 200, 12800, 35, 60),
                    (179, 3.3, 10.7, 200, 15200, 35, 59),
                    (181, 4.2, 7.4, 234, 131400, 35, 72),
                    (182, 1.5, 7.6, 222, 0, 36, 98),
                    (183, 0, 0, 0, 0, 37, 4),
                    (184, 0, 0, 0, 18400, 37, 13),
                    (185, 5.9, 6.3, 250, 41300, 37, 16),
                    (186, 0, 0, 0, 20700, 37, 62),
                    (187, 4.2, 8.9, 221, 18400, 37, 65),
                    (188, 0, 0, 0, 32000, 37, 73),
                    (189, 0, 0, 0, 0, 38, 4),
                    (190, 0, 0, 0, 9700, 38, 13),
                    (191, 0, 0, 0, 41600, 38, 16),
                    (192, 0, 0, 0, 12000, 38, 62),
                    (193, 4.3, 9.2, 215, 9700, 38, 65),
                    (194, 0, 0, 0, 23300, 38, 73),
                    (195, 6.2, 8.7, 222, 0, 39, 8),
                    (196, 6.3, 7.4, 245, 19400, 39, 15),
                    (197, 8.5, 6.3, 250, 100200, 39, 17),
                    (198, 4.7, 10.2, 210, 10000, 39, 65),
                    (199, 4.7, 10.2, 210, 10000, 39, 67),
                    (200, 4.9, 8.8, 222, 17900, 39, 69),
                    (201, 4.8, 8.2, 234, 21800, 39, 75),
                    (202, 0, 0, 0, 75200, 39, 76),
                    (203, 5.9, 6.3, 250, 94700, 39, 79),
                    (204, 5.9, 6.3, 250, 99300, 39, 80),
                    (205, 5.7, 7.9, 230, 0, 40, 8),
                    (206, 5.9, 6.8, 250, 19400, 40, 15),
                    (207, 8.1, 5.8, 250, 100300, 40, 17),
                    (208, 4.2, 8.3, 225, 18000, 40, 68),
                    (209, 4.6, 8.2, 230, 18000, 40, 69),
                    (210, 4.5, 7.7, 240, 21800, 40, 75),
                    (211, 5.1, 7.6, 244, 63400, 40, 76),
                    (212, 5.8, 5.9, 250, 82200, 40, 79),
                    (213, 5.7, 5.9, 250, 98600, 40, 80),
                    (214, 10.7, 4.9, 250, 0, 41, 99),
                    (215, 10.5, 4.5, 250, 0, 42, 99),
                    (216, 8.5, 5.4, 250, 0, 43, 19),
                    (217, 8.1, 4.9, 250, 0, 44, 19),
                    (219, 5.8, 9.3, 220, 0, 46, 7),
                    (220, 5.8, 8.2, 220, 9500, 46, 8),
                    (221, 5.9, 7, 250, 29000, 46, 15),
                    (222, 8.1, 6, 250000, 109900, 46, 17),
                    (223, 4.4, 9.5, 212, 11900, 46, 63),
                    (224, 4.2, 9.5, 212, 17400, 46, 64),
                    (225, 4.5, 9.4, 212, 19300, 46, 67),
                    (226, 4.5, 9.4, 212, 19300, 46, 65),
                    (227, 4.3, 8.6, 221, 27600, 46, 68),
                    (228, 4.6, 7.8, 238, 31600, 46, 75),
                    (229, 5.1, 7.8, 240, 73000, 46, 76),
                    (230, 5.8, 6.2, 250, 91800, 46, 79),
                    (231, 5.9, 7.9, 233, 2200, 47, 10),
                    (232, 5.7, 7.9, 233, 12500, 47, 11),
                    (233, 5.9, 6.7, 250, 25200, 47, 16),
                    (234, 7.4, 5.1, 250, 80700, 47, 19),
                    (235, 4.3, 9.5, 214, 0, 47, 66),
                    (236, 4.4, 8.4, 232, 6000, 47, 74),
                    (237, 5.1, 6.6, 244, 65900, 47, 78),
                    (238, 5.1, 5.5, 250, 82000, 47, 83),
                    (239, 6, 5, 250, 102700, 47, 84),
                    (240, 6.2, 4.9, 250, 134200, 47, 85),
                    (241, 8, 5.8, 250, 15500, 48, 19),
                    (242, 5.6, 7.3, 227, 0, 48, 78),
                    (243, 6.5, 5.5, 250, 31800, 48, 84),
                    (244, 6.2, 8.2, 226, 2200, 49, 10),
                    (245, 6, 6.9, 250, 25200, 49, 16),
                    (246, 7.6, 5.3, 250, 82400, 49, 19),
                    (247, 4.5, 9.8, 209, 0, 49, 66),
                    (248, 4.6, 8.7, 226, 5900, 49, 74),
                    (249, 6.4, 5.1, 250, 135900, 49, 85),
                    (250, 9.6, 3.9, 250, 0, 50, 100),
                    (251, 0, 0, 0, 0, 51, 101),
                    (252, 0, 0, 0, 0, 52, 101),
                    (253, 6, 6.9, 250, 0, 53, 16),
                    (254, 4.7, 7.3, 239, 51900, 53, 77),
                    (255, 6.1, 5.2, 250, 98000, 53, 84),
                    (256, 9.5, 3.9, 250, 0, 54, 100),
                    (257, 0, 0, 0, 0, 55, 101),
                    (258, 7.9, 5.9, 250, 31300, 56, 18),
                    (259, 9.2, 4.6, 250, 98700, 56, 20),
                    (260, 6, 6.1, 250, 0, 56, 81),
                    (261, 7.5, 4.9, 250, 76200, 56, 102),
                    (262, 9.6, 4.1, 250, 0, 57, 103),
                    (263, 7.8, 5.7, 250, 30200, 58, 18),
                    (264, 5.9, 5.9, 250, 0, 58, 81),
                    (265, 11.3, 4.6, 250, 0, 59, 104),
                    (266, 5.8, 9.2, 203, 0, 60, 4),
                    (267, 5.5, 9.2, 204, 1500, 60, 5),
                    (268, 6.6, 7.6, 217, 29600, 60, 12),
                    (269, 6.6, 6.4, 233, 49500, 60, 14),
                    (270, 4.6, 10.9, 190, 7500, 60, 62),
                    (271, 4.4, 9.6, 204, 12600, 60, 65),
                    (272, 5.2, 7.9, 219, 29100, 60, 70),
                    (273, 0, 0, 0, 0, 61, 105),
                    (274, 7.5, 8.5, 210, 15100, 62, 12),
                    (275, 0, 0, 0, 37400, 62, 15),
                    (276, 5.3, 10.9, 192, 0, 62, 65),
                    (277, 0, 0, 0, 0, 62, 67),
                    (278, 6.2, 9.9, 204, 20700, 62, 69),
                    (279, 5.4, 8.7, 210, 24800, 62, 75),
                    (280, 6.3, 6.2, 230, 87500, 62, 81),
                    (281, 6.8, 5.1, 250, 0, 63, 106),
                    (282, 0, 0, 0, 11800, 63, 85),
                    (283, 0, 0, 0, 2800, 64, 19),
                    (284, 0, 0, 0, 0, 64, 82),
                    (285, 6, 6, 250, 0, 65, 21),
                    (286, 4.4, 7.1, 241, 800, 65, 71),
                    (287, 7.1, 4.9, 250, 0, 66, 107),
                    (288, 6, 6.2, 250, 0, 67, 21),
                    (289, 4.3, 7.3, 237, 800, 67, 71),
                    (218, 0, 0, 0, 0, 68, 107);
                    """)

def wyszukiwanie():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_wyszukiwanie` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `Marka` varchar(30) DEFAULT NULL,
                    `Model` varchar(30) DEFAULT NULL,
                    `Rocznik_od` int(11) DEFAULT NULL,
                    `Rocznik_do` int(11) DEFAULT NULL,
                    `Cena_od` int(11) DEFAULT NULL,
                    `Cena_do` int(11) DEFAULT NULL,
                    PRIMARY KEY (id))
                    ENGINE=MyISAM DEFAULT CHARSET=latin1;
                    """)

def zdjecia():
    cur.execute("""CREATE TABLE IF NOT EXISTS `wyszukiwarka_zdjecia` (
                `id` int(11) NOT NULL,
                `plik` longBlob NOT NULL,
                `idNadwozie` int(11) NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (idNadwozie) REFERENCES wyszukiwarka_nadwozia(id))
                ENGINE=MyISAM  DEFAULT CHARSET=latin1;""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (69, 14, x'""" + readFile('photos/ka1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (70, 14, x'""" + readFile('photos/ka2.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (71, 14, x'""" + readFile('photos/ka3.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (72, 4, x'""" + readFile('photos/fiesta3d1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (73, 4, x'""" + readFile('photos/fiesta3d2.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (74, 4, x'""" + readFile('photos/fiesta3d3.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (75, 4, x'""" + readFile('photos/fiesta3d4.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (76, 5, x'""" + readFile('photos/fiesta5d1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (77, 5, x'""" + readFile('photos/fiesta5d2.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (78, 5, x'""" + readFile('photos/fiesta5d3.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (79, 5, x'""" + readFile('photos/fiesta5d4.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (80, 6, x'""" + readFile('photos/fiestast1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (81, 6, x'""" + readFile('photos/fiestast2.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (82, 6, x'""" + readFile('photos/fiestast3.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (83, 6, x'""" + readFile('photos/fiestast4.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (84, 7, x'""" + readFile('photos/fiestavan1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (1,1, x'""" + readFile('photos/1.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (2,2, x'""" + readFile('photos/2.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (3,3, x'""" + readFile('photos/3.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (4,4, x'""" + readFile('photos/4.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (5,5, x'""" + readFile('photos/5.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (6,6, x'""" + readFile('photos/6.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (7,7, x'""" + readFile('photos/7.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (8,8, x'""" + readFile('photos/8.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (9,9, x'""" + readFile('photos/9.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (10,10, x'""" + readFile('photos/10.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (11,11, x'""" + readFile('photos/11.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (12,12, x'""" + readFile('photos/12.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (13,13, x'""" + readFile('photos/13.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (14,14, x'""" + readFile('photos/14.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (15,15, x'""" + readFile('photos/15.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (16,16, x'""" + readFile('photos/16.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (17,17, x'""" + readFile('photos/17.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (18,18, x'""" + readFile('photos/18.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (19,19, x'""" + readFile('photos/19.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (20,20, x'""" + readFile('photos/20.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (21,21, x'""" + readFile('photos/21.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (22,22, x'""" + readFile('photos/22.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (23,23, x'""" + readFile('photos/23.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (24,24, x'""" + readFile('photos/24.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (25,25, x'""" + readFile('photos/25.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (26,26, x'""" + readFile('photos/26.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (27,27, x'""" + readFile('photos/27.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (28,28, x'""" + readFile('photos/28.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (29,29, x'""" + readFile('photos/29.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (30,30, x'""" + readFile('photos/30.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (31,31, x'""" + readFile('photos/31.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (32,32, x'""" + readFile('photos/32.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (33,33, x'""" + readFile('photos/33.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (34,34, x'""" + readFile('photos/34.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (35,35, x'""" + readFile('photos/35.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (36,36, x'""" + readFile('photos/36.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (37,37, x'""" + readFile('photos/37.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (38,38, x'""" + readFile('photos/38.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (39,39, x'""" + readFile('photos/39.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (40,40, x'""" + readFile('photos/40.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (41,41, x'""" + readFile('photos/41.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (42,42, x'""" + readFile('photos/42.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (43,43, x'""" + readFile('photos/43.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (44,44, x'""" + readFile('photos/44.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (45,45, x'""" + readFile('photos/45.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (46,46, x'""" + readFile('photos/46.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (47,47, x'""" + readFile('photos/47.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (48,48, x'""" + readFile('photos/48.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (49,49, x'""" + readFile('photos/49.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (50,50, x'""" + readFile('photos/50.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (51,51, x'""" + readFile('photos/51.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (52,52, x'""" + readFile('photos/52.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (53,53, x'""" + readFile('photos/53.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (54,54, x'""" + readFile('photos/54.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (55,55, x'""" + readFile('photos/55.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (56,56, x'""" + readFile('photos/56.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (57,57, x'""" + readFile('photos/57.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (58,58, x'""" + readFile('photos/58.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (59,59, x'""" + readFile('photos/59.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (60,60, x'""" + readFile('photos/60.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (61,61, x'""" + readFile('photos/61.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (62,62, x'""" + readFile('photos/62.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (63,63, x'""" + readFile('photos/63.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (64,64, x'""" + readFile('photos/64.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (65,65, x'""" + readFile('photos/65.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (66,66, x'""" + readFile('photos/66.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (67,67, x'""" + readFile('photos/67.jpg') + """');""")
    cur.execute("""INSERT INTO `wyszukiwarka_zdjecia` (`id`, `idNadwozie`, `Plik`) VALUES
                    (68,68, x'""" + readFile('photos/68.jpg') + """');""")

def views():
    cur.execute("""CREATE OR REPLACE VIEW wyszukiwarka_porownania AS
                    SELECT concat(s.id, ' ', n.id, ' ', e.id) as id,
                    s.idMarka AS idMarka,
                    s.Model AS Model,
                    s.Rocznik AS Rocznik,
                    n.Rodzaj AS Nadwozie,
                    concat(e.Pojemnosc, ' ', e.Rodzaj, ' ', e.KM) AS Silnik,
                    e.Paliwo AS Paliwo,
                    en.Spalanie AS Spalanie,
                    en.Przyspieszenie AS Przyspieszenie,
                    en.VMax AS VMax,
                    (en.Oplata+n.Oplata+s.Cena) AS Cena
                    FROM
                    wyszukiwarka_silniki_nadwozia en join wyszukiwarka_silniki e on e.id=en.idSilnik join wyszukiwarka_nadwozia n on en.idNadwozie=n.id join wyszukiwarka_samochody s on s.id=n.idSamochod
                    """)

def dodatki():
    cur.execute("""CREATE
                    PROCEDURE `samochodMaxPrice`(IN `s_id` INT) NOT DETERMINISTIC NO SQL SQL SECURITY DEFINER
                    SELECT en.id, MAX(n.Oplata + en.Oplata) AS Cena
                    FROM wyszukiwarka_silniki_nadwozia en
                    JOIN wyszukiwarka_nadwozia n ON en.idNadwozie = n.id
                    WHERE n.idSamochod = s_id
                    """)
    cur.execute("""CREATE
                    PROCEDURE `nadwozieMaxPrice`(IN `s_id` INT) NOT DETERMINISTIC NO SQL SQL SECURITY DEFINER
                    SELECT n.id as id, max(en.Oplata) as Cena
                    FROM wyszukiwarka_silniki_nadwozia en
                    JOIN wyszukiwarka_nadwozia n ON en.idNadwozie = n.id
                    WHERE n.idSamochod = s_id
                    GROUP BY n.id
                    """)
    cur.execute("""CREATE
                    PROCEDURE `defaultVersion`(IN `s_id` INT) NOT DETERMINISTIC NO SQL SQL SECURITY DEFINER
                    SELECT * FROM wyszukiwarka_porownania
                    WHERE id =(
                        SELECT CONCAT ( n.idSamochod, ' ', n.id, ' ', en.idSilnik ) FROM wyszukiwarka_silniki_nadwozia en
                        JOIN wyszukiwarka_nadwozia n ON en.idNadwozie = n.id
                        WHERE n.idSamochod = s_id AND(n.Oplata + en.Oplata) = 0
                    )
                    """)


def readFile(path):
    with open(path, 'rb') as f:
        result = f.read()
    return "".join("{:02x}".format(ord(c)) for c in result)

try:
    con = mdb.connect('127.0.0.1', 'root', '', 'wyszukiwarka');

    with con:

        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        ver = cur.fetchone()
        print "Database version : %s " % ver

        marki()
        samochody()
        nadwozia()
        silniki()
        silnikiNadwozia()
        wyszukiwanie()
        zdjecia()
        dodatki()
        views()

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()