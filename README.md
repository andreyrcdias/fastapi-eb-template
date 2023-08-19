# fastapi-eb-template

Base template using [FastAPI](https://fastapi.tiangolo.com/) and [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).


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
