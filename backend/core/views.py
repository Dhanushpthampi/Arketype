from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question,Result
from .serializers import ResultSerializer
from .serializers import QuestionSerializer

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

@api_view(["GET"])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions,many=True)
    return Response(serializer.data)


@api_view(["POST"])
def submit_answers(request):
    answers = request.data.get("answers", [])

    scores = {}

    for item in answers:
        question_id = item.get("question_id")
        value = int(item.get("value", 0))

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            continue

        trait = question.trait
        weight = question.weight

        scores[trait] = scores.get(trait, 0) + value * weight

    result = Result.objects.create(scores=scores)

    serializer = ResultSerializer(result)
    return Response(serializer.data)