'''
All the questions for the DiagnosticsQuestionnaire's model's forms
'''

from django import forms
from django.db import models
import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import  static

class Question:

    def __init__(self, name, area, question, a_1, a_2, a_3, a_4):
        self.name = name
        self.area = area
        self.question = question
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.a_4 = a_4

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area

    def get_question(self):
        return self.question

    def get_a1(self):
        return self.a_1

    def get_a2(self):
        return self.a_2

    def get_a3(self):
        return self.a_3

    def get_a4(self):
        return self.a_4

    def get_radio_choices(self):
        choices = (
            (1, self.a_1),
            (2, self.a_2),
            (3, self.a_3),
            (4, self.a_4)
        )
        return choices

    def get_model(self):
        return models.IntegerField(choices=self.get_radio_choices, default=1)

def get_questions_from_db():
    '''

    :return: question dictionary {'sub-area' : questions_list }
    '''
    path_to_db = static('diagnostics_db/Diagnostics_db.csv')
    diagnostics_db = pd.read_csv(path_to_db)
    all_questions = {}
    sub_areas = ['Environmental', 'Social', 'Compliance', 'Finance', 'Legal',
                 'Organisation', 'Staff', 'Competition', 'Marketing', 'Governance',
                 'Management', 'Facilities', 'IT/Technology', 'Processes', 'Procurement']
    for area in sub_areas:
        area_df = diagnostics_db[diagnostics_db['Sub-Area'] == area]
        # Init params
        idx = 0
        questions = []
        for index, row in area_df.iterrows():
            area = area
            name = area + "_" + str(idx)
            question = row['Question']
            a_1 = row['Score = 1']
            a_2 = row['Score = 2']
            a_3 = row['Score = 3']
            a_4 = row['Score = 4']
            qs = Question(name, area, question, a_1, a_2, a_3, a_4)
            questions.append(qs)
            idx += 1
        all_questions[area] = questions
    return all_questions

def get_organisation_form_settings():
    fields = [
        'org_1',
        'org_2',
        'org_3',
        'org_4',
        'org_5',
        'org_6',
        'org_7',
        'org_8',
        'org_9',
        'org_10',
        'org_11',
        'org_12',
        'org_13',
        'org_14',
        'org_15'
    ]
    labels = {
        'org_1': 'Are standard business processes for working created, documented and used by workforce?',
        'org_2': 'Are targets formally set in the organisation?',
        'org_3': 'Are the organisation\'s targets linked to aims, vision and mission statement?',
        'org_4': 'Are the organisation\'s targets SMART (Specific, Measurable, Achievable, Relevant, Timely)?',
        'org_5': 'Are there systems in place for planning / project management?',
        'org_6': 'Does a statement of the organisation\'s vision exist?',
        'org_7': 'How amenable is the organisation to change?',
        'org_8': 'How much has the company grown in the past 5 years?',
        'org_9': 'How often are the organisation\'s targets measured / evaluated to assess performance?',
        'org_10': 'How well is the organisation structure set up to deliver the strategy?',
        'org_11': 'Mission statement exists?',
        'org_12': 'What proportion of last year\'s targets did the organisation meet (both financial and otherwise)?',
        'org_13': 'Which sentence best describes planning within the organisation to meet its set targets / objectives?',
        'org_14': 'Which sentence best describes the organisation\'s long term aims?',
        'org_15': 'Which sentence best describes the organisation\'s strategy?'
    }
    widgets = {
        'org_1': forms.RadioSelect(),
        'org_2': forms.RadioSelect(),
        'org_3': forms.RadioSelect(),
        'org_4': forms.RadioSelect(),
        'org_5': forms.RadioSelect(),
        'org_6': forms.RadioSelect(),
        'org_7': forms.RadioSelect(),
        'org_8': forms.RadioSelect(),
        'org_9': forms.RadioSelect(),
        'org_10': forms.RadioSelect(),
        'org_11': forms.RadioSelect(),
        'org_12': forms.RadioSelect(),
        'org_13': forms.RadioSelect(),
        'org_14': forms.RadioSelect(),
        'org_15': forms.RadioSelect()
    }

    return fields, labels, widgets
