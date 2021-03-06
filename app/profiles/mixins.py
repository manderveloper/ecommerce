from django.http import JsonResponse

class AjaxFormMixins(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixins, self).form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixins, self).form_valid(form)

        if self.request.is_ajax():
            print(form.cleaned_data)

            data = {
                'message': "Success"
            }
            return JsonResponse(data)
        else:
            return response
