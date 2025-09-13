# Contributing to HexStrike AI Enhanced

## 🙏 **Acknowledgment**

This project is an enhanced version of the original [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) by 0x4m4. We greatly appreciate the foundation provided by the original project.

## 🎯 **Enhancement Focus**

Our enhancements focus on:
- **Local AI Integration** (LM Studio + DeepSeek V3)
- **VS Code Integration** (Continue extension)
- **Improved Documentation** (PT-BR + EN)
- **Bug Fixes** (nmap NSE scripts, etc.)
- **User Experience** (easier setup, better workflows)

## 🤝 **How to Contribute**

### **1. Types of Contributions**
- 🐛 Bug fixes and improvements
- 📚 Documentation enhancements
- 🔧 New security tool integrations
- 🤖 AI prompt optimizations
- 🌍 Translations

### **2. Development Setup**
```bash
# Fork the repository
git clone https://github.com/yourusername/hexstrike-ai-enhanced.git
cd hexstrike-ai-enhanced

# Build and test
docker build -t hexstrike-ai:v2 .
docker run -d --name hexstrike-ai -p 8888:8888 hexstrike-ai:v2

# Test all tools
docker exec hexstrike-ai nmap -sV 127.0.0.1
docker exec hexstrike-ai nuclei -version
```

### **3. Pull Request Process**
1. Create feature branch (`git checkout -b feature/amazing-feature`)
2. Test your changes thoroughly
3. Update documentation if needed
4. Commit with clear messages
5. Push and create Pull Request

### **4. Code Standards**
- **Docker:** Follow Alpine Linux best practices
- **Python:** PEP 8 compliance for MCP code
- **Documentation:** Clear, concise, bilingual when possible
- **Security:** Always test with authorized targets only

## 📋 **Contribution Guidelines**

### **Security Tools**
- Only add legitimate security tools
- Ensure proper error handling
- Test integration with AI prompts
- Update documentation

### **AI Integration**
- Test prompts with LM Studio + DeepSeek V3
- Ensure Continue extension compatibility
- Provide example workflows
- Document expected behavior

### **Documentation**
- Keep both PT-BR and EN versions
- Include practical examples
- Test all commands before documenting
- Use clear, beginner-friendly language

## 🔐 **Ethical Guidelines**

- **Educational Purpose:** All contributions must support ethical security education
- **Authorized Testing:** Only promote testing on owned/authorized systems
- **Responsible Disclosure:** Support responsible vulnerability disclosure
- **Legal Compliance:** Ensure all tools comply with applicable laws

## 📞 **Getting Help**

- 📖 Check existing documentation first
- 🐛 Search existing issues
- 💬 Use GitHub Discussions for questions
- 📧 Contact maintainers for sensitive issues

## 🏆 **Recognition**

Contributors will be recognized in:
- README.md acknowledgments
- Release notes
- Project documentation

**Thank you for helping make cybersecurity education more accessible! 🚀**