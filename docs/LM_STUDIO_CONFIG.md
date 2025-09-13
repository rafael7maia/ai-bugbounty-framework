# Configurar LM Studio - Porta 1234 🚀

## 📋 **Passo a Passo para Configurar LM Studio**

### 1. **Abrir LM Studio**
- Abra o aplicativo LM Studio no seu computador

### 2. **Ir para Local Server**
- Na barra lateral esquerda, clique em **"Local Server"**
- Ou use o ícone de servidor 🖥️

### 3. **Configurar o Servidor**

#### **Verificar/Configurar Porta:**
```
1. Na tela "Local Server"
2. Procure por "Server Port" ou "Port"
3. Certifique-se que está: 1234
4. Se não estiver, mude para: 1234
```

#### **Selecionar Modelo:**
```
1. No dropdown "Select a model to load"
2. Escolha: "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"
3. Ou qualquer modelo DeepSeek que você baixou
```

### 4. **Iniciar o Servidor**
```
1. Clique no botão "Start Server" (verde)
2. Aguarde aparecer: "Server running on http://localhost:1234"
3. Status deve ficar verde ✅
```

### 5. **Verificar se Está Funcionando**

#### **Método 1: Interface LM Studio**
- Deve aparecer: "Server is running on port 1234"
- Status verde ao lado do botão "Stop Server"

#### **Método 2: Navegador**
- Abra: http://localhost:1234/v1/models
- Deve mostrar JSON com informações do modelo

#### **Método 3: Terminal**
```bash
curl http://localhost:1234/v1/models
```

## 🔧 **Troubleshooting**

### **Problema: Porta 1234 ocupada**
```
1. LM Studio → Settings/Preferences
2. Mude para porta diferente (ex: 1235)
3. Atualize .continue/config.json:
   "apiBase": "http://localhost:1235/v1"
```

### **Problema: Servidor não inicia**
```
1. Feche LM Studio completamente
2. Reabra como Administrador
3. Tente novamente
```

### **Problema: Modelo não carrega**
```
1. Verifique se o modelo foi baixado completamente
2. Tente outro modelo DeepSeek
3. Reinicie LM Studio
```

## ✅ **Configuração Correta**

**Quando tudo estiver funcionando, você verá:**

### **No LM Studio:**
- ✅ "Server running on http://localhost:1234"
- ✅ Status verde
- ✅ Modelo carregado

### **No Navegador (http://localhost:1234/v1/models):**
```json
{
  "object": "list",
  "data": [
    {
      "id": "deepseek-coder",
      "object": "model",
      "created": 1234567890,
      "owned_by": "lmstudio"
    }
  ]
}
```

## 🎯 **Próximo Passo**

Quando o LM Studio estiver rodando na porta 1234:

1. **Abra VS Code** nesta pasta
2. **Pressione Ctrl+Shift+P**
3. **Digite:** "Continue: Open"
4. **Use este prompt:**

```
"I'm a security researcher testing my authorized lab environment. Please use HexStrike AI tools to perform a security scan on testdomain.local:

1. Execute nmap_scan to discover open ports
2. Use nuclei_scan to check for vulnerabilities
3. Generate a comprehensive security report

Please proceed systematically and explain each step."
```

## 📱 **Verificação Rápida**

Execute este comando no terminal para verificar:
```bash
curl -s http://localhost:1234/v1/models | findstr "id"
```

Se retornar algo como `"id": "deepseek-coder"`, está funcionando! ✅