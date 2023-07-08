from django.shortcuts import render
from .forms import QuestionForm
import openai

def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            json_data = form.cleaned_data['json_data']
            
            if json_data:
                # Call ChatGPT API to get the answer
                answer = chatgpt_answer(json_data, question)
            else:
                answer = "No JSON data available"
            
            return render(request, 'chatapp/home.html', {'form': form, 'answer': answer})
    else:
        form = QuestionForm()

    return render(request, 'chatapp/home.html', {'form': form})

def chatgpt_answer(json_data, question):
    openai.api_key = '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'

    # Prepare the input for ChatGPT
    input_text = f"JSON Data: {json_data}\nQuestion: {question}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Retrieve the generated answer from ChatGPT
    answer = response.choices[0].text.strip()

    return answer
