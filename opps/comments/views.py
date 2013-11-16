# coding: utf-8
from django.views.generic.edit import FormView
from django.utils.translation import ugettext_lazy as _
from opps.views.generic.json_views import JSONResponse
from .forms import CommentsForm


class CommentsView(FormView):
    template_name = "comments/comment_form.html"
    form_class = CommentsForm

    def get_initial(self):
        if self.request.user.is_authenticated():
            return {"author_name": self.request.user.get_full_name(),
                    "author_email": self.request.user.email,
                    "path": self.kwargs.get("path"),
                    "published": True}
        else:
            return super(CommentsView, self).get_initial()

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        form.save()
        return JSONResponse(
            {
                "success": True,
                "message": unicode(_("Comment posted"))
            }
        )

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        return JSONResponse(
            {
                "success": False,
                "message": unicode(_("Error posting comment")),
                "errors": form.errors
            }
        )
