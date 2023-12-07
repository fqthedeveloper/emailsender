from django.shortcuts import render, redirect
from .forms import EmailSendForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Render HTML content from the template
            html_message = render_to_string('email_template.html', {'subject': subject, 'message': message})

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

    # Moved the else block outside of the if form.is_valid() block
    else:
        form = EmailSendForm()

    context = {
        'form': form
    }

    return render(request, 'home.html', context)


def emailsent(request):
    return render(request, 'success_emailsend.html')