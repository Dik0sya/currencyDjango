from django.shortcuts import render

# Create your views here.


def converter(request):
    return render(request, 'converter.html', {})


def home(request):
    import requests
    import json

    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP,LTC,LINK,BCH,DOT,BNB,ADA&tsyms=USD")
    price = json.loads(price_request.content)
    return render(request, 'home.html', {'price': price})


def base(request):
    import requests
    import json

    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,XRP&tsyms=USD")
    price = json.loads(price_request.content)
    return render(request, 'base.html', {'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Enter a crypto symbol"
        return render(request, 'prices.html', {'notfound': notfound})