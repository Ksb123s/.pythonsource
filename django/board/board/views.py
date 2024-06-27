from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Question,Answer
from .froms import QuestionFrom, AnswerFrom

from django.core.paginator import Paginator

# Create your views here.

def question_create(request):
    if request.method == "POST":
        form = QuestionFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:question_list")
        
    else:
        form = QuestionFrom()
    return render(request, "board/question_form.html", {"form": form})

def answer_create(request, qid):
    """답변등록"""

    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerFrom(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:question_detail", qid=qid)

    else:   
        form = AnswerFrom()


    # question = get_object_or_404(Question, id=qid)

    # answer = Answer.objects.create(question=question, content=request.POST.get("content"))

    # question.answer_set.create(content=request.POST.get("content"))

    # answer = Answer(question=question, content=request.POST.get("content"))
    # answer.save()
    
    # get 방식(실패시 처리)
    context = {"question" : question, "form":form}
    return render( request,"board/question_detail.html" ,context)




def question_list(request):
    """전체 질문 추출"""

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page",1)

    # questions = Question.objects.all()
    questions = Question.objects.order_by("-created_at")

    paginator = Paginator(questions, 10)
    page_obj = paginator.get_page(page)
    context = {"question_list": page_obj}
    return render(request, "board/question_list.html", context)

def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {"question": question}
    return render(request, "board/question_detail.html", context)