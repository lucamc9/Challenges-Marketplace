import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import (ComplianceModel, EnvironmentalModel, FinanceModel, LegalModel, CompanyModel,
                     GovernanceModel, FacilitiesModel, TechnologyModel, ProcessesModel, ProcurementModel,
                     OrganisationModel, StaffModel, CompetitionModel, MarketingModel)

def get_dataroom_questions(area):
    path_to_db = static('dataroom_db/Dataroom_db.csv')
    dataroom_db = pd.read_csv('/home/lemac/Workspace/ChallenWide/Marketplace/src/static/dataroom_db/Dataroom_db.csv')

    if area == 'Technology':
        area = 'IT/Technology'
    elif area == 'Company':
        area = 'General Company Info'

    return dataroom_db[dataroom_db['Sub-Area'] == area]

def save_dataroom_models(files, user, question, sub_area):

    if sub_area == 'Compliance':
        for file in files:
            model = ComplianceModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Environmental':
        for file in files:
            model = EnvironmentalModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Finance':
        for file in files:
            model = FinanceModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Legal':
        for file in files:
            model = LegalModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Company':
        for file in files:
            model = CompanyModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Governance':
        for file in files:
            model = GovernanceModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Facilities':
        for file in files:
            model = FacilitiesModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Technology':
        for file in files:
            model = TechnologyModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Processes':
        for file in files:
            model = ProcessesModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Organisation':
        for file in files:
            model = OrganisationModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Staff':
        for file in files:
            model = StaffModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Competition':
        for file in files:
            model = CompetitionModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Marketing':
        for file in files:
            model = MarketingModel(user=user, file=file, label=question)
            model.save()
    if sub_area == 'Procurement':
        for file in files:
            model = ProcurementModel(user=user, file=file, label=question)
            model.save()