FROM ghcr.io/marimo-team/marimo:latest-sql
EXPOSE 8080
WORKDIR /app
COPY . .
# Install any additional dependencies here
RUN pip3 install -r requirements.txt
CMD ["marimo", "edit", "--no-token", "-p", "8080", "--host", "0.0.0.0"]