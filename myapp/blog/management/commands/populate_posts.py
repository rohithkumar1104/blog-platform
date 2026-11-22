from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args, **options):
        #Deleting existing
        Post.objects.all().delete()
        
        titles = [
"The Future of AI",
"Climate Change Solutions",
"Remote Work Trends",
"Quantum Computing Explained",
"Renewable Energy Innovations",
"Deep Learning Demystified", 
"Post-Pandemic Economic Outlook", 
"Blockchain In Finance", 
"Storytelling in Marketing", 
"Medical Technology Advances", 
"Space Exploration Challenges",
"Psychology of Decision Making",
"Evolution of Social Media",
"The Art of Cooking",
"Cultural Diversity in Society",
"Sustainable Development Investments",
"Globalization Impact",
"Power of Mindfulness",
"Online Learning Revolution",
"Art and Technology Fusion",
]

        contents = [
    "Artificial intelligence shaping future technologies, industries, employment, automation, and everyday human experiences.",
"Practical strategies for reducing greenhouse gas emissions, protecting ecosystems, and building climate-resilient communities.",
"Emerging workplace models, hybrid employment, digital collaboration, employee flexibility, and changing organizational practices.",
"Quantum principles, qubits, and advanced computational methods for solving complex problems beyond traditional computing.",
"Advanced solar, wind, hydrogen, battery storage, and other technologies accelerating the transition to clean energy.",
"Neural networks, data-driven learning, pattern recognition, and advanced algorithms powering modern artificial intelligence.",
"Economic recovery, inflation, employment, consumer behavior, and structural changes shaping the global economy after the pandemic.",
"Blockchain applications in financial transactions, digital assets, payment systems, security, transparency, and decentralized finance.",
"The use of compelling narratives, emotional connections, and authentic brand experiences to influence consumer engagement.",
"Advancements in artificial intelligence, robotics, medical devices, diagnostics, personalized treatment, and digital healthcare.",
"Technological, financial, environmental, and human challenges associated with long-term space missions and exploration.",
"Psychological factors, cognitive biases, emotions, experiences, and behavioral patterns influencing individual decision-making.",
"The transformation of social media through emerging platforms, digital communication, content creation, algorithms, and changing user behavior.",
"Creative techniques, culinary traditions, ingredients, flavors, and presentation that contribute to the preparation of exceptional food.",
"The role of cultural differences, traditions, identities, and perspectives in creating inclusive and harmonious societies.",
"Financial strategies supporting economic growth, environmental protection, social progress, and long-term sustainable development.",
"Cross-border trade, technology, communication, cultural exchange, and economic integration influencing societies worldwide.",
"Mindfulness practices supporting mental clarity, concentration, emotional balance, self-awareness, and overall well-being.",
"Digital platforms, interactive technologies, flexible education models, and personalized learning transforming modern education.",
"The integration of digital tools, artificial intelligence, virtual reality, and emerging technologies with traditional and contemporary art.",
]

        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",

]
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))