FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir --only-binary=:all: -r ./requirements.txt

WORKDIR ${LAMBDA_TASK_ROOT}
COPY handler.py ${LAMBDA_TASK_ROOT}
COPY src ${LAMBDA_TASK_ROOT}/src

CMD ["handler.handler"]