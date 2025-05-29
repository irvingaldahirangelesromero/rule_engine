from engine.rule_engine import rule_engine
from repositories.rules_file import rules_file
from domain.context import context

def main():
    rules = rules_file("rules.json")
    engine = rule_engine(rules)
    con = context(
        code ="123",
        data = ["",""]
        )
    results = engine.run(con)

    if results is not None:
        for result in results:
            print("rule name: {result.name}")
            print("status: {result.apply}n")

 
if __name__ == "__main__":
    main()