Django PDF rendering
====================

Django PDF rendering, easily convert html responses to pdf responses

.. image:: https://img.shields.io/pypi/v/dj-easy-pdf.svg
    :target: https://pypi.python.org/pypi/dj-easy-pdf/
    :alt: Latest Version
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/dj-easy-pdf/
    :alt: Wheel
.. image:: https://img.shields.io/pypi/l/dj-easy-pdf.svg
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: License

Developed by `William Otieno <https://github.com/WilliamOtieno/>`_.


Overview
--------

This app makes rendering PDF files in Django really easy.
It can be used to create invoices, bills and other documents
from simple HTML markup and CSS styles. You can even embed images
and use custom fonts.

The library provides both Class-Based View that is almost a drop-in
replacement for Django's ``TemplateView`` as well as helper functions
to render PDFs in the backend outside the request scope
(i.e. using Celery workers).


Quickstart
----------

1. Include ``dj-easy-pdf``, ``xhtml2pdf`` in your ``requirements.txt`` file.
   If you are on Python 3 you need to install the latest version of Reportlab and the beta version of xhtml2pdf::

    $ pip install dj-easy-pdf

2. Add ``easy_pdf`` to ``INSTALLED_APPS``.

3. Create HTML template for PDF document and add a view that will render it:

    .. code-block:: css+django

        {% extends "easy_pdf/base.html" %}

        {% block content %}
            <div id="content">
                <h1>Hi there!</h1>
            </div>
        {% endblock %}

    .. code-block:: python

        from easy_pdf.views import PDFTemplateView

        class HelloPDFView(PDFTemplateView):
            template_name = 'hello.html'

4. You can also use a mixin to output PDF from Django generic views:

    .. code-block:: python

        class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
            model = get_user_model()
            template_name = 'user_detail.html'

5. If you're using Function Based views then:

    .. code-block:: python
    
        from easy_pdf.rendering import render_to_pdf_response
        
        def pdf_output(request):
            context = {}
            return render_to_pdf_response(request, "output.html", context)

Documentation
-------------

The full documentation is at `dj-easy-pdf.readthedocs.io <https://dj-easy-pdf.readthedocs.io/>`_.


Dependencies
------------

``django-easy-pdf`` depends on:

    - ``django>=3.2``
    - ``xhtml2pdf``
    - ``reportlab``


License
-------

``dj-easy-pdf`` is released under the MIT license.


Other Resources
---------------

- GitHub repository - https://github.com/WilliamOtieno/dj-easy-pdf
- PyPi Package site - https://pypi.python.org/pypi/dj-easy-pdf
- Docs - https://dj-easy-pdf.readthedocs.io/


Commercial Support
------------------

This app and many other help us build better software
and focus on delivering quality projects faster.
We would love to help you with your next project so get in touch
by dropping an email at jimmywilliamotieno@gmail.com
