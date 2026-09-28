import sys
import json
from client import BankersAlgorithm

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-deadlock-detector-banker-resource-graph-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "check_safe_state",
                    "description": "Determine if resource allocation state is safe from deadlocks using Banker's algorithm",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "available": {"type": "array", "items": {"type": "integer"}},
                            "max_matrix": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}},
                            "allocation": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
                        },
                        "required": ["available", "max_matrix", "allocation"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "check_safe_state":
            banker = BankersAlgorithm(args.get("available", []), args.get("max_matrix", []), args.get("allocation", []))
            data = banker.is_safe_state()
            res = {"content": [{"type": "text", "text": json.dumps(data)}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
