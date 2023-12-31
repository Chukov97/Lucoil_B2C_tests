from models.login_model import LoginData

VALID_CARD = LoginData(
    card_number='5902 2024 228',
    password='Licard2020!'
)

INVALID_CARD = LoginData(
    card_number='59022024220',
    password='LicArd2020!'
)
