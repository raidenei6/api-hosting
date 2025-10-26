# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from decouple import config
# from openai import OpenAI

# # Load Hugging Face token from .env
# HF_TOKEN = config("HF_TOKEN")

# # Initialize client
# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=HF_TOKEN,
# )

# @api_view(['GET', 'POST'])
# def generate(request):
#     if request.method == 'GET':
#         return Response({"message": "Send a POST request with JSON {'prompt': 'your text'}"})

#     prompt = request.data.get("prompt", "")
#     if not prompt:
#         return Response({"error": "No prompt provided"}, status=400)

#     try:
#         completion = client.chat.completions.create(
#             model="openai/gpt-oss-120b:groq",
#             messages=[{"role": "user", "content": prompt}],
#         )
#         # response_text = completion.choices[0].message.get("content", "")
#         # Fix here
#         response_text = getattr(completion.choices[0].message, "content", "")
#         return Response({"response": response_text})
#     except Exception as e:
#         return Response({"error": str(e)}, status=500)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from decouple import config
from openai import OpenAI

@api_view(['GET', 'POST'])
def generate(request):
    # Load token inside the view
    HF_TOKEN = config("HF_TOKEN", default=None)
    if not HF_TOKEN:
        return Response({"error": "HF_TOKEN not set in .env"}, status=500)

    # Initialize client inside the view
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=HF_TOKEN,
    )

    if request.method == 'GET':
        return Response({"message": "Send a POST request with JSON {'prompt': 'your text'}"})

    prompt = request.data.get("prompt", "")
    if not prompt:
        return Response({"error": "No prompt provided"}, status=400)

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:groq",
            messages=[{"role": "user", "content": prompt}],
        )
        response_text = getattr(completion.choices[0].message, "content", "")
        return Response({"response": response_text})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
