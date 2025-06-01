import time

def verify_number(phone_number):
    """Finge verificación del número usando Open Gateway."""
    time.sleep(1)  # Simula latencia de red
    return {
        "status": "VERIFIED",
        "number": phone_number,
        "carrier": "Telefónica",
        "country": "ES",
        "line_type": "mobile",
        "verified_via": "SMS"
    }

def verify_identity(full_name):
    """Finge verificación de identidad por nombre completo."""
    time.sleep(1)  # Simula latencia
    return {
        "match": True,
        "full_name": full_name,
        "confidence_score": 0.91,
        "source": "Fake Identity DB"
    }

def verify_number_real(phone_number):
    """Finge verificación real por SMS."""
    time.sleep(1.5)
    return {
        "status": "VERIFIED",
        "number": phone_number,
        "method": "sms_code",
        "timestamp": "2025-05-31T23:59:59Z",
        "session": "fake-session-id"
    }
