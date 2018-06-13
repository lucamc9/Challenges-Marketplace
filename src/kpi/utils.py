import pandas as pd
from diagnostics.models import Diagnostics

def get_graph_elements_gn(kpis):
    years = []
    gross_values = []
    net_values = []
    for kpi in kpis:
        years.append(kpi.get_year())
        gross_values.append(kpi.get_gross())
        net_values.append(kpi.get_net())
    return years, gross_values, net_values

def get_graph_elements_flow(kpis):
    revenues = []
    expenditures = []
    cash_flow = []
    flow_labels = []
    for kpi in kpis:
        revenues.append(kpi.get_revenues())
        expenditures.append(kpi.get_expenditures())
        cash_flow.append(kpi.get_cash_flow())
        flow_labels.append(kpi.get_flow_month())
    return revenues, expenditures, cash_flow, flow_labels

def get_month_choices():
    choices = (('January','January'),
               ('February', 'February'),
               ('March', 'March'),
               ('April', 'April'),
               ('May', 'May'),
               ('June', 'June'),
               ('July', 'July'),
               ('August', 'August'),
               ('September', 'September'),
               ('October', 'October'),
               ('November', 'November'),
               ('December', 'December'))
    return choices

def extract_excel_data(template):
    # excel = pd.ExcelFile(template)
    # input_sheet = excel.parse(excel.sheet_names[3])
    gross = 10
    net = 10
    year = 2018
    revenues = 10
    expenditures = 10
    cash_flow = 10
    flow_month = 'April'
    return gross, net, year, revenues, expenditures, cash_flow, flow_month

def get_diagnostics_scores(user):
    first_diag = Diagnostics.objects.filter(user=user).last()
    current_diag = Diagnostics.objects.filter(user=user)[0]
    diag_scores_improv = current_diag.get_all_percents()
    diag_scores = first_diag.get_all_percents()

    return diag_scores[:-1], diag_scores_improv[:-1]

# Graph data for the follower dashboard
def get_follower_yearly_data(yearly_excel, data):
    ''' Only returning latest year for now for non-graph elements,
    new functionality could be to have dropdown button with past 3 years
    as choices to display data
    '''
    # Sales, net_income & cash
    data['sales'] = yearly_excel[yearly_excel['Unnamed: 2'] == 'Total Sales'].iloc[0]['FY 2017']
    data['net_income'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Net Income'].iloc[0]['FY 2017']
    data['cash'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cash & Equivalents'].iloc[0]['FY 2017']
    # Sales concentration
    sales_names = []
    sales_concentration = []
    for i in range(3, 9):
        sales_names.append(yearly_excel['Unnamed: 2'].iloc[i])
        sales_concentration.append(yearly_excel['FY 2017'].iloc[i])
        if yearly_excel['Unnamed: 2'].iloc[i] == 'All Other Customers':
            break
    data['sales_names'] = sales_names
    data['sales_concentration'] = sales_concentration
    # Gross profit margin
    gross = []
    gross_margin = yearly_excel[yearly_excel['Unnamed: 2'] == 'Profit Margin %']
    gross.append(gross_margin.iloc[0]['FY 2015'])
    gross.append(gross_margin.iloc[0]['FY 2016'])
    gross.append(gross_margin.iloc[0]['FY 2017'])
    data['gross'] = gross
    # Net profit margins
    net = []
    net_margin = yearly_excel[yearly_excel['Unnamed: 2'] == 'Net Profit Margin %']
    net.append(net_margin.iloc[0]['FY 2015'])
    net.append(net_margin.iloc[0]['FY 2016'])
    net.append(net_margin.iloc[0]['FY 2017'])
    data['net'] = net
    # Cash in Bank
    cash_bank = []
    cashes_bank = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cash & Equivalents']
    cash_bank.append(cashes_bank.iloc[0]['FY 2015'])
    cash_bank.append(cashes_bank.iloc[0]['FY 2016'])
    cash_bank.append(cashes_bank.iloc[0]['FY 2017'])
    data['cash_bank'] = cash_bank
    # Accounts Receivable
    accounts_receivable = []
    receivables = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Receivable']
    accounts_receivable.append(receivables.iloc[0]['FY 2015'])
    accounts_receivable.append(receivables.iloc[0]['FY 2016'])
    accounts_receivable.append(receivables.iloc[0]['FY 2017'])
    data['accounts_receivable'] = accounts_receivable
    # Accounts Payable
    accounts_payable = []
    payable = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Payable']
    accounts_payable.append(payable.iloc[0]['FY 2015'])
    accounts_payable.append(payable.iloc[0]['FY 2016'])
    accounts_payable.append(payable.iloc[0]['FY 2017'])
    data['accounts_payable'] = accounts_payable
    # Quick Ratio
    current_liabilities = yearly_excel[yearly_excel['Unnamed: 1'] == 'Current Liabilities'].iloc[0]['FY 2017']
    data['quick_ratio'] = (cash_bank[-1] + accounts_receivable[-1]) / current_liabilities
    # Current Ratio
    current_assets = yearly_excel[yearly_excel['Unnamed: 1'] == 'TOTAL CURRENT ASSETS'].iloc[0]['FY 2017']
    data['current_ratio'] = current_assets / current_liabilities

    return data

def get_follower_monthly_data(monthly_excel, data):
    # Sales actual vs forecast
    data['actual_sales'] = monthly_excel[monthly_excel[2] == 'Total Sales'].iloc[0][5]
    data['forecast_sales'] = monthly_excel[monthly_excel[1] == '$ Sales projections for 6 M out'].iloc[0][5]
    # Cash flow graph
    data['cash_flow'] = monthly_excel[monthly_excel[1] == 'Net Income'].iloc[0][5]
    data['revenue'] = data['actual_sales']
    data['expenses'] = data['revenue'] - data['cash_flow']
    # Expenses pie
    data['cost_goods'] = monthly_excel[monthly_excel[1] == 'Cost of Goods Sold'].iloc[0][5]
    data['payroll_costs'] = monthly_excel[monthly_excel[1] == 'Payroll Costs'].iloc[0][5]
    data['rent'] = monthly_excel[monthly_excel[1] == 'Rent/ Leases'].iloc[0][5]
    data['general'] = monthly_excel[monthly_excel[1] == 'Sales, General & Administrative'].iloc[0][5]
    other_1 = monthly_excel[monthly_excel[1] == 'Other & Miscellaneous'].iloc[0][5]
    other_2 = monthly_excel[monthly_excel[1] == 'Other #2 ______________'].iloc[0][5]
    data['other'] = other_1 + other_2
    data['interest'] = monthly_excel[monthly_excel[1] == 'Interest Expense'].iloc[0][5]
    data['taxes'] = monthly_excel[monthly_excel[1] == 'Taxes'].iloc[0][5]
    return data

def get_follower_graph_data(yearly_excel, monthly_excel):
    data = {}
    data = get_follower_yearly_data(yearly_excel, data)
    data = get_follower_monthly_data(monthly_excel, data)
    return data

# Graph data for the business dashboard
def get_business_yearly_data(yearly_excel, data):
    return data

def get_business_monthly_data(monthly_excel, data):
    return data

def get_business_graph_data(yearly_excel, monthly_data):
    data = {}
    data = get_business_yearly_data(yearly_excel, data)
    data = get_business_monthly_data(monthly_excel, data)
    return data
