#This site is created by Shiv Hari Tewari.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #Get the Text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # Check which checkbox is on.
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


def newlineremove(request):
    return HttpResponse("New Line Remover")

def spaceremove(request):
    return HttpResponse("Space Remover")

def capfirst(request):
    return HttpResponse("Capitalize First Letter")

def charcount(request):
    return HttpResponse("Character Counter")

def AboutUs(request):
    sites = ['''<h1><em>Navigation Sites Bar</em></h1>''',
             '''<h1>For Entertainment </h1><a href = "https://www.youtube.com/" >Youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.linkedin.com/in/shivhari-tewari-19702712a/" >LinkedIn</a>''',
             '''<h1>For  Publication  </h1><a href = "https://www.svedbergopen.com/files/1614613601_(5)_IJDSBDA15112020MTN003_(p_63-79).pdf" >International Publication</a>''',
             '''<h1>For Internships and Jobs   </h1><a href="https://internshala.com" >Intenship and Jobs</a>''',
             '''<h1>Naukri </h1><a href="https://www.naukri.com/mnjuser/homepage" >JOBS</a>''',
             '''<h1>Games Online </h1><a href="https://krunker.io/" >Games</a>''',
             '''<h1>Some extra 😈 </h1><a href="https://www.pornktube.tv/" >Adult</a>'''
            ]
    return HttpResponse((sites))