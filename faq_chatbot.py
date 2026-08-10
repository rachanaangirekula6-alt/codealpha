import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# FAQ Questions and Answers
faq_questions = [
    "What is Python?",
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is OpenCV?",
    "How are you?",
    "Who created Python?"
]

faq_answers = [
    "Python is a popular programming language.",
    "Artificial Intelligence is the simulation of human intelligence in machines.",
    "Machine Learning is a branch of AI that learns from data.",
    "OpenCV is an open-source computer vision library.",
    "I am doing great! Thanks for asking.",
    "Python was created by Guido van Rossum."
]

# Convert questions into vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

print("===== FAQ Chatbot =====")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, faq_vectors)

    best_match = similarity.argmax()

    if similarity[0][best_match] > 0.2:
        print("Bot:", faq_answers[best_match])
    else:
        print("Bot: Sorry, I don't know the answer.")