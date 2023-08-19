# fastapi-eb-template
Base template using [FastAPI](https://fastapi.tiangolo.com/) and [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).

[![CI](https://github.com/andreyrcdias/fastapi-eb-template/actions/workflows/ci.yaml/badge.svg)](https://github.com/andreyrcdias/fastapi-eb-template/actions/workflows/ci.yaml)


## Prerequisites
* [Python 3.11](https://www.python.org/downloads/release/python-3110/)
* [AWS Elastic Beanstalk CLI](https://docs.aws.amazon.com/elastic-beanstalk/index.html)


## Quick setup
1. Create and activate [virtual environment](https://docs.python.org/3/library/venv.html):
```bash
python3 -m venv .venv && source .venv/bin/activate
```

2. Install the dependencies:
```bash
make install
```

3. Run the application:
```bash
make run
```


## Maintenance
To format the code, run:
```bash
make fmt
```


To run the tests, run:
```bash
make tests
```


## Building and Deployment
First, we need to create an Elastic Beanstalk Application.
```bash
eb create
```

Now, we can create an Application environment:
For deployment, run:
```bash
eb deploy
```
