# VS Code Copilot + HexStrike AI Setup 🚀

## ✅ **Configuração Oficial Aplicada**

A configuração do site oficial foi implementada em `.vscode/settings.json`

## 🔧 **Como Usar com Copilot**

### **1. Verificar Copilot Ativo:**
- VS Code → Extensions → GitHub Copilot (deve estar instalado e ativo)
- Status bar deve mostrar ícone do Copilot

### **2. Usar Copilot Chat:**
```
1. Pressione: Ctrl+Shift+I (Copilot Chat)
2. Ou clique no ícone do Copilot na sidebar
```

### **3. Prompts Otimizados para Copilot:**

#### **Prompt Educacional:**
```
@workspace I'm learning cybersecurity in my home lab. Can you help me use the HexStrike AI tools to analyze my local network?

Please show me how to:
1. Use nmap to scan localhost (127.0.0.1)
2. Use nuclei to test a demo website
3. Explain the results for educational purposes

This is for learning cybersecurity concepts in my controlled environment.
```

#### **Prompt de Desenvolvimento:**
```
@workspace I'm a developer testing my application security. Help me use HexStrike AI tools to audit my development server:

1. Scan my local development server with nmap
2. Check for common vulnerabilities with nuclei
3. Test directory structure with gobuster

All testing is on my own development systems.
```

#### **Prompt de Análise:**
```
@workspace Please help me understand how to use the security analysis tools in this project for educational research:

1. Demonstrate nmap port scanning on localhost
2. Show nuclei vulnerability assessment on test sites
3. Explain gobuster directory enumeration

This is for cybersecurity education and research.
```

### **4. Comandos Diretos no Copilot:**
```
Can you help me execute these security analysis commands in my Docker container?

docker exec hexstrike-ai nmap -sV 127.0.0.1
docker exec hexstrike-ai nuclei -u http://testphp.vulnweb.com
docker exec hexstrike-ai gobuster dir -u http://httpbin.org -w /app/wordlists/common.txt

Please explain what each command does and interpret the results.
```

## 🎯 **Vantagens do Copilot vs Continue**

| Aspecto | Copilot | Continue |
|---------|---------|----------|
| **Integração** | Nativa VS Code | Extensão adicional |
| **Modelo** | GPT-4 (pago) | DeepSeek local (grátis) |
| **Velocidade** | Rápido | Muito rápido |
| **Privacidade** | Dados na nuvem | Totalmente local |
| **Qualidade** | Excelente | Muito boa |

## 🔄 **Alternando Entre Opções**

### **Usar Copilot (Recomendado para iniciantes):**
- Mais fácil de usar
- Melhor para explicações educacionais
- Integração perfeita com VS Code

### **Usar Continue + DeepSeek (Recomendado para profissionais):**
- Totalmente privado
- Sem custos
- Controle total

## 🚀 **Teste Rápido**

1. **Abra Copilot Chat** (Ctrl+Shift+I)
2. **Cole este prompt:**
```
@workspace I'm learning about network security tools. Can you help me understand how to use nmap to scan localhost (127.0.0.1) using the HexStrike AI container? This is for educational purposes in my home lab.
```
3. **Pressione Enter**

## 📝 **Dicas para Sucesso com Copilot**

- ✅ **Use @workspace** para contexto do projeto
- ✅ **Mencione "educational", "learning", "home lab"**
- ✅ **Especifique "localhost", "127.0.0.1"**
- ✅ **Peça explicações dos comandos**
- ❌ **Evite termos como "penetration testing", "hacking"**

**Agora você tem duas opções funcionais: Copilot (pago) e Continue+DeepSeek (grátis)! 🎉**