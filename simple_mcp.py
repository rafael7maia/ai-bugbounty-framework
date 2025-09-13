#!/usr/bin/env python3
"""
Simple MCP for HexStrike AI - 100% Functional
Uses Docker container directly
"""

import json
import subprocess
import sys
from datetime import datetime

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

def nmap_scan(target):
    """Nmap scan via container"""
    return execute_in_container(f"nmap -sV {target}")

def nuclei_scan(target):
    """Nuclei vulnerability scan"""
    return execute_in_container(f"nuclei -u {target} -severity critical,high,medium")

def subfinder_enum(domain):
    """Subdomain enumeration"""
    return execute_in_container(f"subfinder -d {domain} -silent")

def gobuster_scan(target):
    """Directory enumeration"""
    return execute_in_container(f"gobuster dir -u {target} -w /app/wordlists/common.txt -q")

def httpx_probe(target):
    """HTTP probing"""
    return execute_in_container(f"echo {target} | httpx -title -tech-detect")

def sqlmap_scan(url, options="--dbs"):
    """SQLMap injection testing"""
    return execute_in_container(f"sqlmap -u '{url}' {options} --batch --risk=1 --level=1")

def auto_scan(target):
    """Comprehensive automated scan"""
    results = {
        "target": target,
        "timestamp": datetime.now().isoformat(),
        "scans": {}
    }
    
    print(f"Starting comprehensive scan on {target}")
    
    # Subdomain enumeration
    print("Running subfinder...")
    results["scans"]["subfinder"] = subfinder_enum(target)
    
    # Port scanning
    print("Running nmap...")
    results["scans"]["nmap"] = nmap_scan(target)
    
    # Vulnerability scanning
    print("Running nuclei...")
    results["scans"]["nuclei"] = nuclei_scan(f"http://{target}")
    
    # Directory enumeration
    print("Running gobuster...")
    results["scans"]["gobuster"] = gobuster_scan(f"http://{target}")
    
    return results

def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: python simple_mcp.py <command> [target]",
            "available_commands": [
                "nmap_scan", "nuclei_scan", "subfinder_enum", 
                "gobuster_scan", "httpx_probe", "sqlmap_scan", "auto_scan"
            ]
        }))
        return
    
    command = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not target:
        print(json.dumps({"error": "Target is required"}))
        return
    
    # Execute command
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
        # Para sqlmap, target deve ser uma URL completa
        options = sys.argv[3] if len(sys.argv) > 3 else "--dbs"
        result = sqlmap_scan(target, options)
    elif command == "auto_scan":
        result = auto_scan(target)
    else:
        result = {"error": f"Unknown command: {command}"}
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()