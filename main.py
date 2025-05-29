from engine.rule_engine import rule_engine
from repositories.rules_file import rules_file
from domain.context import context_evaluation

def main():
    rules = rules_file("rules.json"),
    engine = rule_engine(rules)
    context = context_evaluation(
        code ="123"
        )
    results = engine.run(context)

    for result in results:
        print("rule name: {result.name}")
        print("status: {result.apply}")

 
if __name__ == "__main__":
    main()