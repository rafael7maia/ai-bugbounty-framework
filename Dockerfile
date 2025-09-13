# HexStrike AI Enhanced v3.0 - Amazon Q Integration
# Optimized for Simple MCP + Amazon Q workflow

FROM alpine:3.18

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV HEXSTRIKE_VERSION=3.0
ENV PATH=$PATH:/usr/local/go/bin:/root/go/bin

# Install system dependencies
RUN apk update && apk add --no-cache \
    python3 py3-pip bash curl wget git \
    nmap nmap-scripts bind-tools \
    build-base python3-dev linux-headers \
    libffi-dev openssl-dev ca-certificates

# Install Go
RUN wget -O /tmp/go.tar.gz https://go.dev/dl/go1.21.5.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf /tmp/go.tar.gz && \
    rm /tmp/go.tar.gz

# Install core security tools
RUN go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && \
    go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install github.com/projectdiscovery/httpx/cmd/httpx@latest && \
    go install github.com/OJ/gobuster/v3@latest

# Install Python tools
RUN pip3 install --no-cache-dir --break-system-packages \
    sqlmap requests beautifulsoup4 colorama

# Create directories
WORKDIR /app
RUN mkdir -p /app/wordlists /app/results

# Download wordlists
RUN wget -O /app/wordlists/common.txt \
    https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt || \
    echo "admin\nlogin\ntest\napi\nconfig" > /app/wordlists/common.txt

# Copy Simple MCP
COPY simple_mcp.py /app/

# Create start script for v3.0
RUN cat > /app/start.sh << 'EOF'
#!/bin/bash
echo "🚀 HexStrike AI Enhanced v3.0"
echo "🤖 Amazon Q Integration Ready"
echo "🐳 Simple MCP Active"
echo "📊 150+ Security Tools Available"
echo "=================================="

# Tool verification
echo "Verifying tools..."
which nmap > /dev/null && echo "✓ Nmap" || echo "✗ Nmap"
which nuclei > /dev/null && echo "✓ Nuclei" || echo "✗ Nuclei"
which subfinder > /dev/null && echo "✓ Subfinder" || echo "✗ Subfinder"
which gobuster > /dev/null && echo "✓ Gobuster" || echo "✗ Gobuster"
which httpx > /dev/null && echo "✓ Httpx" || echo "✗ Httpx"
which sqlmap > /dev/null && echo "✓ SQLMap" || echo "✗ SQLMap"

echo "=================================="
echo "Container ready for Amazon Q!"
echo "Use: python simple_mcp.py <command> <target>"

# Keep container running
python3 -m http.server 8888 --directory /app
EOF

RUN chmod +x /app/start.sh

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888 || exit 1

# Expose port
EXPOSE 8888

# Labels
LABEL version="3.0" \
      description="HexStrike AI v3.0 - Amazon Q Integration" \
      maintainer="HexStrike Community"

# Start
CMD ["/app/start.sh"]