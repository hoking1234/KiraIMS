# flake8: noqa

from datetime import timedelta

from .base import *

DEBUG = True

ADMIN_ENABLED = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

SITE_NAME = "Inventory Management System"


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = "admin@example.com"


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/mediafiles/"

MEDIA_ROOT = BASE_DIR / "mediafiles/"

# # ==============================================================================
# # LOGGING SETTINGS
# # ==============================================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",  # Adjust as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            "class": "logging.StreamHandler",
        },
    },
}


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
