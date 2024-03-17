FROM nginx:latest

# Create admin user and group
RUN addgroup --system admin \
    && useradd --system --shell /bin/false --no-create-home --home-dir /app -g admin admin

# Set working directory
WORKDIR /app

# Copy NGINX configuration and HTML files
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html

# Set ownership and permissions
RUN chown -R admin:admin /app \
    && chmod -R 755 /app \
    && chown -R admin:admin /var/cache/nginx \
    && chown -R admin:admin /var/log/nginx \
    && chown -R admin:admin /etc/nginx/conf.d \
    && touch /var/run/nginx.pid \
    && chown -R admin:admin /var/run/nginx.pid

# Switch to admin user
USER admin

