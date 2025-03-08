ARG BASE_IMAGE
FROM $BASE_IMAGE

COPY playapp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY playapp/ playapp
CMD ["uvicorn", "playapp.main:app", "--host", "0.0.0.0", "--port", "8080"]