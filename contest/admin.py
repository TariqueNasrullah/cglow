from django.contrib import admin
from contest.models import contest
from contest.models import contest_problemset
from contest.models import contest_submission
from contest.models import contestant_point

# Register your models here.

admin.site.register(contest)
admin.site.register(contest_problemset)
admin.site.register(contest_submission)
admin.site.register(contestant_point)