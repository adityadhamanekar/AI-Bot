from django.shortcuts import render
from .gemini_utility import load_gemini_pro_model
from .models import ChatMessage


# Load Gemini-Pro model
model = load_gemini_pro_model()
chat_session = model.start_chat(history=[])

def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        
        # Send user's message to Gemini-Pro and get the response
        gemini_response = chat_session.send_message(user_message)

        # Save user message and Gemini response to database with logged-in user
        if request.user.is_authenticated:
            ChatMessage.objects.create(user=request.user, user_message=user_message, gemini_response=gemini_response.text)
        
            # Retrieve all messages from database
            all_messages = ChatMessage.objects.filter(user=request.user)

            return render(request, 'chatbot/index.html',{ 'all_messages':all_messages})

        
        return render(request, 'chatbot/index.html', {'user_message': user_message, 'gemini_response': gemini_response.text })
    else:
        if request.user.is_authenticated:
            all_messages = ChatMessage.objects.filter(user=request.user)
        
            return render(request, 'chatbot/index.html',{'all_messages':all_messages })

        return render(request, 'chatbot/index.html')