from datetime import datetime
import random

async def report_bug(
    title: str,
    description: str,
    severity: str = "normal",
    error_log: str = None,
    customer_email: str = None
) -> dict:
    """Report a potential bug to engineering.
    
    Args:
        title: Bug title
        description: Detailed description
        severity: low | normal | high | critical
        error_log: Stack trace or error logs
        customer_email: Customer reporting the issue
        
    Returns:
        Bug report confirmation with tracking ID
    """
    return {
        "bug_id": f"BUG_{random.randint(100000, 999999)}",
        "status": "triaged",
        "title": title,
        "description": description,
        "severity": severity,
        "reported_by": customer_email or "support_team",
        "assigned_engineer": "Engineering Team",
        "estimated_fix_time": {
            "critical": "4 hours",
            "high": "1 day",
            "normal": "3 days",
            "low": "1 week"
        }.get(severity, "3 days"),
        "created_at": datetime.now().isoformat()
    }


async def search_api_docs(query: str) -> list:
    """Search API documentation.
    
    Args:
        query: Search term (e.g., "authentication", "rate limits")
        
    Returns:
        List of relevant API docs with code examples
    """
    api_docs = [
        {
            "title": "Authentication",
            "topic": "Auth",
            "content": "All requests must include an Authorization header with a valid API key.",
            "code_example": 'curl -H "Authorization: Bearer YOUR_API_KEY" https://api.company.com/v1/...',
            "url": "https://api.company.com/docs/auth"
        },
        {
            "title": "Rate Limiting",
            "topic": "Limits",
            "content": "API requests are rate limited to 10,000 requests per minute.",
            "code_example": "# Check X-RateLimit-* headers in response",
            "url": "https://api.company.com/docs/rate-limits"
        },
        {
            "title": "Error Handling",
            "topic": "Errors",
            "content": "Errors are returned with appropriate HTTP status codes and error messages.",
            "code_example": '{"error": "Not found", "code": 404}',
            "url": "https://api.company.com/docs/errors"
        }
    ]
    
    results = [doc for doc in api_docs if query.lower() in doc["content"].lower() or query.lower() in doc["title"].lower()]
    return results


async def run_diagnostic(customer_email: str, test_type: str = "all") -> dict:
    """Run diagnostics on customer's setup.
    
    Args:
        customer_email: Customer to diagnose
        test_type: connection | performance | configuration | all
        
    Returns:
        Diagnostic results and recommendations
    """
    return {
        "test_type": test_type,
        "customer_email": customer_email,
        "status": "completed",
        "results": {
            "connection": "✓ OK",
            "latency": "45ms",
            "api_version": "v3.2.1",
            "authentication": "✓ Valid",
            "rate_limit": "450/1000 used",
            "issues_found": []
        },
        "recommendations": [
            "All systems operational",
            "No configuration issues detected"
        ],
        "timestamp": datetime.now().isoformat()
    }
