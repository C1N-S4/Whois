import whois

domain_name = "google.com"

whois_info = whois.whois(domain_name)

print(whois_info)
