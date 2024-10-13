from urllib.parse import urlparse, urljoin

def validate_and_normalize_url(url):
    # Basic URL validation and normalization
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    parsed = urlparse(url)
    
    # Add 'www.' if it's missing and the domain doesn't already have a subdomain
    if not parsed.netloc.startswith('www.') and parsed.netloc.count('.') == 1:
        parsed = parsed._replace(netloc=f'www.{parsed.netloc}')
    
    if not parsed.netloc:
        raise ValueError("Invalid URL")
    
    # Reconstruct the URL
    normalized_url = parsed.geturl()
    
    return normalized_url
