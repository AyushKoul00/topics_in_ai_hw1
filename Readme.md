# AI-Driven Personal Portfolio Website

This project is an interactive resume and portfolio website hosted on an Amazon EC2 instance. It features an AI-powered chatbot and a contact form with submissions stored in an SQLite database.

## Features

- Interactive resume and portfolio
- AI-powered chatbot for user interaction
- Contact form with SQLite database storage
- Hosted on Amazon EC2
- Nginx reverse proxy for improved performance and security

## Prerequisites

- Amazon EC2 instance
- Python 3.x
- Git

## Setup Instructions

### 1. Connect to EC2 and Set Up Environment

1. Update system packages:

   ```bash
   sudo yum update -y
   ```

2. Install Git:

   ```bash
   sudo yum install git -y
   ```

3. Clone the repository:

   ```bash
   git clone https://github.com/AyushKoul00/topics_in_ai_hw1.git
   cd topics_in_ai_hw1
   ```

4. Set up environment variables:

   - Add your API key to the `.env` file:
     ```
     API_KEY="your-api-key-here"
     ```

5. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install eventlet gunicorn
   ```

### 2. Configure and Run the Application

1. Run the Flask application (for testing):

   ```bash
   flask --app app run --debug
   ```

2. Run with Gunicorn:
   ```bash
   gunicorn -b 0.0.0.0:8000 app:app
   ```

### 3. Set Up Systemd Service

1. Create a service file:

   ```bash
   sudo vi /etc/systemd/system/portfolio.service
   ```

2. Add the following configuration:

   ```ini
   [Unit]
   Description=Portfolio website in Flask
   After=network.target

   [Service]
   User=ec2-user
   Group=ec2-user
   WorkingDirectory=/home/ec2-user/topics_in_ai_hw1
   ExecStart=/home/ec2-user/topics_in_ai_hw1/.venv/bin/gunicorn --worker-class eventlet -w 1 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start portfolio
   sudo systemctl enable portfolio
   ```

### 4. Set Up Nginx Reverse Proxy

1. Install Nginx:

   ```bash
   sudo yum install nginx -y
   ```

2. Configure Nginx:

   ```bash
   sudo vi /etc/nginx/nginx.conf
   ```

3. Add the following configuration inside the `http` block:

   ```nginx
   upstream flaskportfolio {
       server 127.0.0.1:8000;
   }

   location / {
       proxy_pass http://flaskportfolio;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "Upgrade";
       proxy_set_header Host $host;
       proxy_cache_bypass $http_upgrade;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
   }
   ```

4. Restart Nginx:
   ```bash
   sudo systemctl restart nginx
   sudo nginx -t
   sudo systemctl reload nginx
   ```

### 5. Configure Security Group

Add an inbound rule for HTTP (port 80) allowing access from Anywhere IPv4.

## Monitoring and Troubleshooting

- View service logs:

  ```bash
  journalctl -u portfolio.service -b
  ```

- Restart the service:
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl restart portfolio
  ```

## Future Enhancements

- Add loading/typing indicators for the chatbot
- Implement resizable windows for better user experience
- Enhance styling for improved inclusivity and accessibility

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## How to run the app in Flask (development mode)

### Windows (Powershell)
```ps
python -m venv .venv
.\.venv\Scripts\activate
pip install -r .\requirements.txt
flask --app app run --debug
```
