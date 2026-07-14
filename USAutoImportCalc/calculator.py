import rates

class ImportCalculator:
    def __init__(self, bid: float, engine_volume: int, engine_type: str, age: int, repair_cost: float):
        self.bid = bid
        self.engine_volume = engine_volume  # in cc (e.g., 2300)
        self.engine_type = engine_type.lower()  # 'gasoline' or 'diesel'
        self.age = max(1, age)  # Age cannot be 0 for excise formula (minimum is 1 year)
        self.repair_cost = repair_cost

    def calculate_auction_fee(self) -> float:
        """Calculates the progressive Copart auction fee + fixed gate/internet fees."""
        base_fee = 0.0
        for limit, fee in rates.COPART_FEES:
            if self.bid <= limit:
                base_fee = fee
                break
        return base_fee + rates.AUCTION_GATE_FEE + rates.AUCTION_INTERNET_FEE

    def calculate_logistics(self) -> float:
        """Sums up all transportation and handling costs from US to Ukraine."""
        return (
            rates.US_DOMESTIC_SHIPPING
            + rates.SEA_FREIGHT
            + rates.EUROPE_TO_UA_SHIPPING
            + rates.PORT_CHARGES
            + rates.BROKER_FEE
            + rates.EXPEDITER_FEE
        )

    def calculate_customs(self) -> dict:
        """
        Calculates Ukrainian customs clearance taxes:
        1. Import Duty (10% of purchase value)
        2. Excise Tax (Base rate * volume/1000 * age, converted to USD)
        3. VAT (20% of purchase value + duty + excise)
        """
        auction_fee = self.calculate_auction_fee()
        # Customs value is the car purchase price plus the auction fee
        customs_value = self.bid + auction_fee

        # 1. Import Duty (10%)
        duty = customs_value * 0.10

        # 2. Excise Tax Formula (in EUR, then converted to USD)
        # Determine base rate in EUR per 1000cc
        if self.engine_type == "gasoline":
            base_rate_eur = 50.0 if self.engine_volume <= 3000 else 100.0
        else:  # diesel
            base_rate_eur = 75.0 if self.engine_volume <= 3500 else 150.0

        # Max age multiplier in Ukraine customs is limited to 15 years
        age_factor = min(15, self.age)
        
        excise_eur = base_rate_eur * (self.engine_volume / 1000.0) * age_factor
        excise_usd = excise_eur * rates.EUR_TO_USD

        # 3. VAT (20%)
        vat = (customs_value + duty + excise_usd) * 0.20

        total_customs = duty + excise_usd + vat

        return {
            "duty": duty,
            "excise": excise_usd,
            "vat": vat,
            "total_customs": total_customs
        }

    def calculate_pension_fund(self) -> float:
        """
        Calculates the mandatory Pension Fund registration fee in Ukraine.
        Progressive rate based on the customs value of the car.
        """
        customs_value = self.bid + self.calculate_auction_fee()
        
        # Approximate thresholds for 2026 (converted to USD)
        if customs_value <= 13000:
            rate = 0.03
        elif customs_value <= 23000:
            rate = 0.04
        else:
            rate = 0.05
            
        return customs_value * rate

    def get_full_report(self) -> dict:
        """Compiles all calculations into a single detailed report."""
        auction_fee = self.calculate_auction_fee()
        logistics = self.calculate_logistics()
        customs = self.calculate_customs()
        pension_fund = self.calculate_pension_fund()
        
        # Standard registration and certification fees in Ukraine
        certification_and_reg = 350.0  
        
        total_investment = (
            self.bid 
            + auction_fee 
            + logistics 
            + customs["total_customs"] 
            + pension_fund 
            + certification_and_reg 
            + self.repair_cost
        )

        return {
            "car_value": self.bid,
            "auction_fee": auction_fee,
            "logistics_total": logistics,
            "duty": customs["duty"],
            "excise": customs["excise"],
            "vat": customs["vat"],
            "customs_total": customs["total_customs"],
            "pension_fund": pension_fund,
            "cert_and_reg": certification_and_reg,
            "repair_cost": self.repair_cost,
            "total_cost": total_investment
        }