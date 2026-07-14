# Auction Fees (Copart Standard Buyer Fees for 2026)
# Maps the maximum bid limit to the corresponding auction fee
COPART_FEES = [
    (50, 3.00),
    (100, 45.00),
    (200, 80.00),
    (300, 125.00),
    (400, 170.00),
    (500, 205.00),
    (600, 230.00),
    (700, 265.00),
    (800, 290.00),
    (900, 315.00),
    (1000, 340.00),
    (1200, 385.00),
    (1300, 415.00),
    (1400, 430.00),
    (1500, 445.00),
    (1600, 460.00),
    (1700, 475.00),
    (1800, 490.00),
    (1900, 505.00),
    (2000, 520.00),
    (2400, 550.00),
    (2900, 600.00),
    (3400, 675.00),
    (3900, 725.00),
    (4400, 775.00),
    (4900, 825.00),
    (5400, 850.00),
    (5900, 875.00),
    (6900, 925.00),
    (7900, 975.00),
    (9900, 1050.00),
    (14900, 1150.00),
    (19900, 1250.00),
    (24900, 1350.00),
    (29900, 1450.00),
    (34900, 1550.00),
    (1000000, 1750.00) # For bids higher than $35k, average fee is around $1750
]

# Additional fixed auction gate and internet fees
AUCTION_GATE_FEE = 79.00
AUCTION_INTERNET_FEE = 119.00

# Logistics Rates (Average estimates for US east coast to European ports)
US_DOMESTIC_SHIPPING = 450.00  # Land transport from auction yard to US port
SEA_FREIGHT = 1450.00          # Container shipping by sea to Europe
EUROPE_TO_UA_SHIPPING = 850.00 # Transport from European port to Ukraine customs
PORT_CHARGES = 350.00          # Local European port handling fees

# Customs Agent and Brokerage Fees in Ukraine
BROKER_FEE = 400.00            # Customs broker services
EXPEDITER_FEE = 300.00         # Port expediting services

# Currency conversion (simplified for calculation)
EUR_TO_USD = 1.09