
from domain.context import context


def apply_promo(context: context)-> None:
    print(f"Promo applied to user with id {context.get('user_id')}")

avaible_actions = {
    "apply_promo": apply_promo
}

def run_action (name_action: str, context: context) -> None:
    action = avaible_actions.get(name_action)
    if not action:
        print(f"action '{name_action}' unavaible")
        return
    
    action(context)