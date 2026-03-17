# Run with: docker compose exec app python test_paystack.py

from app.services.payment_service import initialize_payment, verify_payment

print("--- Testing initialize_payment ---")
result = initialize_payment(
    email="test@example.com",
    amount_naira=1000.00,
    order_id=999,
)
print("Status  :", result["status"])
print("Pay URL :", result.get("authorization_url", "N/A"))
print("Ref     :", result.get("reference", "N/A"))

if result["status"]:
    print()
    print("--- Testing verify_payment ---")
    verify_result = verify_payment(result["reference"])
    print("Status  :", verify_result["status"])
    print("Paid    :", verify_result["paid"])
    print("Message :", verify_result["message"])