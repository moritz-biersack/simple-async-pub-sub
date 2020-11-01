# Simple Async Pub/Sub

This is an example for using Redis to set up a simple asynchronous
Publish/Subscribe system.

There is a input service that listens for HTTP requests and publishes
a message in a Redis channel. On the other side there is a output service
that subscribes to the channel and (as an example) prints the message
it receives.

## Components

The project uses Docker Compose to start three services:

- Redis
- Input service
  - Based on Flask
  - Listens for GET requests on port 5000
  - Query parameter "message" can be used to alter the message
  - Publishes messages to a channel
- Output service
  - Loop that listens for messages from the channel
  - Prints message

## Run

Build and start the services:

```bash
# Build the input and output images
docker-compose build

# Start all services
docker-compose up
```

Now you can send a request to the input service by querying port 5000 on the
host:

```bash
curl 'localhost:5000/?message=foobar'
```

You will see the message being printed in the Docker Compose logs.
