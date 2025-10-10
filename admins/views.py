from django.shortcuts import render, HttpResponse
from django.contrib import messages
from users.models import UserRegistrationModel



def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def ViewRegisteredUsers(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/RegisteredUsers.html', {'data': data})


def AdminActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/RegisteredUsers.html', {'data': data})


def DeleteUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).delete()
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/RegisteredUsers.html', {'data': data})


def adminMLResults(request):
    from users.algorithms import ImplementAlgorithmsCodes
    knn = ImplementAlgorithmsCodes.knnResults()
    rf = ImplementAlgorithmsCodes.randomForest()
    svm = ImplementAlgorithmsCodes.svmAlgorithm()
    sgd = ImplementAlgorithmsCodes.sgdAlgorithm()
    return render(request, 'admins/mlresultst.html', {'knn': knn, 'rf': rf, 'svm': svm, 'sgd': sgd})
