# This module is automatically generated by autogen.sh. DO NOT EDIT.

from .. import _AWS

class _Integration(_AWS):
    _type = "integration"
    _icon_dir = "resources/aws/integration"


class Appsync(_Integration):
    _icon = "appsync.png"
class ConsoleMobileApplication(_Integration):
    _icon = "console-mobile-application.png"
class EventbridgeEvent(_Integration):
    _icon = "eventbridge-event.png"
class EventbridgeRule(_Integration):
    _icon = "eventbridge-rule.png"
class EventbridgeSaasPartnerEvent(_Integration):
    _icon = "eventbridge-saas-partner-event.png"
class Eventbridge(_Integration):
    _icon = "eventbridge.png"
class ExpressWorkflow(_Integration):
    _icon = "express-workflow.png"
class MQ(_Integration):
    _icon = "mq.png"
class SimpleNotificationService(_Integration):
    _icon = "simple-notification-service.png"
class SimpleQueueService(_Integration):
    _icon = "simple-queue-service.png"
class StepFunctions(_Integration):
    _icon = "step-functions.png"

# Aliases

SNS = SimpleNotificationService
SQS = SimpleQueueService
SF = StepFunctions