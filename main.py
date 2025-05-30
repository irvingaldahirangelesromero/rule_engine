from engine.rule_engine import rule_engine
from repositories.rules_file import rules_file
from domain.context import context

def main():
    rules = rules_file("rules.json")
    engine = rule_engine(rules)
    con = context(
        data = ["",""]
        )
    results = engine.evaluate_rules (con)

    if results:
        for result in results:
            print(f"rule name: {result.name}")
            print(f"status: {result.active}")
 
if __name__ == "__main__":
    main()