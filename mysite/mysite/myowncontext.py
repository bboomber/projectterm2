from insurance.models import Insure
from datetime import date

def add_variable_to_context(request):
    insureNum = Insure.objects.filter(confirm="2").count()
    today = date.today()
    return {
        'testme': 'Hello world!',
        'insureNum': insureNum,
        'today': today,
        'tomonth': today.month
    }