from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    txt = request.POST.get('text', 'default')
    txtcount = txt
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@$%#^&*_~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        txt = analyzed

    if uppercase == 'on':
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Converted to Upper case', 'analyzed_text': analyzed}
        txt = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in txt:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        txt = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(txt):
            if txt[index] == " " and txt[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        txt = analyzed

    if charcounter == 'on':
        analyzed = ""
        count = 0
        count1 = 0
        for char in txtcount:
            if char != ' ':
                count += 1
        for char in txt:
            if char != ' ':
                count1 += 1
        analyzed = txt + "\nNumber of characters Your text initially has =" + str(count) + \
                   " \nNumber of characters Your text has after analyzing =" + str(count1)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if removepunc != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on" and \
            charcounter != "on":
        return HttpResponse('Please select atleast one option. TRY AGAIN...!')

    return render(request, 'analyze.html', params)
