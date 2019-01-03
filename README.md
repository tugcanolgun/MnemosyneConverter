# Mnemosyne Converter

This is a very basic API to connect annotatorjs module with the W3C Annotation server in main Mnemosyne project.

It comes with ready to deploy options using uwsgi. Settings of the uwsgi can be found in `server.ini` file.

## Dependencies

> It heavily uses type annotations.

Python3.6 and higher is required. As it uses type annotations, it is highly recommended to use python 3.7+

`python3.7 -m venv .env`

`source .env/bin/activate`

`pip install -r requirements.txt`

### Running as is

Not a production choice but may be useful for testing.

`python server.py`

### Running with uwsgi

Useful for prior systemd check.

`uwsgi --socket 0.0.0.0:5100 --protocol=http -w wsgi:app`

## Deployment with systemd

```
[Unit]
Description=Annotatorjs converter
After=network.target

[Service]
User=user1
Group=www-data
WorkingDirectory=/home/user1/server
Environment="PATH=/home/user1/server/.env/bin"
ExecStart=/home/user1/server/.env/bin/uwsgi --ini server.ini

[Install]
WantedBy=multi-user.target
```
