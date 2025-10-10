from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.conf import settings
import pandas as pd


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def UserViewData(request):
    path = settings.MEDIA_ROOT + "\\" + "dataset.csv"
    df = pd.read_csv(path, nrows=100)
    df = df.to_html(index=False)
    return render(request, 'users/UserViewDataset.html', {'data': df})


def PreprocessedData(request):
    path = settings.MEDIA_ROOT + "\\" + "dataset.csv"
    df = pd.read_csv(path, nrows=100)
    df['Genre'].replace({'Female': 0, 'Male': 1}, inplace=True)
    df['TypeEtab'].replace({'Public': 0, 'Private': 1}, inplace=True)
    df['Niveau'].replace({'Primary': 1, 'Secondary': 2, 'Tertiary': 3}, inplace=True)
    df['RetardSco'].replace({'1 year': 1, '2 years': 2, 'None': 0}, inplace=True)
    df['Provenance'].replace({'Rural': 1, 'Suburban': 2, 'Urban': 3}, inplace=True)
    df['Handicap'].replace({'Yes': 1, 'No': 0}, inplace=True)
    df['SocialAid'].replace({'Yes': 1, 'No': 0}, inplace=True)
    df['Result'].replace({'Pass': 0, 'Fail': 1}, inplace=True)
    df = df.to_html(index=False)
    return render(request, 'users/UserViewDataset.html', {'data': df})


def MLResults(request):
    from .algorithms import ImplementAlgorithmsCodes
    knn = ImplementAlgorithmsCodes.knnResults()
    rf = ImplementAlgorithmsCodes.randomForest()
    svm = ImplementAlgorithmsCodes.svmAlgorithm()
    sgd = ImplementAlgorithmsCodes.sgdAlgorithm()
    return render(request, 'users/mlresultst.html', {'knn': knn, 'rf': rf, 'svm': svm, 'sgd': sgd})


def heatMapDraw(request):
    from .algorithms import ImplementAlgorithmsCodes
    ImplementAlgorithmsCodes.corrGraph()
    return render(request, 'users/corrGraph.html', {})

