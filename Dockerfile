

# --- Build Stage ---
FROM python:3.11-alpine AS builder


# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=production


# Set work directory
WORKDIR /install



# Install build dependencies only
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev


# Copy requirements file
COPY requirements.txt .


# Install Python dependencies to a temp folder
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt


# --- Final Stage ---
FROM python:3.11-alpine

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=production

# Set work directory
WORKDIR /app

# Install runtime dependencies only
RUN apk add --no-cache libffi

# Copy installed python packages from builder
COPY --from=builder /install /usr/local

# Copy only necessary project files
COPY app.py .
COPY requirements.txt .
COPY templates ./templates
COPY static ./static



# Create a non-root user for Alpine
RUN adduser -D appuser \
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]