Sure! Here is the `README.md` content formatted in Markdown code:

```markdown
# Inception Project

Welcome to the **Inception Project**! 🌟

This project is all about setting up a modern, scalable, and secure web infrastructure using Docker. Think of it as building a mini web empire where each part works seamlessly with the others. If you’re curious about how websites are managed and want to dive into the world of system administration and containerization, you’re in the right place!

## 🎯 What’s This All About?

In this project, you’ll create a robust web infrastructure on your own virtual machine. We’ll use Docker to containerize different services, ensuring they work perfectly together. Here’s a breakdown of what you’ll build:

- **NGINX**: This is your web server that will handle all incoming traffic and provide secure connections with TLS.
- **WordPress**: The platform where your website lives, but without the web server – that’s NGINX’s job!
- **MariaDB**: The database that stores all your website’s data.
- **Volumes**: Think of these as storage spaces – one for your WordPress files and another for your database.
- **Network**: This connects everything so that your web server, website, and database can talk to each other.

## 🚀 Getting Started

Here’s how you can set up everything:

### 1. **Clone the Repository**

First, get your hands on the project files:

```bash
git clone https://github.com/yourusername/inception.git
cd inception
```

### 2. **Prepare Your Environment**

Ensure you have Docker and Docker Compose installed on your virtual machine. If not, follow the installation guides for [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

### 3. **Set Up Your Project**

Inside the project folder, you’ll find a `Makefile`. Run the following command to build and set up your Docker containers:

```bash
make
```

This will read the `docker-compose.yml` file and build all the necessary Docker images and containers.

### 4. **Configuration**

Edit the `.env` file to set your environment variables. This file includes:

- **DOMAIN_NAME**: Your website’s domain (e.g., `yourlogin.42.fr`).
- **CERTS**: Path to your TLS certificates.
- **MYSQL_ROOT_PASSWORD**: Root password for MariaDB.
- **MYSQL_USER** and **MYSQL_PASSWORD**: Database user credentials.

Make sure to replace placeholders with your actual information.

### 5. **Access Your Website**

Once everything is set up, you can visit your website by navigating to `https://yourlogin.42.fr` in your web browser. 

## 📁 Directory Structure

Here’s a quick look at the project structure:

```
inception/
├── Makefile
├── srcs/
│   ├── docker-compose.yml
│   ├── .env
│   ├── requirements/
│       ├── mariadb/
│       ├── nginx/
│       ├── wordpress/
```

- **Makefile**: Automates the build process.
- **srcs/docker-compose.yml**: Defines how your containers interact.
- **srcs/.env**: Contains environment variables.
- **srcs/requirements/**: Contains Dockerfiles and configuration for each service.

## 💡 Tips

- **Security**: Make sure your `.env` file is secure and not shared publicly.
- **Troubleshooting**: If you run into issues, check Docker logs for details.

## 📚 Learn More

If you want to dive deeper into Docker, NGINX, WordPress, or MariaDB, here are some resources to check out:

- [Docker Documentation](https://docs.docker.com/)
- [NGINX Documentation](https://nginx.org/en/docs/)
- [WordPress Documentation](https://wordpress.org/support/)
- [MariaDB Documentation](https://mariadb.com/kb/en/documentation/)



Feel free to replace placeholders like `yourusername` and `your-email@example.com` with your actual details.
