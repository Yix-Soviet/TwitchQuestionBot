# Twitch Question Bot

<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/200px-Python-logo-notext.svg.png" weight=200px />
</div>

Description: Bot that answers questions asked by the chat using the OpenAI API (more precisely the Davinci model)

## Used Modules

-  `python-dotenv`
-  `openai`
-  `twitchio`

## How to use

-  Create the `.env` file

-  Complete it with the indications of the `.env.example` file.

-  Execute the command (as a recommendation create a virtual environment)

```
pip -r requirements.txt
```

-  Finally run the program with

```
python main.py
```

# Command(s)

- `?question <message>`: Ask a question