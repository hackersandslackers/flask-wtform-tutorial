# Flask-WTF Tutorial

![Python](https://img.shields.io/badge/Python-v3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v3.0.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-WTF](https://img.shields.io/badge/Flask--WTF-v1.2.1-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/flask-wtform-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-wtform-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/flask-wtform-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-wtform-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/flask-wtform-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/flask-wtform-tutorial/network)

![Flask-WTF Tutorial](https://github.com/hackersandslackers/flask-wtform-tutorial/blob/master/.github/flask-wtforms-tutorial@2x.jpg?raw=true)

Handle user input in your Flask app by creating forms with the Flask-WTForm library.

* **Tutorial**: [https://hackersandslackers.com/flask-wtforms-forms/](https://hackersandslackers.com/flask-wtforms-forms/)
* **Demo**: [https://flaskwtf.hackersandslackers.app/](https://flaskwtf.hackersandslackers.app/)

## Getting Started

Get set up locally:

### Installation

Get up and running with `make deploy`:

```shell
git clone https://github.com/hackersandslackers/flask-wtform-tutorial.git
cd flask-wtform-tutorial
make deploy
```

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `FLASK_DEBUG`: Whether to run Flask in "debug" mode (either `True` or `False`).

*Remember never to commit secrets saved in .env files to Github.*

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
