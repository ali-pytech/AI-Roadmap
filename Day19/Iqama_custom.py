
class InvalidFeeError(Exception):
    pass

def create_iqama_record(name, year, fee):
    if fee <= 0:
        raise InvalidFeeError("Fee Must be Greater Than Zero")
    return {"name": name, "year": year, "fee":fee}


try:
    ali_record = create_iqama_record("Ali",2026,800)
    ahmed_record = create_iqama_record("Ahmed",2025, -500)  #invalid
    iqama_record = [ali_record, ahmed_record]
    print(f"Iqama Record: {iqama_record}")


except InvalidFeeError as e:
    print("Error:", e)
