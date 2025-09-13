#!/usr/bin/env python3
"""
Security Bridge for AI Bug Bounty Framework
MITRE ATT&CK integrated security testing bridge
"""

import json
import subprocess
import sys
from datetime import datetime

# MITRE ATT&CK Mapping for Bug Bounty
MITRE_MAPPING = {
    "nmap_scan": {
        "technique": "T1046",
        "name": "Network Service Scanning", 
        "tactic": "Discovery",
        "description": "Adversaries may attempt to get a listing of services running on remote hosts"
    },
    "nuclei_scan": {
        "technique": "T1190",
        "name": "Exploit Public-Facing Application",
        "tactic": "Initial Access", 
        "description": "Adversaries may attempt to take advantage of a weakness in an Internet-facing computer"
    },
    "subfinder_enum": {
        "technique": "T1590.005",
        "name": "Gather Victim Network Information: IP Addresses",
        "tactic": "Reconnaissance",
        "description": "Adversaries may gather the victim's IP addresses that can be used during targeting"
    },
    "gobuster_scan": {
        "technique": "T1083",
        "name": "File and Directory Discovery", 
        "tactic": "Discovery",
        "description": "Adversaries may enumerate files and directories or may search in specific locations"
    },
    "sqlmap_scan": {
        "technique": "T1190",
        "name": "Exploit Public-Facing Application",
        "tactic": "Initial Access",
        "description": "SQL injection attacks against web applications"
    },
    "httpx_probe": {
        "technique": "T1595.002", 
        "name": "Active Scanning: Vulnerability Scanning",
        "tactic": "Reconnaissance",
        "description": "Adversaries may scan victims for vulnerabilities that can be used during targeting"
    }
}

def execute_in_container(command):
    """Execute command in HexStrike AI container"""
    try:
        full_command = f"docker exec hexstrike-ai {command}"
        result = subprocess.run(
            full_command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "timestamp": datetime.now().isoformat()
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Command timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def add_mitre_context(command, result):
    """Add MITRE ATT&CK context to results"""
    if command in MITRE_MAPPING:
        result["mitre_attack"] = MITRE_MAPPING[command]
    return result

def nmap_scan(target):
    """Network Service Scanning (T1046)"""
    result = execute_in_container(f"nmap -sV -sC {target}")
    return add_mitre_context("nmap_scan", result)

def nuclei_scan(target):
    """Exploit Public-Facing Application (T1190)"""
    result = execute_in_container(f"nuclei -u {target} -severity critical,high,medium")
    return add_mitre_context("nuclei_scan", result)

def subfinder_enum(domain):
    """Gather Victim Network Information (T1590.005)"""
    result = execute_in_container(f"subfinder -d {domain} -silent")
    return add_mitre_context("subfinder_enum", result)

def gobuster_scan(target):
    """File and Directory Discovery (T1083)"""
    result = execute_in_container(f"gobuster dir -u {target} -w /app/wordlists/common.txt -q")
    return add_mitre_context("gobuster_scan", result)

def httpx_probe(target):
    """Active Scanning: Vulnerability Scanning (T1595.002)"""
    result = execute_in_container(f"echo {target} | httpx -title -tech-detect")
    return add_mitre_context("httpx_probe", result)

def sqlmap_scan(url, options="--dbs"):
    """SQL Injection Testing (T1190)"""
    result = execute_in_container(f"sqlmap -u '{url}' {options} --batch --risk=1 --level=1")
    return add_mitre_context("sqlmap_scan", result)

def mitre_attack_chain(target):
    """Complete MITRE ATT&CK chain simulation"""
    results = {
        "target": target,
        "timestamp": datetime.now().isoformat(),
        "mitre_attack_chain": {
            "reconnaissance": {},
            "initial_access": {},
            "discovery": {}
        }
    }
    
    print(f"🎯 MITRE ATT&CK Chain Analysis: {target}")
    
    # Reconnaissance Phase
    print("📡 Phase 1: Reconnaissance (T1590, T1595)")
    results["mitre_attack_chain"]["reconnaissance"]["subfinder"] = subfinder_enum(target)
    results["mitre_attack_chain"]["reconnaissance"]["httpx"] = httpx_probe(target)
    
    # Discovery Phase  
    print("🔍 Phase 2: Discovery (T1046, T1083)")
    results["mitre_attack_chain"]["discovery"]["nmap"] = nmap_scan(target)
    results["mitre_attack_chain"]["discovery"]["gobuster"] = gobuster_scan(f"http://{target}")
    
    # Initial Access Phase
    print("🚪 Phase 3: Initial Access (T1190)")
    results["mitre_attack_chain"]["initial_access"]["nuclei"] = nuclei_scan(f"http://{target}")
    
    return results

def auto_scan(target):
    """Legacy comprehensive scan (maintained for compatibility)"""
    return mitre_attack_chain(target)

def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: python security_bridge.py <command> [target]",
            "available_commands": [
                "nmap_scan", "nuclei_scan", "subfinder_enum", 
                "gobuster_scan", "httpx_probe", "sqlmap_scan", 
                "mitre_attack_chain", "auto_scan"
            ],
            "mitre_integration": "All commands mapped to MITRE ATT&CK techniques"
        }))
        return
    
    command = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not target:
        print(json.dumps({"error": "Target is required"}))
        return
    
    # Execute command with MITRE context
    if command == "nmap_scan":
        result = nmap_scan(target)
    elif command == "nuclei_scan":
        result = nuclei_scan(target)
    elif command == "subfinder_enum":
        result = subfinder_enum(target)
    elif command == "gobuster_scan":
        result = gobuster_scan(target)
    elif command == "httpx_probe":
        result = httpx_probe(target)
    elif command == "sqlmap_scan":
        options = sys.argv[3] if len(sys.argv) > 3 else "--dbs"
        result = sqlmap_scan(target, options)
    elif command == "mitre_attack_chain":
        result = mitre_attack_chain(target)
    elif command == "auto_scan":
        result = auto_scan(target)
    else:
        result = {"error": f"Unknown command: {command}"}
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()