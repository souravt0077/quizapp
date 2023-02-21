from django.shortcuts import render,redirect
from .models import quizModel
from .form import addQuestionForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        questions=quizModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.ans == request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        context={
            'score':f'{score}/{total}',
            'wrong':wrong,
            'correct':correct,
            'total':total,
            'questions':questions
        }
        return render(request,'result.html',context)
    else:
        questions=quizModel.objects.all()
        context={'questions':questions}
        return render(request,'home.html',context)

def addQuestion(request):
    form=addQuestionForm
    if request.method == 'POST':
        form=addQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Added')
            return redirect('addquestions')
    context={'form':form}
    return render(request,'addquestion.html',context)