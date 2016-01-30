from wyszukiwarka.forms import komentarzForm
from wyszukiwarka.models import Komentarze


def handleComments(request):
    if request.method == 'POST':
        type = request.POST.get('submit')
        nowy = komentarzForm(request.POST)
        if nowy.is_valid():
            nowy = nowy.save(commit = False)
            nowy.Rate = request.POST.get('rate')
            nowy.User = request.user
            nowy.site = request.path
            nowy.save()
    rate = 0
    komentarze = list(Komentarze.objects.filter(site = request.path))
    for r in komentarze:
        rate+=r.Rate
    if len(komentarze)>0:
        rate = float(rate)/len(komentarze)
    else:
        rate=0
    intRate = int(rate)
    edge=rate-intRate
    if edge<0.25:
        edge='s'
    elif edge>0.75:
        edge='g'
    else:
        edge='h'
    return {'komentarze': komentarze, 'form': komentarzForm(), 'rating':rate, 'grange':range(0,intRate), 'srange':range(intRate, 4), 'edgeStar':edge}