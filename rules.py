# rules.py

class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    WHITE = 4

def latest_financial_index(data: dict):
    for index, financial in enumerate(data.get("financials")):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0

def total_revenue(data: dict, financial_index):
    return data["financials"][financial_index]["pnl"]["lineItems"]["net_revenue"]

def total_borrowing(data: dict, financial_index):
    liabilities = data["financials"][financial_index]["bs"]["liabilities"]
    return liabilities["long_term_borrowings"] + liabilities["short_term_borrowings"]

def total_revenue_5cr_flag(data: dict, financial_index):
    total_rev = total_revenue(data, financial_index)
    return FLAGS.GREEN if total_rev >= 50000000 else FLAGS.RED

def iscr(data: dict, financial_index):
    pnl = data["financials"][financial_index]["pnl"]["lineItems"]
    ebitda = pnl["profit_before_tax"] + pnl["depreciation"]
    interest = pnl.get("interest", 1)  # Ensure no division by 0
    return ebitda / (interest + 1)

def iscr_flag(data: dict, financial_index):
    iscr_value = iscr(data, financial_index)
    return FLAGS.GREEN if iscr_value >= 2 else FLAGS.RED

def borrowing_to_revenue_flag(data: dict, financial_index):
    borrowings = total_borrowing(data, financial_index)
    revenue = total_revenue(data, financial_index)
    ratio = borrowings / revenue
    return FLAGS.GREEN if ratio <= 0.25 else FLAGS.AMBER
