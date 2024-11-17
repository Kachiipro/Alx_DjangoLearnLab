Library project

# Security Settings for HTTPS and Secure Cookies

# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True  # Enforces secure connections

# HTTP Strict Transport Security (HSTS) settings
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS

# Secure cookies settings
SESSION_COOKIE_SECURE = True  # Session cookies only over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF cookies only over HTTPS

# Secure headers to mitigate clickjacking, XSS, and MIME sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filter
