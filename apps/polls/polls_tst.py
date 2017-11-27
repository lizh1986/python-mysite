#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .models import Question
from django.utils import timezone

arr = Question.objects.all()
print(arr)

q = Question(question_text='What is new?', pub_date=timezone.now())
q.save()
print(q)

q.question_text = 'What is up?'
q.save()

arr = Question.objects.all()
print(arr)


arr = Question.objects.filter(id=1)
arr = Question.objects.filter(question_text__startswith='what')
