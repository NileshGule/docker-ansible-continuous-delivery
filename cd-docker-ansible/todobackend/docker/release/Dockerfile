FROM nileshgule/todobackend-base:latest
MAINTAINER Nilesh Gule <vn_nilesh@yahoo.com>

# Copy application artifacts
COPY target /wheelhouse

# Install the application
RUN . /appenv/bin/activate && \
  pip install --no-index -f /wheelhouse todobackend && \
  rm -rf /wheelhouse
