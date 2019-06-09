from access_control.rule import Rule
from access_control.ruleset import Ruleset
from access_control.permission import Permission

approve_claim = Rule('Claims.ApproveClaim')
deny_claim = Rule('Claims.DenyClaim')
issue_policy = Rule('Policy.IssuePolicy')

ruleset = Ruleset({approve_claim, deny_claim, issue_policy})

import pudb; pudb.set_trace()

print(ruleset.evaluate_action_permission('Claims.ApproveClaim'))
print(ruleset.evaluate_action_permission('Claims.RejectPolicy'))

print(ruleset.is_action_allowed('Claims.ApproveClaim'))
print(ruleset.is_action_allowed('Claims.RejectPolicy'))
