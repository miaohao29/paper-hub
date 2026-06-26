#!/bin/bash

# Create uploads directory
mkdir -p uploads lancedb logs

# Run database migrations
alembic upgrade head

# Start server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
