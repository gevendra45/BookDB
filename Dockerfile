FROM python:3.7-slim
RUN apt-get update && apt-get install -y \
    python3 python3-dev gcc \
    gfortran musl-dev 
RUN apt-get install libenchant1c2a -y
RUN pip install -r requirements.txt && ls
RUN chmod 777 my_wrapper_script.sh
CMD ./my_wrapper_script.sh