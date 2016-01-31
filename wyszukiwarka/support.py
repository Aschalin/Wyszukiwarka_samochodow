from wyszukiwarka.forms import komentarzForm
from wyszukiwarka.models import Komentarze, Samochody, Nadwozia, Silniki_Nadwozia


def handleComments(request):
    c = {}
    if request.method == 'POST':
        type = request.POST.get('submit')
        nowy = komentarzForm(request.POST)
        if nowy.is_valid():
            nowy = nowy.save(commit = False)
            nowy.Rate = request.POST.get('rate')
            nowy.User = request.user
            nowy.site = handlePath(request.path)
            nowy.save()
    komentarze = Komentarze.objects.filter(site = handlePath(request.path)).order_by('Time')
    for k in komentarze:
        k.Time = k.Time.strftime("%y-%m-%d %H:%M:%S")
    c['komentarze'] = komentarze
    c['form'] = komentarzForm()
    return c


def handlePath(path):
    return path.split('/', 3)[3]


def handleRating(path):
    c={}
    rate = getRating(path)
    intRate = int(rate)
    edge=rate-intRate
    if edge<0.25:
        edge='s'
    elif edge>0.75:
        edge='g'
    else:
        edge='h'
    c['rating'] = rate
    c['grange'] = range(0,intRate)
    c['srange'] = range(intRate, 4)
    c['edgeStar'] = edge
    return c


def getRating(path):
    rate = 0
    komentarze = list(Komentarze.objects.filter(site = path))
    if len(komentarze)>0:
        for r in komentarze:
            rate+=r.Rate
        rate = float(rate)/len(komentarze)
    return rate


def getSite(path):
    path=path.split('/')
    if len(path) == 1:
        site = Samochody.objects.get(id = path[0])
    elif len(path) == 2:
        site = Nadwozia.objects.get(id = path[1])
    elif len(path) == 3:
        site = Silniki_Nadwozia.objects.filter(Nadwozie_id = path[1]).filter(Silnik_id = path[2])[0]
    return site
