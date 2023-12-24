# Vaartalaap
Vaartalaap is a real-time chatroom based on WebSocket built using Django. Communicate seemlessly in global or private chatrooms.

Deployment: [link](http://3.108.196.226:8000/chat/)

## Features
- Realtime communication across global or private chatrooms.
- Chat with multiple users at the same time.
- Custom chatroom IDs for private rooms.
- Chat notifications when a user joins the room.
- Tokenise the message by prepending ":tokenise:" before at message.
  
## Usage
- Navigate to the [Homepage](http://3.108.196.226:8000/chat/)
- Choose a Username
- Enter a chatroom id to create/join a private room or leave the field empty to join global chatroom
- Use the buttons to send messages or disconnect
- Add ":tokenise:" before the message to deconstruct into constituent parts of speech.

## Tech Stack
- Languages
    - Python
    - Javascript
    - HTML
- Libraries / Frameworks
    - Django
    - Django-channels
    - NLTK
- Database
    - Redis
