# Serviços Necessários - HexStrike AI 🔧

## 🚀 **Serviços que DEVEM estar rodando:**

### **1. Docker Desktop**
- ✅ **Status:** Deve estar rodando
- 🔧 **Como verificar:** `docker ps`
- 💡 **Iniciar:** Abrir Docker Desktop

### **2. HexStrike AI Container (v2)**
- ✅ **Status:** Deve estar ativo na porta 8888
- 🔧 **Como verificar:** `curl http://localhost:8888/health`
- 💡 **Iniciar:** `docker start hexstrike-ai`
- 📦 **Imagem:** hexstrike-ai:v2 (nmap corrigido)

### **3. LM Studio Server**
- ✅ **Status:** Deve estar ativo na porta 1234
- 🔧 **Como verificar:** `curl http://localhost:1234/v1/models`
- 💡 **Iniciar:** LM Studio → Local Server → Start Server

## 📋 **Checklist de Verificação:**

```bash
# 1. Verificar Docker
docker ps

# 2. Verificar HexStrike AI
curl http://localhost:8888/health

# 3. Verificar LM Studio
curl http://localhost:1234/v1/models

# 4. Verificar MCP
docker exec hexstrike-ai python3 /app/hexstrike_mcp.py --help
```

## ⚙️ **Comandos de Inicialização:**

### **Iniciar Tudo:**
```bash
# 1. Iniciar container (se parado)
docker start hexstrike-ai

# 2. Verificar se está funcionando
curl http://localhost:8888/health

# 3. Abrir LM Studio e iniciar servidor na porta 1234
```

### **Parar Tudo:**
```bash
# 1. Parar container
docker stop hexstrike-ai

# 2. Parar LM Studio (interface)
```

## 🎯 **Status Ideal:**
- ✅ Docker Desktop rodando
- ✅ Container `hexstrike-ai` ativo (porta 8888)
- ✅ LM Studio servidor ativo (porta 1234)
- ✅ VS Code com Continue ou Copilot configurado

**Quando todos estiverem ativos, o sistema está pronto para uso! 🚀**