# from django.views.generic import TemplateView, ListView, DetailView
# from .models import ContactInfo, Contact


# class ContactInfoView(TemplateView):
# 	template_name = 'contacts.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(ContactInfoView, self).get_context_data(**kwargs)
# 		context["contacts_title"] = Contact.objects.filter(id=1)
# 		return context