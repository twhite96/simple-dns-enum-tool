import dns.resolver
import sys

dns_record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
    domain = sys.argv[1]
except IndexError:
    print('Syntax Error: python3 dnsenum.py <domainname> ')
for records in dns_record_types:
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f'\n{records}  Records')
        print('-'*30)
        for server in answer:
             print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
       print (f'{domain} does not exist. Please enter the correct domain.')
       quit()
    except KeyboardInterrupt:
        quit()