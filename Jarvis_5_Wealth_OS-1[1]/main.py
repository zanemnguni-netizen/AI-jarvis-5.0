from core.jarvis import Jarvis
from modules.wealth_engine import WealthEngine
from modules.business_engine import BusinessEngine
from modules.investment_engine import InvestmentEngine
from modules.productivity_engine import ProductivityEngine

def main():
    jarvis = Jarvis("Zane Mnguni")
    jarvis.boot()

    wealth = WealthEngine()
    business = BusinessEngine()
    invest = InvestmentEngine()
    productivity = ProductivityEngine()

    jarvis.speak("Your wealth directive for today:")
    for task in wealth.daily_directive():
        jarvis.speak(f"- {task}")

    jarvis.speak("High-leverage business opportunities:")
    for idea in business.ideas():
        jarvis.speak(f"- {idea}")

    jarvis.speak("Investment strategy overview:")
    for horizon, assets in invest.strategy().items():
        jarvis.speak(f"{horizon}: {', '.join(assets)}")

    jarvis.speak("Productivity laws:")
    for rule in productivity.focus_rules():
        jarvis.speak(f"- {rule}")

    jarvis.speak("Jarvis is online and executing. 🚀")

if __name__ == "__main__":
    main()
