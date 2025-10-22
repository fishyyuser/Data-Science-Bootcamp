# Tiny Python base
FROM python:3.12-alpine
# Set working directory
WORKDIR /app
# Copy only needed files
COPY app.py requirements.txt ./
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port
EXPOSE 5000
# Run the app
CMD ["python", "app.py"]
