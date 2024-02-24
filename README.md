<h1 align="center">Welcome to fastapi-apps 👋</h1>

> This repository contains two demo applications built with [FastAPI](https://fastapi.tiangolo.com), managed as a monorepo using [Moon](https://moonrepo.dev).

## Applications

1. **[App 1](./apps/app1/README.md)**: This application is set up using the `poetry` approach for dependency management.
2. **[App 2](./apps/app2/README.md)**: This application is set up using the traditional `requirements.txt` approach for dependency management.

## Getting Started

### Prerequisites

- **Python**: You have installed Python 3.8 or higher. If you need to install a specific version of Python, we recommend using [pyenv](https://github.com/pyenv/pyenv).
- **Moon**: You have installed [Moon](https://moonrepo.dev/), which is used to manage this monorepo.
- **Dependency Management Tools**: Depending on the application, you will need different tools:
  - For App 1, you need pip, which is typically installed with Python.
  - For App 2, you need [Poetry](https://python-poetry.org) for dependency management.

### Installation

1. Clone the repo
2. Run `moon run :install` to install dependencies for both apps

### Running the Apps

Use Moon to run the apps:

#### Run Server

- Run App 1 with `moon run app1:dev`

#### Run Tests

- Run App 2 with `moon run app2:test`

## Resources

- [Tutorial - User Guide - FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Best Practices and Conventions we used at our startup](https://github.com/zhanymkanov/fastapi-best-practices)
- [Full stack, modern web application generator. Using FastAPI, PostgreSQL as database, Docker, automatic HTTPS and more.](https://github.com/tiangolo/full-stack-fastapi-postgresql)

## Author

👤 **Huynh Duc Dung**

- Website: https://productsway.com/
- Twitter: [@jellydn](https://twitter.com/jellydn)
- Github: [@jellydn](https://github.com/jellydn)

## Show your support

Give a ⭐️ if this project helped you!

[![kofi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/dunghd)
[![paypal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/dunghd)
[![buymeacoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/dunghd)
