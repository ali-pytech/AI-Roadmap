"""Iqama Renewal Update"""

iqama = {
    "Ahmed": {"year":2025, "fee":800, "status":"Active"},
    "Faisal": {"year":2024, "fee":700, "status":"Pending"}
}

#updating Faisal's Status:

iqama["Faisal"].update({"status": "Active"})

#Adding New record:

iqama["Ali"] = {"year":2026, "fee":900, "status":"Active"}

print(iqama)
