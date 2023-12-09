from django.contrib.sites.shortcuts import get_current_site
from .forms import EmailSendForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Render HTML content from the template
            current_site = get_current_site(request)
            domain = current_site.domain
            html_message = render_to_string('email_template.html', {'subject': subject, 'message': message, 'domain': domain})

            # Send both HTML and plain text versions of the email
            send_mail(
                subject,
                strip_tags(html_message),  # Plain text version
                'fq118574@gmail.com',  # Sender's email address
                [email],
                html_message=html_message,  # HTML version
                fail_silently=False,
            )

            form.save()
            return redirect('emailsent')  # Redirect to a success page

    else:
        form = EmailSendForm()

    current_site = get_current_site(request)
    domain = current_site.domain
    context = {
        'form': form,
        'domain': domain,
    }

    return render(request, 'home.html', context)

def emailsent(request):
    current_site = get_current_site(request)
    domain = current_site.domain
    context = {
        'domain': domain,
    }
    return render(request, 'success_emailsend.html',context)



def send_email_from_url(request):
    email = request.GET.get('e', '')
    subject = request.GET.get('s', '')
    message = request.GET.get('msg', '')
    current_site = get_current_site(request)
    domain = current_site.domain

    if email and subject and message:
        # Render HTML content from the template
        html_message = render_to_string('email_template.html', {'subject': subject, 'message': message})

        # Send both HTML and plain text versions of the email
        send_mail(
            subject,
            strip_tags(html_message),
            'fq118574@gmail.com',
            [email],
            html_message=html_message,
            fail_silently=False,
        )
        
        context = {
            'domain': domain,
            }

        return render(request,'success_emailsend.html',context)

    else:
        # Return an error message or redirect to an error page
        error_message = "Error: Missing required parameters for sending email."
        return HttpResponse(error_message)

