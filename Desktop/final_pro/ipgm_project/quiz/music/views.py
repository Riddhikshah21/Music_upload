from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MusicForm
from music.models import Music
from . import forms
from django.views import generic
from .models import Music
from accounts.models import User
from django.contrib.auth.models import User


# Create your views here.
class MusicHome(generic.TemplateView):
    template_name = 'music/music_home.html'


'''class MusicView(LoginRequiredMixin, generic.CreateView):
    template_name = 'music/music_detail.html'


    def get(self, request):
        form = MusicForm()
        return render(request, self.template_name,{'form': form})

    def post(self, request):
        form = MusicForm(request.POST)
        if form.is_valid():
            record = form.save()
            record.user = request.user.username
            record.save()
            text = form.cleaned_data['music_name','music_genre','music_logo','file']
            form = MusicForm()
            return redirect('music:music_home')

            args = {'form':form,'text':text}
            return render(request, self.template_name,args)

def MusicView(request):

    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = forms.MusicForm(data=request.POST)
        # print(form)
        if form.is_valid():
            record =form.save(commit=False)
            record.user = request.user.username

            record.instance.file = request.FILES['file']
            print("hello")

            record.instance.music_logo = request.FILES['music_logo']
            record.save()
            form = forms.MusicForm()
            #return redirect('post_home')
    else:
        form = forms.MusicForm()
    variable = {'form': form }
    return render(request,'music/music_detail.html',variable)'''

def MusicView(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('music:musicdetaillist')
    else:
        form = MusicForm()
    return render(request, 'music/music_detail.html', {
        'form': form
    })

class MusicDetailList(generic.TemplateView):
    template_name = 'music/nav.html'

    def get(self,request):
        music = Music.objects.all().order_by('-added_date')
        user = User.objects.all()
        args = {'music': music, 'user': user}
        return render(request,self.template_name,args)

def MusicArtistList(request, pk):
    artist = Music.objects.get(user_id = pk).order_by('-added_date')
    context = {'artist':artist}
    return render(request,'music/music_artist.html',context)

def ArtistDetail(request, pk):
    artist = Music.objects.get(pk=pk)
    context = {'artist':artist}
    return render(request,'music/artist_detail.html',context)
