# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re

# -----------------------------
# Training Data (Improved)
# -----------------------------
messages = [
    "Congratulations you won a lottery",
    "Click here to claim your prize",
    "Urgent your bank account is blocked",
    "Send OTP immediately",
    "Win free iPhone now",
    "You have been selected for a reward",
    "Claim your cashback now",
    "Limited offer click now",
    "Hello how are you",
    "Let's catch up tomorrow",
    "Meeting is scheduled at 5pm",
    "Happy birthday have a great day",
    "Your package has been delivered",
    "See you soon",
    "Lunch at 2?"
]

labels = [1,1,1,1,1,1,1,1, 0,0,0,0,0,0,0]  # 1 = Scam, 0 = Safe

# -----------------------------
# Preprocessing Function
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    return text

# Clean dataset
cleaned_messages = [clean_text(msg) for msg in messages]

# -----------------------------
# Model Training
# -----------------------------
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(cleaned_messages)

model = MultinomialNB()
model.fit(X, labels)

# -----------------------------
# Scam Detector Class
# -----------------------------
class ScamDetector:
    def __init__(self):
        self.history = []
        self.scam_keywords = {
            "otp", "urgent", "lottery", "win", "free",
            "prize", "click", "reward", "account", "bank",
            "offer", "cashback"
        }

    def keyword_risk(self, text):
        words = clean_text(text).split()
        return [word for word in words if word in self.scam_keywords]

    def predict(self, text):
        if not text.strip():
            return "⚠️ Invalid input!", 0, []

        cleaned = clean_text(text)

        # ML Prediction
        text_vector = vectorizer.transform([cleaned])
        probabilities = model.predict_proba(text_vector)[0]

        scam_prob = probabilities[1] * 100
        safe_prob = probabilities[0] * 100

        # Keyword Risk
        risky_words = self.keyword_risk(text)

        # Final Decision Logic (balanced)
        if scam_prob > 60 or len(risky_words) >= 2:
            result = " SCAM DETECTED"
        else:
            result = " SAFE MESSAGE"

        return result, round(scam_prob, 2), risky_words

    def add_to_history(self, text, result):
        self.history.append((text, result))

    def show_history(self):
        print("\n Message History:")
        for i, (msg, res) in enumerate(self.history, 1):
            print(f"{i}. {msg} --> {res}")

    def summary(self):
        scam_count = sum(1 for _, res in self.history if "SCAM" in res)
        total = len(self.history)

        if total > 0:
            print("\n Summary:")
            print(f"Total Messages: {total}")
            print(f"Scam Detected: {scam_count}")
            print(f"Safe Messages: {total - scam_count}")

# -----------------------------
# Main Program
# -----------------------------
def main():
    detector = ScamDetector()
    print("===  Scam Message Tracker Pro (Improved) ===")

    while True:
        try:
            user_input = input("\nEnter message (type 'exit' to quit): ")

            if user_input.lower() == "exit":
                detector.show_history()
                detector.summary()
                print("\n Exiting... Stay Safe Online!")
                break

            result, confidence, risky_words = detector.predict(user_input)

            print("\nResult:", result)
            print("Scam Probability:", confidence, "%")

            if risky_words:
                print("Risky Keywords:", ", ".join(risky_words))

            detector.add_to_history(user_input, result)

        except Exception as e:
            print("Error:", e)

# Run program
if __name__ == "__main__":
    main()
