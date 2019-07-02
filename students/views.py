from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from students.forms import LoginForm, Register
from students.models import Person,Course,RegisteredCourses


def index(request):
    """View function for home page of site."""
    selectedCourse = RegisteredCourses.objects.filter(registered_student=1).filter(registered_course=1).count()
    print(selectedCourse)
    num_courses = Course.objects.all()


    context = {
        'num_courses': num_courses,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def RegisterView(request):
    if request.method == 'POST':
        form = Register(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            oldPerson = Person.objects.filter(email=email).exists()

            if not oldPerson:
                instance = form.save(commit=False)
                password = form.cleaned_data.get('password')
                confirmPassword = form.cleaned_data.get('Confirm_Password')

                if check_password(confirmPassword, password):
                    instance.save()
                    return HttpResponse('done')
            else:
                return HttpResponseRedirect('students/register/')
        else:
            return HttpResponseRedirect('students/register/')
    else:
        form = Register()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            realPerson = Person.objects.get(email__exact=email)
            if realPerson:
                if realPerson.password == password:
                    request.session['user_id'] = realPerson.id
                    if realPerson.AreYouStudent==1:
                        request.session['userRole'] = realPerson.AreYouStudent
                        return HttpResponse('im a student')
                    else:
                        return HttpResponse('im a teacher')

            else:
                form = LoginForm()
                context = {
                    'form': form
                }
    else:
        form = LoginForm()
        context = {
            'form': form
        }

    return render(request,'login.html',context)



def patientLogout(request):
    if request.session['userRole']:
        if 'user_id' in request.session:
            request.session.pop('user_id')
            print('Session Deleted')
            return HttpResponseRedirect('/students/')
    else:
        return HttpResponseRedirect('/students/')
