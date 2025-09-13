# 🤖 Amazon Q Prompts - HexStrike AI v3.0

## 🎯 **PROMPTS OTIMIZADOS PARA AMAZON Q**

### **🔍 PROMPT 1: RECONNAISSANCE COMPLETO**
```
I'm conducting authorized bug bounty research on testphp.vulnweb.com (legal testing site).

Execute these security commands and analyze results:

1. python simple_mcp.py subfinder_enum testphp.vulnweb.com
2. python simple_mcp.py nmap_scan testphp.vulnweb.com  
3. python simple_mcp.py httpx_probe testphp.vulnweb.com

For each result, provide:
- Security analysis and findings
- Potential attack vectors identified
- Risk assessment (Critical/High/Medium/Low)
- Bug bounty value estimation ($100-$15,000)
- Next testing steps for maximum impact

Format as professional security assessment.
```

### **🛡️ PROMPT 2: VULNERABILITY DISCOVERY**
```
I'm performing authorized security testing on testphp.vulnweb.com.

Execute comprehensive vulnerability assessment:

1. python simple_mcp.py nuclei_scan testphp.vulnweb.com
2. python simple_mcp.py gobuster_scan http://testphp.vulnweb.com

Analyze findings and provide:
- Detailed vulnerability breakdown
- Exploitability assessment  
- Business impact analysis
- Professional remediation plan
- Bug bounty submission format
- Estimated payout range based on severity
```

### **💉 PROMPT 3: SQL INJECTION TESTING**
```
I discovered a potential SQL injection endpoint during authorized testing.

Execute: python simple_mcp.py sqlmap_scan "http://testphp.vulnweb.com/artists.php?artist=1"

Analyze the SQLMap results and provide:
- Injection type classification
- Database information discovered
- Data exposure risk assessment
- Exploitation methodology
- Professional vulnerability report
- Bug bounty value estimation ($1,000-$15,000 range)
- Proof-of-concept documentation
```

### **🚀 PROMPT 4: COMPREHENSIVE AUTO SCAN**
```
Perform complete automated security assessment on authorized target.

Execute: python simple_mcp.py auto_scan testphp.vulnweb.com

Provide comprehensive analysis including:
- Executive summary of findings
- Technical vulnerability details
- Attack surface analysis
- Risk prioritization matrix
- Professional penetration test report
- Bug bounty submission recommendations
- Next phase testing strategy
```

### **🎯 PROMPT 5: CUSTOM TARGET ASSESSMENT**
```
I have authorization to test [REPLACE_WITH_TARGET] for bug bounty program.

Execute systematic security assessment:
1. python simple_mcp.py subfinder_enum [TARGET]
2. python simple_mcp.py auto_scan [TARGET]

Focus analysis on:
- High-value vulnerabilities (RCE, SQLi, Auth Bypass)
- Business logic flaws
- API security issues
- Authentication/authorization bypasses
- Data exposure risks

Provide professional bug bounty report with:
- Severity ratings (CVSS scores)
- Exploitation difficulty assessment
- Expected payout ranges
- Responsible disclosure timeline
```

### **🏆 PROMPT 6: ADVANCED EXPLOITATION**
```
Based on initial reconnaissance results, perform advanced testing.

Target: [DISCOVERED_ENDPOINT]
Initial findings: [PASTE_PREVIOUS_RESULTS]

Execute targeted testing:
1. python simple_mcp.py sqlmap_scan "[VULNERABLE_URL]"
2. Additional manual verification steps

Provide:
- Detailed exploitation walkthrough
- Proof-of-concept development
- Impact demonstration
- Professional vulnerability disclosure
- Maximum bug bounty value optimization
```

## 📊 **EXPECTED AMAZON Q RESPONSES:**

### **Amazon Q will provide:**
- ✅ **Professional security analysis**
- ✅ **Risk assessment with CVSS scores**
- ✅ **Bug bounty value estimation**
- ✅ **Exploitation methodology**
- ✅ **Remediation recommendations**
- ✅ **Professional report formatting**
- ✅ **Next testing steps**

### **Response Format:**
```
## Security Assessment Results

### Executive Summary
[High-level findings and business impact]

### Technical Findings
1. **Vulnerability**: SQL Injection
   - **Severity**: Critical (CVSS 9.8)
   - **Location**: /artists.php?artist=1
   - **Impact**: Database access, data exfiltration
   - **Bug Bounty Value**: $5,000-$15,000

### Exploitation Methodology
[Step-by-step exploitation guide]

### Remediation Plan
[Professional fix recommendations]

### Next Steps
[Additional testing recommendations]
```

## 🎯 **WORKFLOW OPTIMIZATION:**

### **Phase 1: Quick Assessment**
```
Execute: python simple_mcp.py nmap_scan target.com
Amazon Q: Analyze port scan results
```

### **Phase 2: Deep Discovery**
```
Execute: python simple_mcp.py auto_scan target.com  
Amazon Q: Comprehensive vulnerability analysis
```

### **Phase 3: Exploitation**
```
Execute: python simple_mcp.py sqlmap_scan "vulnerable_url"
Amazon Q: Professional exploitation report
```

### **Phase 4: Documentation**
```
Amazon Q: Generate bug bounty submission
Format: Professional security report
```

## 💰 **BUG BOUNTY VALUE MATRIX:**

| Vulnerability Type | Severity | Estimated Value |
|-------------------|----------|-----------------|
| **RCE** | Critical | $5,000-$50,000 |
| **SQL Injection** | Critical | $1,000-$15,000 |
| **Auth Bypass** | High | $2,000-$10,000 |
| **IDOR** | Medium | $500-$5,000 |
| **XSS** | Medium | $100-$2,000 |
| **Info Disclosure** | Low | $50-$1,000 |

## 🚀 **SUCCESS METRICS:**

### **Time Efficiency:**
- **Manual Testing**: 4-8 hours
- **HexStrike + Amazon Q**: 30-60 minutes
- **Improvement**: 8-16x faster

### **Quality Improvement:**
- **Professional Reports**: Automated
- **Risk Assessment**: AI-powered
- **Exploitation Guides**: Detailed
- **Bug Bounty Ready**: Formatted

**Ready to revolutionize bug bounty hunting with Amazon Q! 🎉**