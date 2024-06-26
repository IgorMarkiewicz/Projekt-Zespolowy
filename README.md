
# Simple Cooking site

Our project is a recipe sharing website where users can log in to add, rate, and search for recipes by ingredient. Administrators will have the ability to add and delete recipes, as well as moderate user-generated content. In the future, there may be an option to open a chat with recipe creators and engage in conversations with them.



## Features

* User Authentication: Users can create accounts and log in to the website.
* Recipe Management: Logged-in users can add new recipes to the website, including details such as ingredients, preparation instructions, and images.
* Recipe Rating: Users can rate recipes based on their experience.
* Administrator Control: Administrators have the authority to delete inappropriate content, manage user accounts, and add new recipes.
* Content Moderation: Administrators can monitor and moderate user-generated content to ensure quality and appropriateness.
* Future Feature: Chat Functionality: There may be an option for users to chat with recipe creators and discuss recipes or ask questions.

## Installation

Clone the repository

```bash
  git clone https://github.com/IgorMarkiewicz/Projekt-Zespolowy
```

Install requirements

```bash
  pip install -r requirements.txt
```

Migrate the db

```bash
  python manage.py migrate
```

Run development server

```bash
  python manage.py runserver
```

## Tech Stack

**Frontend:** Bootstrap

**Backend:** Django

**Database:** SQLite

## Authors

* [@IgorMarkiewicz](https://github.com/IgorMarkiewicz)
* [@MaciejMatczak2001](https://github.com/MaciejMatczak2001)
* [@JakubBlacha](https://github.com/JakubBlacha)

