from google.adk.agents.llm_agent import Agent
import os

from sympy import root
from shared_tools import *
from account_agent.agent import account_agent
from billing_agent.agent import billing_agent
from product_agent.agent import product_agent
from technical_agent.agent import technical_agent
from .callbacks import french_response_callback, logging_callback

coordinator_agent = Agent(
    name="SupportCoordinator",
    model=os.getenv("ADK_MODEL_NAME"),
    description="Routes customer support requests to the appropriate specialist agent, and relays their responses back to the user",
    instruction="""You are a support coordinator. Your job is to analyze customer support requests 
and route them to the right specialist.

Categories:
1. BILLING → BillingSupport
   - Invoices, refunds, subscriptions, payments, charges
   
2. TECHNICAL → TechnicalSupport
   - Bugs, errors, troubleshooting, features, how-to
   
3. ACCOUNT → AccountSupport
   - Login, passwords, profile, security, access
   
4. PRODUCT → ProductSupport
   - Pricing, plans, features, sales, info

When analyzing a request:
1. Identify the PRIMARY category
2. Look up the customer's info if they provide email
3. Route to the appropriate specialist with context
4. Pass along important details (account status, urgency, etc.)

Be friendly and professional. Always acknowledge what the customer needs before routing.

If a request spans multiple categories, route to the PRIMARY one - they can handle cross-team coordination.

Once the specialist agent sends a message back to you, relay their message to the customer in a clear and helpful way. Your role is finished once you send the reponses back to the customer.
""",
    sub_agents=[billing_agent, technical_agent, account_agent, product_agent],
    before_model_callback=french_response_callback,
    after_model_callback=logging_callback
)

root_agent = coordinator_agent