# Inception Project

## Introduction

Welcome to the **Inception Project**! This project is a comprehensive introduction to Docker and containerized applications. By setting up a fully functional environment with **Nginx**, **WordPress**, and **MariaDB**, this project demonstrates the power and flexibility of containerization in modern software development.

## Project Overview

The Inception project involves creating a multi-container setup to host a WordPress site with an Nginx web server and a MariaDB database. This setup is designed to provide a solid foundation for understanding how these components interact in a containerized environment.

### Key Components

1. **Nginx**: A high-performance web server used to serve web pages and manage traffic.
2. **WordPress**: A popular content management system (CMS) that powers websites and blogs.
3. **MariaDB**: A robust and reliable database management system that stores the data for WordPress.

## Goals

- **Containerization**: Learn how to use Docker to create isolated environments for each component of the stack.
- **Integration**: Understand how Nginx, WordPress, and MariaDB work together within a Docker setup.
- **Configuration**: Gain experience in configuring Nginx to work with WordPress and managing database connections.

## Setup 

### Docker Compose

The project uses Docker Compose to define and manage the multi-container setup. Docker Compose simplifies the process of configuring and running multi-container applications.

### Nginx Configuration

The Nginx server is configured to handle incoming requests and route them to the WordPress container. Custom configurations ensure that the server performs efficiently and securely.

### WordPress

WordPress is set up to run in a Docker container, connected to the MariaDB container for database management. Configuration files are provided to ensure seamless integration with Nginx and MariaDB.

### MariaDB

MariaDB is used to store all WordPress data. The database container is configured to provide reliable data storage and retrieval for the WordPress site.

## Technical Details

- **Dockerfile**: Custom Dockerfiles are provided for each component, specifying the setup and configuration of Nginx, WordPress, and MariaDB.
- **docker-compose.yml**: The Docker Compose file defines the services, networks, and volumes required for the application.
- **nginx.conf**: Custom Nginx configuration to manage requests and ensure proper routing to the WordPress container.


## Usage

- **WordPress Admin**: Access the WordPress admin panel to configure and manage your site at `https://www.hed-dyb.42.fr/wp-admin`.
- **Database Management**: Use tools like phpMyAdmin or MySQL Workbench to manage the MariaDB database if needed.

## Conclusion

The Inception Project is a powerful way to understand the fundamentals of containerization and how different services interact within a Docker environment. By setting up Nginx, WordPress, and MariaDB, you'll gain practical experience in managing and configuring a complete web application stack.
