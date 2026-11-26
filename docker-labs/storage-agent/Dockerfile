FROM python:3.11-alpine

# Create a dedicated non-root system user and group
RUN addgroup -S devops && adduser -S appuser -G devops

WORKDIR /app
COPY storage_audit.py .

# Give ownership to appuser and switch away from root
RUN chown -R appuser:devops /app
USER appuser

CMD ["python3", "storage_audit.py"]
