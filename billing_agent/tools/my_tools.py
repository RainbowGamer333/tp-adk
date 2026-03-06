import random
from datetime import datetime


async def lookup_invoice(customer_email: str, invoice_id: str = None) -> list:
    """Lookup invoices for a customer.
    
    Args:
        customer_email: Customer email
        invoice_id: Optional specific invoice ID
        
    Returns:
        List of invoices with dates, amounts, and statuses
    """
    # Mock invoices
    all_invoices = {
        "john@example.com": [
            {
                "invoice_id": "INV_2024_001",
                "date": "2024-03-01",
                "amount": 99.99,
                "status": "paid",
                "items": ["Professional Plan - 1 month"],
                "due_date": "2024-03-05",
                "payment_method": "Credit card ending in 4242"
            },
            {
                "invoice_id": "INV_2024_002",
                "date": "2024-02-01",
                "amount": 99.99,
                "status": "paid",
                "items": ["Professional Plan - 1 month"],
                "due_date": "2024-02-05"
            }
        ],
        "jane@example.com": [
            {
                "invoice_id": "INV_2024_003",
                "date": "2024-03-01",
                "amount": 29.99,
                "status": "paid",
                "items": ["Starter Plan - 1 month"],
                "due_date": "2024-03-05"
            }
        ]
    }
    
    invoices = all_invoices.get(customer_email, [])
    if invoice_id:
        invoices = [i for i in invoices if i["invoice_id"] == invoice_id]
    return invoices


async def process_refund(
    invoice_id: str,
    amount: float = None,
    reason: str = "Customer request"
) -> dict:
    """Process a refund for an invoice.
    
    Args:
        invoice_id: Invoice to refund
        amount: Amount to refund (full if not specified)
        reason: Reason for refund
        
    Returns:
        Refund confirmation with ID and processing details
    """
    return {
        "refund_id": f"REF_{random.randint(100000, 999999)}",
        "invoice_id": invoice_id,
        "status": "processing",
        "amount": amount or 99.99,
        "reason": reason,
        "estimated_arrival": "3-5 business days",
        "original_payment_method": "Credit card",
        "initiated_at": datetime.now().isoformat()
    }


async def modify_subscription(
    customer_email: str,
    action: str,  # upgrade | downgrade | cancel | pause
    new_plan: str = None
) -> dict:
    """Modify a customer's subscription.
    
    Args:
        customer_email: Customer email
        action: upgrade | downgrade | cancel | pause
        new_plan: New plan name (for upgrade/downgrade)
        
    Returns:
        Subscription change confirmation
    """
    return {
        "subscription_id": f"sub_{random.randint(10000, 99999)}",
        "customer_email": customer_email,
        "action": action,
        "status": "updated",
        "effective_date": "2024-03-10",
        "new_plan": new_plan,
        "changes": {
            "old_plan": "Professional" if action in ["downgrade", "cancel"] else "Starter",
            "new_plan": new_plan if action in ["upgrade", "downgrade"] else "None",
            "prorated_amount": 15.50 if action == "downgrade" else 0
        }
    }
