'''
All the questions for the DiagnosticsQuestionnaire's model's forms
'''

from django import forms

def get_organisation_questions():
    _1 = (
        (1, 'No standard processes are followed or documented'),
        (2, 'Only key / core business processes are standardised, documented and followed by the organisation'),
        (3, 'Most business processes are standardised, documented and followed by the organisation'),
        (4, 'All business processes are standardised, documented and followed by the organisation')
    )
    _2 = (
        (1, 'No targets are set'),
        (2, 'Yes, but only at an organisational level'),
        (3, 'Yes, at both organisational and team levels'),
        (4, 'Yes, at organisational, team and individual levels')
    )
    _3 = (
        (1, 'No - not at all'),
        (2, 'There are some links'),
        (3, 'They are largely linked, but some gaps'),
        (4, 'All elements are completely linked')
    )
    _4 = (
        (1, 'No - none of the targets are SMART'),
        (2, 'Some of the targets are SMART, but there are areas which aren\'t'),
        (3, 'Most of the targets are SMART'),
        (4, 'All the targets are SMART')
    )
    _5 = (
        (1, 'No systems in place'),
        (2, 'Yes, but it is an undocumented basic paper-based approach, done by a handful of employees (not everyone who needs to use it)'),
        (3, 'Yes, it is a well-documented paper-based approach, understood by a large number of the people in the organisation who need to use it'),
        (4, 'Yes, an IT-based approach is in place, understood by everyone who needs to use it in the organisation')
    )
    _6 = (
        (1, 'No written vision exists'),
        (2, 'Yes, but can only be verbalised amongst the senior leadership'),
        (3, 'Yes, can be verbalised amongst entire leadership and management group'),
        (4, 'Yes, the entire organisation can verbalise the organisation\'s vision')
    )
    _7 = (
        (1, 'Very change resistant / No examples of change found'),
        (2, 'Rare occurrences of change given, but almost always met with resistance by the organisation'),
        (3, 'Some change efforts undertaken, with mixed success'),
        (4, 'Clear evidence of successful change initiatives having taken place, with good approaches taken to reduce any resistance')
    )
    _8 = (
        (1, '<25%'),
        (2, '25-50%'),
        (3, '50-75%'),
        (4, '>75%')
    )
    _9 = (
        (1, 'Never'),
        (2, 'Annually'),
        (3, 'Quarterly'),
        (4, 'Monthly')
    )
    _10 = (
        (1, 'No clear linkage between staff and highly beauraucratic structure'),
        (2, 'Some linkages, but disjointed groups and lack of clarity around hierarchy impacting effectiveness '),
        (3, 'Clear structure but not ideal match for strategy and therefore not optimised for performance '),
        (4, 'Clear structure which makes sense in theory and practice when considering delivery on the strategy ')
    )
    _11 = (
        (1, 'No written mission or limited expression of the organisation’s reason for existence; lacks clarity or specificity; either held by very few in organisation or rarely referred to'),
        (2, 'There is some expression of organisation’s reason for existence that reflects its values and purpose, but may lack clarity; held by only a few; lacks broad agreement or rarely referred to'),
        (3, 'There is a clear expression of organisation’s reason for existence which reflects its values and purpose; held by many within organisation and often referred to'),
        (4, 'There is a clear expression of organisation’s reason for existence which is of continued relevance that reflects its values and purpose; broadly held within organisation and frequently referred to')
    )
    _12 = (
        (1, '<25% targets met'),
        (2, '<50% targets met'),
        (3, '<75% targets met'),
        (4, '>75% targets met')
    )
    _13 = (
        (1, 'Organisation runs operations purely on day-to-day basis with no short- or longer-term planning activities; no experience in operational planning'),
        (2, 'Some ability and tendency to develop high-level operational plan either internally or via external assistance; operational plan loosely or not linked to strategic planning activities and used roughly to guide operations'),
        (3, 'Ability and tendency to develop and refine concrete, realistic operational plan; some internal expertise in operational planning or access to relevant external assistance; operational planning carried out on a near regular basis; operational plan linked to strategic planning activities and used to guide operations'),
        (4, 'Organisation develops and refines concrete, realistic, and detailed operational plan; has critical mass of internal expertise in operational planning, or efficiently uses external, sustainable, highly qualified resources; operational planning exercise carried out regularly; operational plan tightly linked to strategic planning activities and systematically used to direct operations')
    )
    _14 = (
        (1, 'No written aims or limited expression of the organisation’s reason for existence; lacks clarity or specificity; either held by very few in organisation or rarely referred to  '),
        (2, 'Some expression of organisation’s reason for existence that reflects its values and purpose, but may lack clarity; held by only a few; lacks broad agreement or rarely referred to     '),
        (3, 'Clear expression of organisation’s reason for existence which reflects its values and purpose; held by many within organisation and often referred to'),
        (4, 'Clear expression of organisation’s reason for existence which is of continued relevance that reflects its values and purpose; broadly held within organisation and frequently referred to')
    )
    _15 = (
        (1, 'Strategy is either nonexistent, unclear, or incoherent (a set of scattered initiatives); strategy has no influence over day-today behaviour'),
        (2, 'Strategy exists but is either not clearly linked to mission, vision, and overarching goals, or lacks coherence, or is not easily actionable; strategy is not broadly known and has limited influence over day-to-day behaviour'),
        (3, 'Coherent strategy has been developed and is linked to mission and vision but is not fully ready to be acted upon; strategy is mostly known at all levels of the organisation and day-to-day behaviour is partly driven by it'),
        (4, 'Organisation has clear, coherent medium- to long-term strategy that is both actionable and linked to overall mission, vision, and overarching aims / goals; strategy is broadly known and consistently helps drive day to- day behaviour at all levels of organisation')
    )

    return _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15

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

def get_finance_questions():
    _1 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _2 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _3 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _4 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _5 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _6 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _7 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _8 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _9 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _10 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _11 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _12 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _13 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _14 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )
    _15 = (
        (1, ''),
        (2, ''),
        (3, ''),
        (4, '')
    )