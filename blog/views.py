from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category,News
from .forms import ContactFrom

def news_list(request):
    news_list = News.Chopetish.all()
    news_list = News.objects.filter(status=News.status.Chopetish)
    context ={
        "news_list":news_list
    }
    return render(request,"index.html",context={})

def categoryPage(request):
    news_list = News.chopetish.all().order_by('-publish_time')[:6]
    new = News.chopetish.all().order_by('-publish_time')[:3]
    full = News.chopetish.all().order_by('-publish_time')[:2]
    catigories = Category.objects.all().order_by('name')
    locals = News.chopetish.all().filter(category__name="Mahalliy").order_by("-publish_time")[:3]
    xorijiy = News.chopetish.all().filter(category__name="Xorijiy").order_by("-publish_time")[:4]
    xalqaro = News.chopetish.all().filter(category__name="Xalqaro").order_by("-publish_time")[:4]
    sport = News.chopetish.all().filter(category__name="Sport").order_by("-publish_time")[:4]
    biznes = News.chopetish.all().filter(category__name="Biznes").order_by("-publish_time")[:4]
    ilmfan = News.chopetish.all().filter(category__name="Ilm-fan").order_by("-publish_time")[:1]
    texnalogiya = News.chopetish.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:2]
    obunachi = News.chopetish.all().filter(category__name="Obunachilar").order_by("-publish_time")[:5]
    reklama = News.chopetish.all().filter(category__name="Reklamalar").order_by("-publish_time")[:1]

    print("locals ->", locals)
    context = {
        "newss": news_list,
        "news": new,
        "full": full,
        "catigories": catigories,
        "locals": locals,
        "xorijiy": xorijiy,
        "xalqaro": xalqaro,
        "sport": sport,
        "biznes": biznes,
        "ilmfan": ilmfan,
        "texnalogiya": texnalogiya,
        "obunachi": obunachi,
        "reklama": reklama
    }
    return render(request, "category.html", context=context)

def singlenewsPage(request):
    news_list = News.chopetish.all().order_by('-publish_time')[:6]
    new = News.chopetish.all().order_by('-publish_time')[:3]
    full = News.chopetish.all().order_by('-publish_time')[:2]
    catigories = Category.objects.all().order_by('name')
    locals = News.chopetish.all().filter(category__name="Mahalliy").order_by("-publish_time")[:3]
    xorijiy = News.chopetish.all().filter(category__name="Xorijiy").order_by("-publish_time")[:4]
    xalqaro = News.chopetish.all().filter(category__name="Xalqaro").order_by("-publish_time")[:4]
    sport = News.chopetish.all().filter(category__name="Sport").order_by("-publish_time")[:4]
    biznes = News.chopetish.all().filter(category__name="Biznes").order_by("-publish_time")[:4]
    ilmfan = News.chopetish.all().filter(category__name="Ilm-fan").order_by("-publish_time")[:1]
    texnalogiya = News.chopetish.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:2]
    obunachi = News.chopetish.all().filter(category__name="Obunachilar").order_by("-publish_time")[:5]
    reklama = News.chopetish.all().filter(category__name="Reklamalar").order_by("-publish_time")[:1]

    print("locals ->", locals)
    context = {
        "newss": news_list,
        "news": new,
        "full": full,
        "catigories": catigories,
        "locals": locals,
        "xorijiy": xorijiy,
        "xalqaro": xalqaro,
        "sport": sport,
        "biznes": biznes,
        "ilmfan": ilmfan,
        "texnalogiya": texnalogiya,
        "obunachi": obunachi,
        "reklama": reklama
    }
    return render(request, "single.html", context=context)


def news_detali(request,news):
    new = get_object_or_404(News, slug=news, status=News.Status.Chopetish)
    context = {
        "new":new
    }
    return render(request,"single.html",context=context)

def base(request):
    catigories = Category.objects.all()[:5]
    context = {
        "catigories": catigories,
    }
    return render(request, "base.html", context=context)

def contactpage(request):

    news_list = News.chopetish.all().order_by('-publish_time')[:6]
    new = News.chopetish.all().order_by('-publish_time')[:3]
    full = News.chopetish.all().order_by('-publish_time')[:2]
    catigories = Category.objects.all().order_by('name')
    locals = News.chopetish.all().filter(category__name="Mahalliy").order_by("-publish_time")[:3]
    xorijiy = News.chopetish.all().filter(category__name="Xorijiy").order_by("-publish_time")[:4]
    xalqaro = News.chopetish.all().filter(category__name="Xalqaro").order_by("-publish_time")[:4]
    sport = News.chopetish.all().filter(category__name="Sport").order_by("-publish_time")[:4]
    biznes = News.chopetish.all().filter(category__name="Biznes").order_by("-publish_time")[:4]
    ilmfan = News.chopetish.all().filter(category__name="Ilm-fan").order_by("-publish_time")[:1]
    texnalogiya = News.chopetish.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:2]
    obunachi = News.chopetish.all().filter(category__name="Obunachilar").order_by("-publish_time")[:5]
    reklama = News.chopetish.all().filter(category__name="Reklamalar").order_by("-publish_time")[:1]

    form = ContactFrom(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>malumotingiz saqlandi</h2>")
    context = {
        "form":form,
        "newss": news_list,
        "news": new,
        "full": full,
        "catigories": catigories,
        "locals": locals,
        "xorijiy": xorijiy,
        "xalqaro": xalqaro,
        "sport": sport,
        "biznes": biznes,
        "ilmfan": ilmfan,
        "texnalogiya": texnalogiya,
        "obunachi": obunachi,
        "reklama": reklama,
    }
    return render(request, 'contact.html',context=context)

def newspage(request):
    news_list = News.chopetish.all().order_by('-publish_time')[:6]
    new = News.chopetish.all().order_by('-publish_time')[:3]
    full = News.chopetish.all().order_by('-publish_time')[:2]
    catigories = Category.objects.all().order_by('name')
    locals = News.chopetish.all().filter(category__name="Mahalliy").order_by("-publish_time")[:3]
    xorijiy = News.chopetish.all().filter(category__name="Xorijiy").order_by("-publish_time")[:4]
    xalqaro = News.chopetish.all().filter(category__name="Xalqaro").order_by("-publish_time")[:4]
    sport = News.chopetish.all().filter(category__name="Sport").order_by("-publish_time")[:4]
    biznes = News.chopetish.all().filter(category__name="Biznes").order_by("-publish_time")[:4]
    ilmfan = News.chopetish.all().filter(category__name="Ilm-fan").order_by("-publish_time")[:1]
    texnalogiya = News.chopetish.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:2]
    obunachi = News.chopetish.all().filter(category__name="Obunachilar").order_by("-publish_time")[:5]
    reklama = News.chopetish.all().filter(category__name="Reklamalar").order_by("-publish_time")[:1]

    print("locals ->", locals)
    context = {
        "newss":news_list,
        "news": new,
        "full": full,
        "catigories":catigories,
        "locals":locals,
        "xorijiy": xorijiy,
        "xalqaro":xalqaro,
        "sport":sport,
        "biznes":biznes,
        "ilmfan":ilmfan,
        "texnalogiya":texnalogiya,
        "obunachi":obunachi,
        "reklama":reklama
    }
    return render(request, "index.html", context=context)

