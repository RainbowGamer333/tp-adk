import random
from datetime import datetime


async def lookup_customer(email: str) -> dict:
    """Lookup customer account information by email.
    
    Args:
        email: Customer's email address
        
    Returns:
        Customer account info including ID, name, plan, status
    """
    # Mock data for testing
    mock_customers = {
        "john@example.com": {
            "account_id": "cust_001",
            "name": "John Doe",
            "email": "john@example.com",
            "status": "active",
            "plan_type": "professional",
            "created_date": "2023-01-15",
            "support_tickets_open": 1
        },
        "jane@example.com": {
            "account_id": "cust_002",
            "name": "Jane Smith",
            "email": "jane@example.com",
            "status": "active",
            "plan_type": "starter",
            "created_date": "2023-06-20",
            "support_tickets_open": 0
        }
    }
    return mock_customers.get(email, {
        "error": f"No account found for {email}",
        "suggestion": "Please verify the email address"
    })


async def search_knowledge_base(query: str, category: str = None) -> list:
    """Search the company knowledge base for relevant articles.
    
    Args:
        query: Search query (e.g., "password reset", "billing")
        category: Optional filter (BILLING, TECHNICAL, ACCOUNT, PRODUCT)
        
    Returns:
        List of relevant KB articles with titles, URLs, and excerpts
    """
    # Mock knowledge base
    kb_articles = [
        {
            "title": "How to Reset Your Password",
            "url": "https://docs.company.com/reset-password",
            "excerpt": "Click 'Forgot Password' on the login page. Check your email for the reset link.",
            "category": "ACCOUNT",
            "relevance": 0.95 if "password" in query.lower() else 0.2
        },
        {
            "title": "Understanding Your Invoice",
            "url": "https://docs.company.com/invoices",
            "excerpt": "Your invoice shows charges for your active subscription plan.",
            "category": "BILLING",
            "relevance": 0.95 if "invoice" in query.lower() else 0.3
        },
        {
            "title": "API Reference Guide",
            "url": "https://docs.company.com/api",
            "excerpt": "Complete API documentation with code examples in Python, JavaScript, and REST.",
            "category": "TECHNICAL",
            "relevance": 0.95 if "api" in query.lower() else 0.2
        },
        {
            "title": "Upgrading Your Plan",
            "url": "https://docs.company.com/upgrade",
            "excerpt": "Compare plans and upgrade to get more features and storage.",
            "category": "PRODUCT",
            "relevance": 0.95 if "plan" in query.lower() or "upgrade" in query.lower() else 0.2
        },
        {
            "title": "Account Security Best Practices",
            "url": "https://docs.company.com/security",
            "excerpt": "Enable two-factor authentication and use strong passwords.",
            "category": "ACCOUNT",
            "relevance": 0.85 if "security" in query.lower() else 0.3
        }
    ]
    
    # Filter by relevance and category
    results = [
        article for article in kb_articles 
        if (category is None or article["category"] == category)
        and article["relevance"] > 0.5
    ]
    
    return sorted(results, key=lambda x: x["relevance"], reverse=True)


async def create_support_ticket(
    customer_email: str,
    category: str,
    subject: str,
    description: str,
    priority: str = "normal"
) -> dict:
    """Create a new support ticket.
    
    Args:
        customer_email: Customer's email
        category: BILLING | TECHNICAL | ACCOUNT | PRODUCT
        subject: Ticket subject line
        description: Detailed description
        priority: low | normal | high | urgent
        
    Returns:
        Ticket confirmation with ID and expected response time
    """
    ticket_id = f"TKT_{random.randint(100000, 999999)}"
    
    # Set response time based on priority
    response_times = {
        "urgent": "15 minutes",
        "high": "1 hour",
        "normal": "2-4 hours",
        "low": "24 hours"
    }
    
    return {
        "ticket_id": ticket_id,
        "status": "open",
        "customer_email": customer_email,
        "category": category,
        "subject": subject,
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "estimated_response_time": response_times.get(priority, "2-4 hours"),
        "assigned_to": None
    }