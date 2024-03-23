ARG IMAGE_NAME
ARG IMAGE_VERSION

FROM ${IMAGE_NAME}:${IMAGE_VERSION}

WORKDIR /opt/quickselect

COPY pyproject.toml .
COPY README.md .
COPY setup.py .
COPY quickselect quickselect
COPY tests tests

RUN pip install -e .[tests]
