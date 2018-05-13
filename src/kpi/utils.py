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
