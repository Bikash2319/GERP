from behave import given, when, then
from behave import StepNotImplementedError



@given(u'User redirect to reset password page')
def step_impl(context):
    raise StepNotImplementedError(u'Given User redirect to reset password page')


@when(u'User enter valid password in both the fields')
def step_impl(context):
    raise StepNotImplementedError(u'When User enter valid password in both the fields')


@when(u'Click on Reset Password button')
def step_impl(context):
    raise StepNotImplementedError(u'When Click on Reset Password button')


@then(u'Passoword should reset successfully and user redirect to login page')
def step_impl(context):
    raise StepNotImplementedError(u'Then Passoword should reset successfully and user redirect to login page')


@when(u'User enter invalid password in both the fields')
def step_impl(context):
    raise StepNotImplementedError(u'When User enter invalid password in both the fields')


@then(u'Error message should appear to enter valid passwords')
def step_impl(context):
    raise StepNotImplementedError(u'Then Error message should appear to enter valid passwords')


@then(u'User enter mismatched password')
def step_impl(context):
    raise StepNotImplementedError(u'Then User enter mismatched password')


@then(u'Password mismatched error message should appear')
def step_impl(context):
    raise StepNotImplementedError(u'Then Password mismatched error message should appear')