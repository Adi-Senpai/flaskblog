-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2021 at 04:57 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(50) NOT NULL,
  `mes` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phno`, `mes`, `date`) VALUES
(1, 'abc', 'abc@xyz', '112344311', 'bbdqdbqd npkdqnpnd', '2021-07-29 20:44:57'),
(2, 'abc', 'abc@xyz', '123344', 'asdede dqwdq', '2021-07-29 15:52:16'),
(3, 'wwww', 'qqqw@qsq', '112113131', 'scacasca', '2021-07-29 15:52:56'),
(4, 'wwww', 'qqqw@qsq', '112113131', 'scacasca', '2021-07-29 15:58:32'),
(5, 'abc', 'abc@xyz', '123344', 'asdede dqwdq', '2021-07-29 15:58:47'),
(6, 'qqwewerwq', 'dwdqwd@ayx', '1233521', 'sdsdadada', '2021-07-30 13:37:49'),
(7, 'fffffffffff', 'ddddddddd@eweq', '1123421211', 'cddqdqdqq', '2021-07-30 14:11:52'),
(8, 'fffffffffff', 'ddddddddd@eweq', '1123421211', 'cddqdqdqq', '2021-07-30 14:29:19'),
(9, 'fffffffffff', 'ddddddddd@eweq', '1123421211', 'cddqdqdqq', '2021-07-30 15:11:36'),
(10, 'dqdqd', 'dqwdwqd@assa', '123211', 'ssdsdadasd', '2021-08-05 07:39:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
