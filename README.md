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
- Hosting
    - AWS EC2

## Working demo
### Video:
[![Watch the video]()](https://github.com/UtkarshRastogi0712/Vaartalaap/assets/53490007/87d17659-16c1-4cd6-bf0c-675fa9a54e64)

### Image:
<img width="953" alt="VaartalaapSS" src="https://github.com/UtkarshRastogi0712/Vaartalaap/assets/53490007/dbdc2027-a466-4640-939c-c141da3d0bf1">
