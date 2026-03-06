async def get_pricing_info(plan_type: str = None) -> dict:
    """Get current pricing and plan information.
    
    Args:
        plan_type: Specific plan (starter | professional | enterprise)
        
    Returns:
        All plans with features, pricing, and billing info
    """
    plans = {
        "starter": {
            "name": "Starter",
            "price": 29.99,
            "billing_cycle": "monthly",
            "users": "Up to 100",
            "storage": "1GB",
            "features": [
                "Basic analytics",
                "Email support",
                "Community access"
            ],
            "popular": False
        },
        "professional": {
            "name": "Professional",
            "price": 99.99,
            "billing_cycle": "monthly",
            "users": "Up to 1000",
            "storage": "100GB",
            "features": [
                "Advanced analytics",
                "Priority support",
                "API access",
                "Custom branding"
            ],
            "popular": True
        },
        "enterprise": {
            "name": "Enterprise",
            "price": "Custom",
            "billing_cycle": "annual",
            "users": "Unlimited",
            "storage": "Unlimited",
            "features": [
                "Everything in Professional",
                "Dedicated support",
                "SLA guarantee",
                "Custom integrations",
                "On-premise option"
            ],
            "popular": False
        }
    }
    
    if plan_type:
        return plans.get(plan_type.lower(), {"error": "Plan not found"})
    return {"plans": list(plans.values())}


async def check_feature_availability(
    feature_name: str,
    plan_type: str = None
) -> dict:
    """Check if a feature is available on a plan.
    
    Args:
        feature_name: Feature to check (e.g., "API access", "SSO")
        plan_type: Specific plan to check
        
    Returns:
        Feature availability across plans
    """
    feature_matrix = {
        "api_access": {
            "starter": False,
            "professional": True,
            "enterprise": True,
            "coming_to": "Starter plan (Q3 2024)"
        },
        "sso": {
            "starter": False,
            "professional": False,
            "enterprise": True,
            "coming_to": "Professional plan (Q2 2024)"
        },
        "priority_support": {
            "starter": False,
            "professional": True,
            "enterprise": True,
            "coming_to": None
        }
    }
    
    key = feature_name.lower().replace(" ", "_")
    feature_info = feature_matrix.get(key, {
        "starter": False,
        "professional": False,
        "enterprise": True
    })
    
    return {
        "feature": feature_name,
        "available_on": [plan.title() for plan, available in feature_info.items() if available is True],
        "not_available_on": [plan.title() for plan, available in feature_info.items() if available is False],
        "coming_soon": feature_info.get("coming_to")
    }
