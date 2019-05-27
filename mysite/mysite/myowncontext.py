from insurance.models import Insure

def add_variable_to_context(request):
    insureNum = Insure.objects.filter(confirm="2").count()
    return {
        'testme': 'Hello world!',
        'insureNum': insureNum,
    }