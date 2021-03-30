from django.contrib import admin
from .models import *


admin.site.register(GoalType)
admin.site.register(Goal)
admin.site.register(TrainingType)
admin.site.register(Trainer)
admin.site.register(Training)
admin.site.register(Promotion)
admin.site.register(Resignation)
admin.site.register(TerminationType)
admin.site.register(Termination)

