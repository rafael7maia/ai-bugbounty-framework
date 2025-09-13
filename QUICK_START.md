# 🚀 AI Bug Bounty Framework v3.0 - Quick Start

## ⚡ 3-Step Setup

### 1. Build HexStrike Container
```bash
docker build -t hexstrike-ai:v3 .
docker run -d --name hexstrike-ai -p 8888:8888 hexstrike-ai:v3
```

### 2. Test MCP Script
```bash
python simple_mcp.py nmap_scan testphp.vulnweb.com
```

### 3. Use with Amazon Q
Copy prompts from `AMAZON_Q_PROMPTS.md` and start analyzing!

## 🎯 Architecture
- **HexStrike AI Container**: 150+ security tools (Docker)
- **Simple MCP**: Python script for tool execution  
- **Amazon Q**: AI analysis and reporting

## 📖 Full Documentation
- `README.md` - Complete guide
- `ARCHITECTURE_V3.md` - Technical details
- `AMAZON_Q_PROMPTS.md` - AI prompts