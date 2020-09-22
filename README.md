# Keep It

![Keep It Brand](https://raw.githubusercontent.com/castilhoin/keep-it/main/Keep-It.png)

## Description

Keep It is a simple web application to manage notes and keep things organized. Here, the user can manage multiple notebooks, organize their ideas, and keep everything safe with an encrypted password.

This is my **CS50's final project**. My first application developed in Python/Flask.

### Tech Stack

- Python/Flask
- SQLite3
- Flask-SQLAlchemy
- Flask-Login

## Preparing the Environment

```sh
git clone https://github.com/castilhoin/keep-it.git
cd keep-it
python3 -m venv venv
source venv/bin/activate
```

## Running the Application

```sh
make install && make run
```

Visit http://localhost:5000

## Conclusion

### Learning

I already had a professional experience with front-end development. But, it was my first experience developing the back-end of an application in Python. During approximately a year, I studied Python programming, and developed simple command-line programs. But only during **CS50** course, I could learn many Computer Science concepts that were really important to develop web applications. I had my first contact with databases, and I could understand how to make SQL queries and use an ORM to easily manage multiple queries. In this project, I focused on developing a complete and useful application from scratch using the Flask web framework.

Flask uses a design pattern called *application factory*. In this way, it is possible to break the application into multiple instances and *connect* them according the needs. During the development, I created five extensions: cli, config, db, login, and site. In the future, I can create and connect more extensions like tasks, calendar, projects, and more, in order to offer new tools for the users.

### Points to Improve

- Handle exceptions with try/catch
- Write tests
- Improve web accessibility