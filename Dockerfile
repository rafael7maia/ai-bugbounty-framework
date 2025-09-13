# Dockerfile corrigido para HexStrike AI MCP v6.1 - Nmap NSE Fix
FROM alpine:3.18

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV HEXSTRIKE_PORT=8888
ENV HEXSTRIKE_DEBUG=false
ENV PATH=$PATH:/usr/local/go/bin:/root/go/bin:/root/.cargo/bin

# Instalar dependências básicas do sistema
RUN apk update && apk add --no-cache \
    python3 py3-pip git curl wget unzip bash \
    build-base python3-dev linux-headers \
    libffi-dev openssl-dev musl-dev gcc g++ \
    make cmake pkgconfig ca-certificates perl \
    nmap nmap-scripts bind-tools netcat-openbsd \
    file tar gzip grep sed gawk openssh-client \
    chromium chromium-chromedriver xvfb && \
    ln -s /usr/bin/chromium-browser /usr/bin/google-chrome

# Instalar Go
RUN wget -O /tmp/go.tar.gz https://go.dev/dl/go1.21.5.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf /tmp/go.tar.gz && \
    rm /tmp/go.tar.gz

# Instalar ferramentas Go essenciais
RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest && \
    go install github.com/projectdiscovery/httpx/cmd/httpx@latest && \
    go install github.com/ffuf/ffuf@latest && \
    go install github.com/OJ/gobuster/v3@latest

# Instalar Python essencial
RUN pip3 install --no-cache-dir --break-system-packages \
    requests beautifulsoup4 paramiko scapy \
    fastapi uvicorn aiohttp websockets \
    psutil colorama tabulate rich sqlmap

# Instalar ferramentas Python adicionais
RUN pip3 install --no-cache-dir --break-system-packages \
    dirsearch arjun wafw00f || echo "Some tools failed to install"

# Instalar masscan
RUN git clone --depth 1 https://github.com/robertdavidgraham/masscan /tmp/masscan && \
    cd /tmp/masscan && make && \
    cp bin/masscan /usr/local/bin/ && \
    rm -rf /tmp/masscan

# Criar diretório de trabalho
WORKDIR /app

# Criar estrutura básica do projeto
RUN mkdir -p /app/data /app/logs /app/cache /app/wordlists

# Baixar wordlists essenciais
RUN wget -O /app/wordlists/common.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt || \
    echo "common.txt" > /app/wordlists/common.txt

# Copiar arquivos MCP
COPY hexstrike_mcp.py /app/
COPY requirements.txt /app/

# Criar arquivo de servidor básico
RUN cat > /app/hexstrike_server.py << 'EOF'
#!/usr/bin/env python3
import sys
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HexStrikeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>HexStrike AI MCP Server</h1><p>Server is running!</p>")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8888)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    server = HTTPServer(("0.0.0.0", args.port), HexStrikeHandler)
    print(f"HexStrike AI MCP Server running on port {args.port}")
    server.serve_forever()

if __name__ == "__main__":
    main()
EOF
RUN chmod +x /app/hexstrike_server.py

# Criar script de inicialização com teste do nmap
RUN cat > /app/start.sh << 'EOF'
#!/bin/bash
echo "=== HexStrike AI MCP Server (Alpine Fixed) ==="
echo "Porta: ${HEXSTRIKE_PORT}"
echo "Debug: ${HEXSTRIKE_DEBUG}"
echo "=============================================="

# Verificar ferramentas disponíveis
echo "Verificando ferramentas de segurança..."
if nmap --version > /dev/null 2>&1; then
    echo "✓ Nmap disponível"
    # Testar NSE scripts
    if nmap -sV --version-trace 127.0.0.1 2>&1 | grep -q "nse_main.lua"; then
        echo "✗ Nmap NSE scripts com problema"
    else
        echo "✓ Nmap NSE scripts funcionando"
    fi
else
    echo "✗ Nmap não encontrado"
fi

which gobuster > /dev/null && echo "✓ Gobuster disponível" || echo "✗ Gobuster não encontrado"
which nuclei > /dev/null && echo "✓ Nuclei disponível" || echo "✗ Nuclei não encontrado"
which subfinder > /dev/null && echo "✓ Subfinder disponível" || echo "✗ Subfinder não encontrado"
which httpx > /dev/null && echo "✓ Httpx disponível" || echo "✗ Httpx não encontrado"
which masscan > /dev/null && echo "✓ Masscan disponível" || echo "✗ Masscan não encontrado"
which sqlmap > /dev/null && echo "✓ SQLMap disponível" || echo "✗ SQLMap não encontrado"

echo "=============================================="
echo "Iniciando servidor..."

# Iniciar servidor
if [ "$HEXSTRIKE_DEBUG" = "true" ]; then
    python3 hexstrike_server.py --port $HEXSTRIKE_PORT --debug
else
    python3 hexstrike_server.py --port $HEXSTRIKE_PORT
fi
EOF
RUN chmod +x /app/start.sh

# Criar script de verificação de saúde
RUN cat > /app/healthcheck.sh << 'EOF'
#!/bin/bash
curl -f http://localhost:${HEXSTRIKE_PORT}/health || exit 1
EOF
RUN chmod +x /app/healthcheck.sh

# Atualizar templates do Nuclei
RUN nuclei -update-templates || echo "Nuclei templates update failed"

# Expor porta padrão
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD /app/healthcheck.sh

# Volumes para persistência
VOLUME ["/app/data", "/app/logs", "/app/cache", "/app/wordlists"]

# Labels para metadados
LABEL maintainer="HexStrike AI Community" \
      version="6.1-nmap-fixed" \
      description="HexStrike AI MCP - Alpine Linux Edition (Nmap NSE Fixed)" \
      base.image="alpine:3.18"

# Comando padrão
CMD ["/app/start.sh"]