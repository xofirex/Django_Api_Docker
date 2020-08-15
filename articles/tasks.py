from django_cron import CronJobBase, Schedule
from .models import Post


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ["00:00"]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "articles.tasks"  # a unique code

    def do(self):
        for post in Post.objects.all():
            print(post)
            post.amount_of_upvotes = 0
            post.save()
