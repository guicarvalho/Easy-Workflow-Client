# coding: utf-8

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
	
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        import ipdb; ipdb.set_trace()
        context['username'] = self.request.session.get('user')
        return context
