# -*- coding: utf-8 -*-

from handlers import *
import utils


from ask_sdk_core.skill_builder import CustomSkillBuilder
# from ask_sdk_core.handler_input import HandlerInput
# from ask_sdk_model import Response


# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter=utils.s3_adapter())

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(RegisterPressureIntentHandler())
sb.add_request_handler(ReadLastPressureIntentHandler())
sb.add_request_handler(RemoveLastPressureIntentHandler())
sb.add_request_handler(EditLastPressureIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
