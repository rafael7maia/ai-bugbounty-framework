#!/usr/bin/env python3
"""
HexStrike AI MCP Server - Model Context Protocol Implementation
"""
import asyncio
import json
import sys
import subprocess
import argparse
from typing import Any, Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HexStrikeMCP:
    def __init__(self, server_url: str = "http://localhost:8888"):
        self.server_url = server_url
        self.tools = {
            "nmap_scan": self.nmap_scan,
            "nuclei_scan": self.nuclei_scan,
            "gobuster_scan": self.gobuster_scan,
            "subfinder_enum": self.subfinder_enum,
            "httpx_probe": self.httpx_probe,
            "sqlmap_scan": self.sqlmap_scan,
            "masscan_scan": self.masscan_scan,
            "dirsearch_scan": self.dirsearch_scan,
            "wafw00f_detect": self.wafw00f_detect,
            "arjun_params": self.arjun_params
        }

    async def execute_command(self, command: str, timeout: int = 300) -> Dict[str, Any]:
        """Execute security tool command"""
        try:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(
                process.communicate(), 
                timeout=timeout
            )
            
            return {
                "success": True,
                "stdout": stdout.decode('utf-8', errors='ignore'),
                "stderr": stderr.decode('utf-8', errors='ignore'),
                "return_code": process.returncode
            }
        except asyncio.TimeoutError:
            return {"success": False, "error": "Command timeout"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def nmap_scan(self, target: str, scan_type: str = "basic") -> Dict[str, Any]:
        """Nmap network scanning"""
        scan_options = {
            "basic": "-sV -sC",
            "fast": "-T4 -F",
            "comprehensive": "-sS -sV -sC -A -O",
            "stealth": "-sS -T2"
        }
        
        options = scan_options.get(scan_type, "-sV -sC")
        command = f"nmap {options} {target}"
        
        result = await self.execute_command(command)
        return {
            "tool": "nmap",
            "target": target,
            "scan_type": scan_type,
            "result": result
        }

    async def nuclei_scan(self, target: str, severity: str = "medium") -> Dict[str, Any]:
        """Nuclei vulnerability scanning"""
        command = f"nuclei -u {target} -severity {severity} -json"
        
        result = await self.execute_command(command)
        return {
            "tool": "nuclei",
            "target": target,
            "severity": severity,
            "result": result
        }

    async def gobuster_scan(self, target: str, wordlist: str = "/app/wordlists/common.txt") -> Dict[str, Any]:
        """Gobuster directory enumeration"""
        command = f"gobuster dir -u {target} -w {wordlist} -q"
        
        result = await self.execute_command(command)
        return {
            "tool": "gobuster",
            "target": target,
            "wordlist": wordlist,
            "result": result
        }

    async def subfinder_enum(self, domain: str) -> Dict[str, Any]:
        """Subfinder subdomain enumeration"""
        command = f"subfinder -d {domain} -silent"
        
        result = await self.execute_command(command)
        return {
            "tool": "subfinder",
            "domain": domain,
            "result": result
        }

    async def httpx_probe(self, target: str) -> Dict[str, Any]:
        """HTTPx web probing"""
        command = f"echo {target} | httpx -title -tech-detect -status-code"
        
        result = await self.execute_command(command)
        return {
            "tool": "httpx",
            "target": target,
            "result": result
        }

    async def sqlmap_scan(self, url: str, data: str = None) -> Dict[str, Any]:
        """SQLMap SQL injection testing"""
        command = f"sqlmap -u '{url}' --batch --risk=1 --level=1"
        if data:
            command += f" --data='{data}'"
        
        result = await self.execute_command(command)
        return {
            "tool": "sqlmap",
            "url": url,
            "data": data,
            "result": result
        }

    async def masscan_scan(self, target: str, ports: str = "80,443,8080,8443") -> Dict[str, Any]:
        """Masscan fast port scanning"""
        command = f"masscan {target} -p{ports} --rate=1000"
        
        result = await self.execute_command(command)
        return {
            "tool": "masscan",
            "target": target,
            "ports": ports,
            "result": result
        }

    async def dirsearch_scan(self, target: str) -> Dict[str, Any]:
        """Dirsearch web directory scanning"""
        command = f"dirsearch -u {target} -e php,html,js,txt --quiet"
        
        result = await self.execute_command(command)
        return {
            "tool": "dirsearch",
            "target": target,
            "result": result
        }

    async def wafw00f_detect(self, target: str) -> Dict[str, Any]:
        """WAF detection with wafw00f"""
        command = f"wafw00f {target}"
        
        result = await self.execute_command(command)
        return {
            "tool": "wafw00f",
            "target": target,
            "result": result
        }

    async def arjun_params(self, target: str) -> Dict[str, Any]:
        """Parameter discovery with Arjun"""
        command = f"arjun -u {target} --get"
        
        result = await self.execute_command(command)
        return {
            "tool": "arjun",
            "target": target,
            "result": result
        }

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle MCP requests"""
        method = request.get("method")
        params = request.get("params", {})
        
        if method == "tools/list":
            return {
                "tools": [
                    {"name": name, "description": f"Execute {name} security tool"}
                    for name in self.tools.keys()
                ]
            }
        
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            
            if tool_name in self.tools:
                try:
                    result = await self.tools[tool_name](**arguments)
                    return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
                except Exception as e:
                    return {"error": f"Tool execution failed: {str(e)}"}
            else:
                return {"error": f"Unknown tool: {tool_name}"}
        
        return {"error": "Unknown method"}

async def main():
    parser = argparse.ArgumentParser(description="HexStrike AI MCP Server")
    parser.add_argument("--server", default="http://localhost:8888", help="HexStrike server URL")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    mcp = HexStrikeMCP(args.server)
    
    # MCP stdio communication loop
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            request = json.loads(line.strip())
            response = await mcp.handle_request(request)
            
            print(json.dumps(response))
            sys.stdout.flush()
            
        except json.JSONDecodeError:
            continue
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main())