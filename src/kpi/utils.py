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
