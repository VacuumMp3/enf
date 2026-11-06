"""
URL configuration for enf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls", namespace="main"))
]

                # <a href="{% url 'users:profile' %}" 
                # hx-get="{% url 'users:profile' %}" 

                #     <a href="{% url 'users:profile' %}" 
                #     hx-get="{% url 'users:profile' %}" 
                #     hx-target="#main-content" 
                # hx-push-url="true"
                # class="text-sm font-medium text-gray-900 uppercase hover:text-gray-600">
                #     ACCOUNT
                # </a>

            #                 function updateCartCount() {
            #     fetch('{% url "cart:cart_count" %}')
            #         .then(response => response.json())
            #         .then(data => {
            #             updateHeaderCartCount(data.total_items);
            #         });
            # }
    
            # function openCart() {
            #     htmx.ajax('GET', '{% url "cart:cart_modal" %}', {
            #         target: '#cart-container',
            #         swap: 'innerHTML'
            #     });
            # }


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)