from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES) # Django, kötü niyetli saldırıları önlemek için uygulanan bir {% csrf_token %} etiketine sahiptir. Sayfayı oluştururken sunucu tarafında bir jeton oluşturur ve bu jetonun geri gelen herhangi bir istek için çapraz kontrol edilmesini sağlar. Gelen istekler jetonu içermiyorsa yürütülmez
#     print(request.path)
#     print(request.user)
#     print(request.META)
#     html = "<html> <body> hello FS </body> </html>"
#     return HttpResponse(html)


def home(request):
    context = {
        'caption': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, 'fsApp/index.html', context)