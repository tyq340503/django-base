from django.http import HttpResponse
 
from models import Test

def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>data add success！</p>")
