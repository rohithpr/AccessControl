from datetime import datetime
import unittest

from access_control import Rule, Permission, exceptions


class TestRule(unittest.TestCase):
    def test_implicit_deny_explicitly_stated(self):
        with self.assertRaises(
            exceptions.rule_expections.ImplicitDenyExplictlyDeclaredException) as context:
            rule = Rule('scope.action', permission=Permission.IMPLICIT_DENY)
        
        expected_message = 'An IMPLICIT_DENY was excplicitly declared. Use EXPLICIT_DENY instead.'
        self.assertEqual(expected_message, context.exception.message)

    def test_rule_construction_with_all_params(self):
        action = 'scope.action'
        permission = Permission.EXPLICIT_DENY
        now = datetime.now()
        rule = Rule(action, permission, now)
        self.assertEqual(rule.action, action)
        self.assertEqual(rule.permission, permission)
        self.assertEqual(rule.expiration, now)

    def test_rule_construction_with_no_optional_params(self):
        action = 'scope.action'
        rule = Rule(action)
        self.assertEqual(rule.action, action)
        self.assertEqual(rule.permission, Permission.ALLOW)
        self.assertEqual(rule.expiration, None)
