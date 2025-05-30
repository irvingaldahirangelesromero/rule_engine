from engine.rule_engine import rule_engine
from repositories.rules_file import rules_file
from engine.rule import rule
from domain.context import context

def main():
    rules = rules_file("rules.json")

    engine = rule_engine(rules)
    
    actions_rule_1 = [AplicarDescuento(), EnviarCorreoBienvenida()]
    rule1 = rule(name="Decuento nuevo cliente", conditions=[...], exceptions=[...], restrictions=[...], benefits=[...], actions = actions_rule_1)   
    
    engine.registrar(rule1)

    # con = context(code=["code"],data=datoscontexto)
    results = engine.evaluate_rules(con)

    if results:
        for result in results:
            print(f"rule name: {result.name}")
            print(f"status: {result.active}")

if __name__ == "__main__":
    main()