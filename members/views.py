from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm


# Create your views here.
def homeMembers(request):
    memberModel = Member.objects.all()
    return render(request, "show_delete_exos/members/homeMembers.html", { "memberModel": memberModel })

def homeMen(request):
    allMen = Member.objects.all().filter(gender="male")
    return render(request, "show_delete_exos/members/men.html", { "allMen": allMen })

def homeWomen(request):
    allWomen = Member.objects.all().filter(gender="female")
    return render(request, "show_delete_exos/members/women.html", { "allWomen": allWomen })


def createMember(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homeMembers")
    else:
        form = MemberForm()
    return render(request, "show_delete_exos/members/createMember.html", { "form": form })


def destroy(request, id):
    destroy = Member(id)
    destroy.delete()
    return redirect("homeMembers")
