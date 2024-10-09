from blog.models import Post
from blog.tasks import NewsClient, AIModel
from .models import Analysis


def createPostFromAnalysis(analysis: Analysis):
    if analysis:
        post = Post.objects.create(
            title=analysis.title,
            content=f"keywords: {analysis.keywords}\nprompt: {analysis.prompt}\nDate Range: {analysis.date_range_start} - {analysis.date_range_end}\nfindings: {analysis.findings}",
            date_posted=analysis.date_posted,
            author=analysis.author,
            is_public=False,
            analysis=analysis,
        )
        return post
    else:
        return None


class AINewsAnalyzer(NewsClient, AIModel):
    pass
