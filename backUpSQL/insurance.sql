-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2019 at 10:39 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `insurance`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add car', 7, 'add_car'),
(26, 'Can change car', 7, 'change_car'),
(27, 'Can delete car', 7, 'delete_car'),
(28, 'Can view car', 7, 'view_car'),
(29, 'Can add customer', 8, 'add_customer'),
(30, 'Can change customer', 8, 'change_customer'),
(31, 'Can delete customer', 8, 'delete_customer'),
(32, 'Can view customer', 8, 'view_customer'),
(33, 'Can add employee', 9, 'add_employee'),
(34, 'Can change employee', 9, 'change_employee'),
(35, 'Can delete employee', 9, 'delete_employee'),
(36, 'Can view employee', 9, 'view_employee'),
(37, 'Can add package', 10, 'add_package'),
(38, 'Can change package', 10, 'change_package'),
(39, 'Can delete package', 10, 'delete_package'),
(40, 'Can view package', 10, 'view_package'),
(41, 'Can add promotion', 11, 'add_promotion'),
(42, 'Can change promotion', 11, 'change_promotion'),
(43, 'Can delete promotion', 11, 'delete_promotion'),
(44, 'Can view promotion', 11, 'view_promotion'),
(45, 'Can add insure', 12, 'add_insure'),
(46, 'Can change insure', 12, 'change_insure'),
(47, 'Can delete insure', 12, 'delete_insure'),
(48, 'Can view insure', 12, 'view_insure');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$CwZ0FW0uvMF1$Akn9l72eMqWSAbsCIV1CBXvNgFb3wm11ovKjOusuI/c=', '2019-04-24 15:13:21.734161', 1, 'boom', '', '', '58070035@it.kmitl.ac.th', 1, 1, '2019-04-24 15:13:14.872223');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customer_car`
--

CREATE TABLE `customer_car` (
  `id` int(11) NOT NULL,
  `car_id` varchar(30) NOT NULL,
  `car_number` varchar(30) NOT NULL,
  `province` varchar(30) NOT NULL,
  `brand` varchar(30) NOT NULL,
  `chassis_number` varchar(30) NOT NULL,
  `model` varchar(30) NOT NULL,
  `car_cc` int(11) NOT NULL,
  `car_type` varchar(30) NOT NULL,
  `sit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `customer_customer`
--

CREATE TABLE `customer_customer` (
  `id` int(11) NOT NULL,
  `cus_id` varchar(30) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `province` varchar(30) NOT NULL,
  `zipcode` varchar(5) NOT NULL,
  `id_card` varchar(13) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `cus_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-04-24 15:21:33.372290', '1', 'ID: 1 ,boom', 2, '[{\"changed\": {\"fields\": [\"fname\", \"lname\", \"id_card\", \"phone1\", \"phone2\", \"email\", \"address\", \"remark\"]}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'customer', 'car'),
(8, 'customer', 'customer'),
(9, 'employee_control', 'employee'),
(12, 'insurance', 'insure'),
(10, 'package_control', 'package'),
(11, 'package_control', 'promotion'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-04-24 14:43:01.716437'),
(2, 'auth', '0001_initial', '2019-04-24 14:43:09.444033'),
(3, 'admin', '0001_initial', '2019-04-24 14:43:12.512730'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-04-24 14:43:12.605831'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-24 14:43:12.877040'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-04-24 14:43:13.821580'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-04-24 14:43:14.412027'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-04-24 14:43:15.261250'),
(9, 'auth', '0004_alter_user_username_opts', '2019-04-24 14:43:15.296339'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-04-24 14:43:15.964767'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-04-24 14:43:16.009041'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-04-24 14:43:16.050114'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-04-24 14:43:16.833484'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-04-24 14:43:17.966196'),
(15, 'sessions', '0001_initial', '2019-04-24 14:43:18.370989'),
(16, 'customer', '0001_initial', '2019-04-24 14:57:33.872919'),
(17, 'employee_control', '0001_initial', '2019-04-24 15:00:14.765676'),
(18, 'package_control', '0001_initial', '2019-04-24 15:02:16.585598'),
(19, 'insurance', '0001_initial', '2019-04-24 15:03:29.309410'),
(20, 'employee_control', '0002_auto_20190424_1522', '2019-04-24 15:22:54.250279'),
(21, 'employee_control', '0003_auto_20190424_1534', '2019-04-24 15:34:16.001069');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5mq39ap13sqoc5ce37xwis6ym7mmdriq', 'YzU0YWE4NDQ4YTk3M2JhYTRmODIwMzZkZGIwMzFjMGZkMzdiN2E3Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyN2FiMDJjMTUzNTUyN2I2ZDQ4MjgzNDVkMTczYmYzYjEyZjA2MjkzIn0=', '2019-05-08 15:13:21.809909');

-- --------------------------------------------------------

--
-- Table structure for table `employee_control_employee`
--

CREATE TABLE `employee_control_employee` (
  `id` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `id_card` varchar(13) NOT NULL,
  `phone1` varchar(15) NOT NULL,
  `phone2` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `address` varchar(200) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `role` varchar(30) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `distinct` varchar(30) DEFAULT NULL,
  `province` varchar(30) DEFAULT NULL,
  `sub_district` varchar(30) DEFAULT NULL,
  `zipcode` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employee_control_employee`
--

INSERT INTO `employee_control_employee` (`id`, `fname`, `lname`, `id_card`, `phone1`, `phone2`, `email`, `address`, `remark`, `role`, `user_id`, `distinct`, `province`, `sub_district`, `zipcode`) VALUES
(1, 'boom', 'ber', '11111111111', '0888874866', '', '58070035@it.kmitl.ac.th', 'ทวีวัฒนา', 'เป็นแอดมินจ้า', 'admin', 1, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `insurance_insure`
--

CREATE TABLE `insurance_insure` (
  `id` int(11) NOT NULL,
  `doc_nbr` varchar(30) DEFAULT NULL,
  `car_number` varchar(15) DEFAULT NULL,
  `company_order` varchar(30) DEFAULT NULL,
  `price` double NOT NULL,
  `total_price` double NOT NULL,
  `post_date` date DEFAULT NULL,
  `agent_code_id` int(11) NOT NULL,
  `car_id_id` int(11) DEFAULT NULL,
  `cus_id_id` int(11) DEFAULT NULL,
  `package_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `package_control_package`
--

CREATE TABLE `package_control_package` (
  `id` int(11) NOT NULL,
  `package_id` varchar(30) DEFAULT NULL,
  `package_name` varchar(30) DEFAULT NULL,
  `company_name` varchar(30) DEFAULT NULL,
  `package_cc` int(11) NOT NULL,
  `package_type` varchar(30) DEFAULT NULL,
  `price` double NOT NULL,
  `detail` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `package_control_promotion`
--

CREATE TABLE `package_control_promotion` (
  `id` int(11) NOT NULL,
  `promotion_name` varchar(30) NOT NULL,
  `promotion_detail` varchar(200) NOT NULL,
  `end_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `customer_car`
--
ALTER TABLE `customer_car`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_customer`
--
ALTER TABLE `customer_customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employee_control_employee`
--
ALTER TABLE `employee_control_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `insurance_insure`
--
ALTER TABLE `insurance_insure`
  ADD PRIMARY KEY (`id`),
  ADD KEY `insurance_insure_agent_code_id_4006f937_fk_employee_` (`agent_code_id`),
  ADD KEY `insurance_insure_car_id_id_1b7b5630_fk_customer_car_id` (`car_id_id`),
  ADD KEY `insurance_insure_cus_id_id_241a9a61_fk_customer_customer_id` (`cus_id_id`),
  ADD KEY `insurance_insure_package_id_id_45df6228_fk_package_c` (`package_id_id`);

--
-- Indexes for table `package_control_package`
--
ALTER TABLE `package_control_package`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `package_control_promotion`
--
ALTER TABLE `package_control_promotion`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_car`
--
ALTER TABLE `customer_car`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_customer`
--
ALTER TABLE `customer_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `employee_control_employee`
--
ALTER TABLE `employee_control_employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `insurance_insure`
--
ALTER TABLE `insurance_insure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `package_control_package`
--
ALTER TABLE `package_control_package`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `package_control_promotion`
--
ALTER TABLE `package_control_promotion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `employee_control_employee`
--
ALTER TABLE `employee_control_employee`
  ADD CONSTRAINT `employee_control_employee_user_id_b7aa06dc_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `insurance_insure`
--
ALTER TABLE `insurance_insure`
  ADD CONSTRAINT `insurance_insure_agent_code_id_4006f937_fk_employee_` FOREIGN KEY (`agent_code_id`) REFERENCES `employee_control_employee` (`id`),
  ADD CONSTRAINT `insurance_insure_car_id_id_1b7b5630_fk_customer_car_id` FOREIGN KEY (`car_id_id`) REFERENCES `customer_car` (`id`),
  ADD CONSTRAINT `insurance_insure_cus_id_id_241a9a61_fk_customer_customer_id` FOREIGN KEY (`cus_id_id`) REFERENCES `customer_customer` (`id`),
  ADD CONSTRAINT `insurance_insure_package_id_id_45df6228_fk_package_c` FOREIGN KEY (`package_id_id`) REFERENCES `package_control_package` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
