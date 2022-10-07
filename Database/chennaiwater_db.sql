-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2022 at 09:22 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chennaiwater_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `table_chembarambakkam_monthlylakelevel`
--

CREATE TABLE `table_chembarambakkam_monthlylakelevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(20) NOT NULL,
  `February` bigint(20) NOT NULL,
  `March` bigint(20) NOT NULL,
  `April` bigint(20) NOT NULL,
  `May` bigint(20) NOT NULL,
  `June` bigint(20) NOT NULL,
  `July` bigint(20) NOT NULL,
  `August` bigint(20) NOT NULL,
  `September` bigint(20) NOT NULL,
  `October` bigint(20) NOT NULL,
  `November` bigint(20) NOT NULL,
  `December` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_chembarambakkam_monthlylakelevel`
--

INSERT INTO `table_chembarambakkam_monthlylakelevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(2003, 792, 650, 459, 224, 56, 0, 25, 2, 31, 33, 39, 8),
(2004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 494),
(2005, 401, 275, 211, 129, 131, 68, 30, 6, 0, 9, 1259, 2908),
(2006, 2986, 2843, 2637, 2419, 2168, 1938, 1719, 1486, 1349, 1293, 2113, 2512),
(2007, 2351, 2157, 1859, 1609, 1312, 1091, 1060, 942, 1162, 1634, 2728, 2671),
(2008, 3120, 2960, 2793, 2434, 2099, 2034, 1971, 1734, 1484, 1249, 1852, 3158),
(2009, 2979, 2679, 2742, 2929, 2560, 2064, 1478, 999, 725, 486, 534, 1552),
(2010, 2496, 2254, 1956, 2166, 2379, 2106, 1881, 1646, 1727, 1572, 1527, 2202),
(2011, 3130, 3080, 2725, 2210, 1704, 1822, 1983, 2438, 2845, 2792, 2735, 2673),
(2012, 2825, 2719, 2390, 1989, 1574, 1177, 759, 1123, 1404, 1199, 1193, 1141),
(2013, 1239, 980, 1446, 1775, 1422, 1012, 757, 555, 445, 668, 749, 956),
(2014, 874, 719, 790, 747, 916, 1264, 1105, 850, 633, 718, 1211, 1189),
(2015, 968, 747, 728, 864, 799, 572, 511, 323, 165, 148, 228, 3141),
(2016, 3153, 3018, 2855, 2378, 2307, 2310, 1977, 1561, 1145, 972, 569, 240),
(2017, 537, 339, 162, 463, 287, 93, 49, 83, 180, 221, 617, 1759),
(2018, 1842, 1693, 1507, 1215, 1198, 1214, 906, 628, 445, 338, 235, 185),
(2019, 102, 50, 22, 10, 2, 1, 0, 0, 0, 12, 75, 749),
(2020, 1694, 1547, 1984, 2078, 1930, 2011, 2019, 1849, 1671, 1585, 2297, 3123),
(2021, 3347, 3470, 3177, 3030, 2965, 2952, 2641, 2475, 0, 2879, 0, 3187);

-- --------------------------------------------------------

--
-- Table structure for table `table_cholavaram_monthlylakelevel`
--

CREATE TABLE `table_cholavaram_monthlylakelevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(20) NOT NULL,
  `February` bigint(20) NOT NULL,
  `March` bigint(20) NOT NULL,
  `April` bigint(20) NOT NULL,
  `May` bigint(20) NOT NULL,
  `June` bigint(20) NOT NULL,
  `July` bigint(20) NOT NULL,
  `August` bigint(20) NOT NULL,
  `September` bigint(20) NOT NULL,
  `October` bigint(20) NOT NULL,
  `November` bigint(20) NOT NULL,
  `December` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_cholavaram_monthlylakelevel`
--

INSERT INTO `table_cholavaram_monthlylakelevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(2003, 542, 139, 53, 46, 7, 0, 0, 0, 0, 0, 0, 0),
(2004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 158),
(2005, 71, 57, 36, 0, 0, 0, 0, 0, 0, 0, 569, 797),
(2006, 763, 721, 665, 585, 521, 439, 387, 325, 208, 229, 540, 708),
(2007, 473, 545, 524, 294, 49, 39, 37, 56, 68, 130, 431, 660),
(2008, 881, 867, 785, 756, 676, 583, 514, 289, 184, 97, 325, 881),
(2009, 872, 778, 705, 625, 539, 172, 83, 104, 167, 188, 208, 607),
(2010, 715, 686, 651, 214, 84, 98, 100, 155, 270, 405, 431, 698),
(2011, 816, 840, 770, 678, 624, 218, 90, 92, 123, 140, 684, 836),
(2012, 855, 495, 300, 102, 86, 83, 85, 85, 85, 93, 218, 329),
(2013, 471, 398, 89, 75, 41, 0, 0, 0, 0, 0, 142, 170),
(2014, 170, 94, 79, 0, 7, 3, 0, 0, 0, 0, 46, 61),
(2015, 123, 113, 75, 64, 19, 0, 0, 0, 0, 0, 0, 595),
(2016, 717, 533, 376, 252, 120, 83, 80, 73, 69, 100, 72, 72),
(2017, 82, 69, 28, 0, 0, 0, 0, 0, 22, 36, 180, 595),
(2018, 513, 451, 398, 100, 70, 68, 61, 26, 1, 8, 20, 40),
(2019, 48, 48, 48, 42, 11, 1, 0, 0, 0, 54, 194, 96),
(2020, 68, 72, 72, 72, 72, 72, 72, 77, 94, 112, 138, 504),
(2021, 874, 881, 855, 770, 704, 626, 593, 622, 640, 646, 834, 817);

-- --------------------------------------------------------

--
-- Table structure for table `table_monthlyrainfalllevel`
--

CREATE TABLE `table_monthlyrainfalllevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(20) NOT NULL,
  `February` bigint(20) NOT NULL,
  `March` bigint(20) NOT NULL,
  `April` bigint(20) NOT NULL,
  `May` bigint(20) NOT NULL,
  `June` bigint(20) NOT NULL,
  `July` bigint(20) NOT NULL,
  `August` bigint(20) NOT NULL,
  `September` bigint(20) NOT NULL,
  `October` bigint(20) NOT NULL,
  `November` bigint(20) NOT NULL,
  `December` bigint(20) NOT NULL,
  `TOTAL` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_monthlyrainfalllevel`
--

INSERT INTO `table_monthlyrainfalllevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `TOTAL`) VALUES
(2003, 0, 0, 5, 5, 6, 26, 141, 139, 103, 231, 98, 56, 810),
(2004, 30, 0, 0, 7, 229, 50, 51, 37, 191, 275, 297, 5, 1171),
(2005, 0, 0, 9, 101, 32, 52, 84, 119, 207, 590, 514, 501, 2208),
(2006, 0, 0, 28, 31, 22, 139, 55, 113, 172, 420, 224, 36, 1240),
(2007, 0, 6, 0, 12, 19, 68, 245, 271, 175, 265, 118, 270, 1449),
(2008, 85, 6, 189, 0, 28, 128, 89, 136, 121, 327, 530, 16, 1655),
(2009, 8, 0, 1, 0, 27, 33, 48, 146, 139, 86, 450, 181, 1120),
(2010, 2, 0, 0, 0, 160, 106, 269, 296, 160, 147, 180, 242, 1561),
(2011, 2, 58, 0, 35, 24, 60, 85, 249, 147, 167, 394, 96, 1316),
(2012, 10, 0, 0, 4, 11, 32, 120, 61, 146, 320, 104, 174, 982),
(2013, 0, 44, 23, 4, 1, 72, 146, 171, 242, 216, 120, 28, 1065),
(2014, 0, 0, 0, 0, 18, 85, 101, 122, 136, 245, 192, 127, 1026),
(2015, 1, 0, 1, 54, 25, 57, 163, 173, 88, 178, 996, 419, 2155),
(2016, 0, 0, 0, 0, 187, 134, 36, 14, 249, 7, 35, 211, 874),
(2017, 4, 0, 0, 0, 32, 81, 85, 267, 109, 330, 418, 62, 1388),
(2018, 0, 1, 5, 0, 1, 35, 63, 166, 134, 135, 249, 91, 880),
(2019, 0, 1, 0, 3, 9, 17, 107, 178, 327, 368, 85, 191, 1285),
(2020, 49, 0, 0, 25, 3, 39, 105, 127, 199, 227, 379, 225, 1379),
(2021, 90, 4, 0, 12, 29, 43, 251, 260, 68, 76, 0, 0, 832);

-- --------------------------------------------------------

--
-- Table structure for table `table_poondi_monthlylakelevel`
--

CREATE TABLE `table_poondi_monthlylakelevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(20) NOT NULL,
  `February` bigint(20) NOT NULL,
  `March` bigint(20) NOT NULL,
  `April` bigint(20) NOT NULL,
  `May` bigint(20) NOT NULL,
  `June` bigint(20) NOT NULL,
  `July` bigint(20) NOT NULL,
  `August` bigint(20) NOT NULL,
  `September` bigint(20) NOT NULL,
  `October` bigint(20) NOT NULL,
  `November` bigint(20) NOT NULL,
  `December` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_poondi_monthlylakelevel`
--

INSERT INTO `table_poondi_monthlylakelevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(2003, 781, 278, 192, 22, 14, 7, 3, 5, 7, 5, 57, 14),
(2004, 4, 5, 4, 8, 4, 5, 5, 4, 1, 14, 50, 324),
(2005, 805, 851, 495, 215, 236, 180, 126, 89, 79, 18, 1582, 2826),
(2006, 3231, 3035, 2669, 1958, 1744, 1394, 793, 531, 632, 1725, 2265, 2354),
(2007, 2928, 2565, 2246, 2036, 1867, 1270, 305, 200, 1071, 2265, 2429, 2568),
(2008, 3101, 3061, 2801, 2487, 2257, 945, 736, 639, 540, 989, 2100, 3018),
(2009, 3058, 3025, 2798, 2886, 2287, 2000, 1567, 695, 180, 605, 1175, 2255),
(2010, 2293, 1493, 1758, 2054, 1356, 1195, 1050, 1098, 1264, 1306, 1795, 2823),
(2011, 3231, 3108, 2733, 2530, 2381, 1700, 1180, 1798, 2312, 3054, 2666, 2484),
(2012, 2839, 3048, 2858, 2577, 2348, 2080, 1705, 940, 614, 593, 695, 796),
(2013, 1520, 1359, 986, 411, 404, 337, 219, 198, 307, 329, 457, 747),
(2014, 147, 254, 526, 93, 294, 429, 105, 81, 574, 410, 286, 280),
(2015, 487, 235, 235, 77, 155, 98, 80, 52, 59, 59, 70, 2745),
(2016, 3114, 2627, 2049, 1911, 1239, 1065, 1018, 643, 569, 285, 229, 194),
(2017, 617, 724, 799, 160, 58, 39, 19, 20, 27, 42, 332, 1004),
(2018, 1012, 1387, 2011, 1611, 396, 184, 132, 50, 13, 93, 695, 381),
(2019, 298, 190, 477, 333, 193, 56, 18, 16, 16, 597, 1682, 989),
(2020, 1426, 1584, 1548, 1438, 849, 377, 222, 85, 95, 712, 1540, 2902),
(2021, 3135, 3231, 2941, 2018, 1160, 427, 404, 1869, 2550, 2507, 2807, 2841);

-- --------------------------------------------------------

--
-- Table structure for table `table_redhills_monthlylakelevel`
--

CREATE TABLE `table_redhills_monthlylakelevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(20) NOT NULL,
  `February` bigint(20) NOT NULL,
  `March` bigint(20) NOT NULL,
  `April` bigint(20) NOT NULL,
  `May` bigint(20) NOT NULL,
  `June` bigint(20) NOT NULL,
  `July` bigint(20) NOT NULL,
  `August` bigint(20) NOT NULL,
  `September` bigint(20) NOT NULL,
  `October` bigint(20) NOT NULL,
  `November` bigint(20) NOT NULL,
  `December` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_redhills_monthlylakelevel`
--

INSERT INTO `table_redhills_monthlylakelevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(2003, 1585, 1992, 1919, 1730, 1447, 1176, 897, 716, 535, 371, 266, 274),
(2004, 268, 220, 153, 190, 151, 130, 109, 49, 0, 0, 175, 793),
(2005, 986, 1458, 1887, 1873, 1640, 1361, 1091, 823, 545, 397, 1570, 3052),
(2006, 3116, 2624, 2232, 2545, 2141, 1770, 1881, 1596, 1514, 1134, 2216, 2426),
(2007, 2507, 3106, 2856, 2467, 2156, 2016, 2254, 2085, 1987, 1921, 2415, 2440),
(2008, 3187, 3022, 2732, 2910, 2489, 2854, 2421, 2143, 1873, 1529, 1685, 3022),
(2009, 2886, 2528, 2335, 2432, 2248, 2071, 1786, 1871, 1803, 1378, 1074, 1652),
(2010, 2013, 2342, 2579, 2769, 2344, 2004, 1600, 1381, 1428, 1297, 1581, 2695),
(2011, 3235, 3254, 3106, 2705, 2263, 2207, 1883, 1732, 2018, 2956, 3062, 3006),
(2012, 2632, 2771, 2572, 2290, 1820, 1319, 1201, 1378, 1375, 1538, 1886, 1970),
(2013, 2164, 2212, 2189, 1725, 1257, 821, 476, 338, 575, 976, 1332, 1850),
(2014, 2166, 1994, 2237, 0, 1746, 1507, 1281, 927, 901, 1044, 974, 1339),
(2015, 1580, 1743, 1833, 1501, 1359, 1007, 690, 428, 242, 84, 25, 2790),
(2016, 2864, 2827, 2711, 2346, 1881, 1611, 1202, 1082, 674, 658, 413, 268),
(2017, 450, 305, 720, 646, 418, 166, 21, 0, 83, 135, 614, 1557),
(2018, 1585, 1368, 1194, 1660, 1779, 1427, 1120, 920, 713, 478, 809, 1102),
(2019, 941, 720, 520, 301, 125, 3, 0, 0, 0, 50, 838, 1639),
(2020, 2456, 2906, 2583, 2796, 2956, 2782, 2745, 2510, 2320, 2162, 2167, 2841),
(2021, 3125, 3243, 3128, 3032, 2990, 2784, 2623, 2593, 2847, 2964, 2724, 2908);

-- --------------------------------------------------------

--
-- Table structure for table `table_sum`
--

CREATE TABLE `table_sum` (
  `Year` int(11) NOT NULL,
  `TOTAL` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_sum`
--

INSERT INTO `table_sum` (`Year`, `TOTAL`) VALUES
(2003, 1831),
(2004, 4140),
(2005, 12232),
(2006, 9731),
(2007, 10344),
(2008, 12712),
(2009, 7949),
(2010, 10957),
(2011, 11002),
(2012, 5643),
(2013, 5791),
(2014, 4733),
(2015, 11999),
(2016, 2204),
(2017, 7023),
(2018, 3725),
(2019, 6102),
(2020, 11727),
(2021, 11542);

-- --------------------------------------------------------

--
-- Table structure for table `table_veeranam_monthlylakelevel`
--

CREATE TABLE `table_veeranam_monthlylakelevel` (
  `Year` int(11) NOT NULL,
  `January` bigint(11) NOT NULL,
  `February` bigint(11) NOT NULL,
  `March` bigint(11) NOT NULL,
  `April` bigint(11) NOT NULL,
  `May` bigint(11) NOT NULL,
  `June` bigint(11) NOT NULL,
  `July` bigint(11) NOT NULL,
  `August` bigint(11) NOT NULL,
  `September` bigint(11) NOT NULL,
  `October` bigint(11) NOT NULL,
  `November` bigint(11) NOT NULL,
  `December` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_veeranam_monthlylakelevel`
--

INSERT INTO `table_veeranam_monthlylakelevel` (`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) VALUES
(2003, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 725),
(2004, 75, 0, 0, 0, 0, 295, 90, 33, 0, 965, 1275, 1200),
(2005, 670, 1465, 935, 523, 1271, 892, 458, 132, 1173, 914, 720, 441),
(2006, 671, 1465, 1441, 1051, 646, 327, 212, 605, 828, 704, 507, 491),
(2007, 742, 1465, 1465, 1076, 774, 425, 94, 687, 671, 605, 507, 556),
(2008, 1344, 1465, 1356, 1271, 924, 425, 318, 679, 1222, 327, 605, 978),
(2009, 589, 1416, 1112, 623, 327, 52, 0, 0, 474, 376, 573, 763),
(2010, 1076, 1465, 1258, 742, 376, 1124, 671, 294, 704, 671, 704, 978),
(2011, 978, 458, 77, 0, 0, 0, 0, 507, 704, 687, 687, 687),
(2012, 914, 1416, 1368, 720, 384, 499, 111, 96, 0, 0, 871, 425),
(2013, 499, 127, 26, 237, 56, 0, 0, 0, 1161, 474, 704, 1003),
(2014, 763, 1296, 1065, 726, 1003, 1051, 782, 467, 614, 935, 1027, 838),
(2015, 1197, 1380, 1258, 838, 791, 1283, 967, 655, 967, 924, 978, 573),
(2016, 488, 458, 0, 0, 0, 0, 0, 0, 0, 0, 0, 556),
(2017, 253, 69, 0, 0, 0, 0, 0, 0, 0, 0, 425, 720),
(2018, 806, 409, 111, 0, 0, 0, 0, 0, 1344, 806, 564, 1137),
(2019, 1453, 1339, 1012, 589, 1197, 757, 359, 96, 1251, 1271, 1180, 1344),
(2020, 1171, 1453, 1387, 1, 597, 269, 228, 1465, 1105, 687, 600, 978),
(2021, 993, 584, 187, 19, 0, 0, 0, 129, 1441, 935, 785, 957);

-- --------------------------------------------------------

--
-- Table structure for table `table_yearlylakelevels`
--

CREATE TABLE `table_yearlylakelevels` (
  `Year` int(11) NOT NULL,
  `Poondi` bigint(20) NOT NULL,
  `Cholavaram` bigint(20) NOT NULL,
  `Red Hills` bigint(20) NOT NULL,
  `Chembarambakkam` bigint(20) NOT NULL,
  `Veeranam` bigint(20) NOT NULL,
  `TOTAL` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `table_yearlylakelevels`
--

INSERT INTO `table_yearlylakelevels` (`Year`, `Poondi`, `Cholavaram`, `Red Hills`, `Chembarambakkam`, `Veeranam`, `TOTAL`) VALUES
(2003, 14, 0, 274, 8, 725, 1021),
(2004, 324, 158, 793, 494, 1200, 2969),
(2005, 2826, 797, 3052, 2908, 441, 10024),
(2006, 2354, 708, 2426, 2512, 491, 8491),
(2007, 2568, 660, 2440, 2671, 556, 8895),
(2008, 3018, 881, 3022, 3158, 978, 11057),
(2009, 2255, 607, 1652, 1552, 763, 6829),
(2010, 2823, 698, 2695, 2202, 978, 9396),
(2011, 2484, 836, 3006, 2673, 687, 9686),
(2012, 796, 329, 1970, 1141, 425, 4661),
(2013, 747, 170, 1850, 956, 1003, 4726),
(2014, 280, 61, 1339, 1189, 838, 3707),
(2015, 2745, 595, 2790, 3141, 573, 9844),
(2016, 194, 72, 268, 240, 556, 1330),
(2017, 1004, 595, 1557, 1759, 720, 5635),
(2018, 381, 40, 1102, 185, 1137, 2845),
(2019, 989, 96, 1639, 749, 1344, 4817),
(2020, 2902, 504, 2841, 3123, 978, 10348),
(2021, 2841, 817, 2908, 3187, 957, 10710);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `table_chembarambakkam_monthlylakelevel`
--
ALTER TABLE `table_chembarambakkam_monthlylakelevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_cholavaram_monthlylakelevel`
--
ALTER TABLE `table_cholavaram_monthlylakelevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_monthlyrainfalllevel`
--
ALTER TABLE `table_monthlyrainfalllevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_poondi_monthlylakelevel`
--
ALTER TABLE `table_poondi_monthlylakelevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_redhills_monthlylakelevel`
--
ALTER TABLE `table_redhills_monthlylakelevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_sum`
--
ALTER TABLE `table_sum`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_veeranam_monthlylakelevel`
--
ALTER TABLE `table_veeranam_monthlylakelevel`
  ADD PRIMARY KEY (`Year`);

--
-- Indexes for table `table_yearlylakelevels`
--
ALTER TABLE `table_yearlylakelevels`
  ADD PRIMARY KEY (`Year`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
