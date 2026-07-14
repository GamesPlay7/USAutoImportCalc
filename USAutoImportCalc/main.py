import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, FloatPrompt

# Import our custom calculator
from calculator import ImportCalculator

console = Console()

def print_header():
    """Prints a stylish application header."""
    console.print("\n[bold magenta]🇺🇸 US AUTO IMPORT & REPAIR CALCULATOR 🇺🇸[/bold magenta]")
    console.print("[dim]Estimate bidding, shipping, customs clearance, and repair costs under Ukrainian law[/dim]\n")

def get_car_input() -> ImportCalculator:
    """Collects and validates all necessary vehicle details from the user."""
    console.print("[bold cyan]📋 Enter Vehicle Specifications:[/bold cyan]")
    
    # 1. Auction Bid
    bid = FloatPrompt.ask("➔ Auction winning bid ($)", default=12000.0)
    
    # 2. Engine Volume
    engine_volume = IntPrompt.ask("➔ Engine volume in cc (e.g., 2300 for 2.3L, 5000 for 5.0L)", default=2300)
    
    # 3. Fuel Type
    engine_type = Prompt.ask(
        "➔ Fuel/Engine type", 
        choices=["gasoline", "diesel"], 
        default="gasoline"
    )
    
    # 4. Vehicle Age
    age = IntPrompt.ask("➔ Vehicle age (years since manufacture year)", default=2)
    
    # 5. Repair Budget
    repair_cost = FloatPrompt.ask("➔ Estimated repair and parts budget ($)", default=4000.0)
    
    return ImportCalculator(
        bid=bid,
        engine_volume=engine_volume,
        engine_type=engine_type,
        age=age,
        repair_cost=repair_cost
    )

def display_financial_report(report: dict):
    """Renders a gorgeous financial breakdown table using rich."""
    table = Table(
        title="\n[bold green]💰 DETAILED FINANCIAL BREAKDOWN (USD)[/bold green]", 
        show_header=True, 
        header_style="bold magenta",
        box=None
    )
    
    table.add_column("Expense Category", style="cyan")
    table.add_column("Detailed Item", style="dim white")
    table.add_column("Cost ($)", style="bold yellow", justify="right")

    # Group 1: Auction
    table.add_row("Auction Costs", "Winning Bid", f"${report['car_value']:,.2f}")
    table.add_row("", "Copart Fees & Gates", f"${report['auction_fee']:,.2f}")
    
    # Group 2: Shipping
    table.add_row("Logistics & Transport", "Land, Ocean & Port Freight", f"${report['logistics_total']:,.2f}")
    
    # Group 3: Customs
    table.add_row("Customs Taxes", "Import Duty (10%)", f"${report['duty']:,.2f}")
    table.add_row("", "Excise Tax", f"${report['excise']:,.2f}")
    table.add_row("", "VAT (20%)", f"${report['vat']:,.2f}")
    table.add_row("", "[bold]Total Customs Clearance[/bold]", f"[bold]${report['customs_total']:,.2f}[/bold]")
    
    # Group 4: Local Registration & Prep
    table.add_row("Registration & Prep", "Pension Fund Registration Fee", f"${report['pension_fund']:,.2f}")
    table.add_row("", "Certification & State Plates", f"${report['cert_and_reg']:,.2f}")
    
    # Group 5: Repairs
    table.add_row("Restoration", "Estimated Repair & Parts", f"${report['repair_cost']:,.2f}")
    
    table.add_section()
    
    # Grand Total
    table.add_row(
        "[bold green]GRAND TOTAL[/bold green]", 
        "[bold green]Estimated Ready-to-Drive Cost[/bold green]", 
        f"[bold green]${report['total_cost']:,.2f}[/bold green]"
    )
    
    console.print(table)

def run_analysis(total_cost: float):
    """Performs market price comparison and estimates investment profitability."""
    console.print("\n[bold cyan]📊 Market Price Comparison:[/bold cyan]")
    market_price = FloatPrompt.ask("➔ Average market price for this ready model in Ukraine ($)")
    
    savings = market_price - total_cost
    
    console.print("\n" + "─" * 50)
    if savings > 0:
        percent_saved = (savings / market_price) * 100
        console.print(Panel(
            f"[bold green]🎉 SUCCESS: Importing this car is highly profitable![/bold green]\n\n"
            f"• Total Saved: [bold]${savings:,.2f}[/bold]\n"
            f"• You save approximately [bold]{percent_saved:.1f}%[/bold] compared to buying locally.",
            border_style="green"
        ))
    else:
        loss = abs(savings)
        console.print(Panel(
            f"[bold red]⚠️ WARNING: Importing this car might not be financially viable.[/bold red]\n\n"
            f"• It is estimated to cost [bold]${loss:,.2f}[/bold] MORE than the local market price.\n"
            f"• Consider finding a cheaper lot or lowering the repair budget.",
            border_style="red"
        ))

def main():
    print_header()
    
    while True:
        calc = get_car_input()
        report = calc.get_full_report()
        
        display_financial_report(report)
        run_analysis(report['total_cost'])
        
        repeat = Prompt.ask("\nCalculate another vehicle?", choices=["y", "n"], default="y")
        if repeat == "n":
            console.print("\n[bold magenta]🚗 Drive safe! Session closed.[/bold magenta]\n")
            break
        console.print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()