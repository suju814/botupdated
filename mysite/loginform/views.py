from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import requests
import requests

def home(request):
	count =User.objects.count()
	return render(request,'home.html',{
		'count':count
		})

def trade(request):
	count =User.objects.count()
	return render(request,'trade.html',{
		'count':count
		})
	
def index(request):
    trd = {}
    trd["crpto_data"] = get_cryto_data()
    return render(request, "index.html", trd)




# return the data received from api as json object
def get_cryto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        trd = requests.get(api_url).json()
    except Exception as e:
        print(e)
        trd = dict()

    return trd
"""
def index(request):
    dat = {}
    dat["cryp_data"] = get_cryto_data()
    return render(request,'index.html',dat)




# return the data received from api as json object
def get_cryto_data():
  while True:

      r = requests.get("https://api.bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=buy")

      dat = r.json()
      

      return dat["result"]
      
      
      time.sleep(5)

"""

def main(request):


	return render(request,'main.html')

def homes(request):

	return render(request,'homes.html')

def logo(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request,'logo.html',data)


def get_crypto_data():
    url = 'https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_ETH'
    parameters ={
        'id':'1'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'PE7QD910-N2TDEPAP-LZILGG72-E3ICHKJW',
        }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

"""
def signup(request):
	if request.method =='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'registration/signup.html',{
		'form':form
		})
"""
