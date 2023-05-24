import simplejson as json
import csv


def extract(file_path_json, file_path_csv):
    with open(file_path_json) as f:
        data = json.load(f)

    with open(file_path_csv, mode="a") as f:
        writer = csv.writer(f)

        tls = (len(data['network']['tls']))
        udp = (len(data['network']['udp']))
        dns_servers = (len(data['network']['dns_servers']))
        http = (len(data['network']['http']))
        irc = (len(data['network']['irc']))
        smtp = (len(data['network']['smtp']))
        tcp = (len(data['network']['tcp']))
        smtp_ex = (len(data['network']['smtp_ex']))
        mitm = (len(data['network']['mitm']))
        hosts = (len(data['network']['hosts']))
        dns = (len(data['network']['dns']))
        http_ex = (len(data['network']['http_ex']))
        domains = (len(data['network']['domains']))
        dead_hosts = (len(data['network']['dead_hosts']))
        icmp = (len(data['network']['icmp']))
        http_ex = (len(data['network']['http_ex']))

        writer.writerow(["tls", "udp", "dns_servers", "http", "irc", "smtp", "tcp", "smtp_ex", "mitm", "hosts", "dns",
                         "http_ex", "domains", "dead_hosts", "icmp", "http_ex"])
        writer.writerow([tls, udp, dns_servers, http, irc, smtp, tcp, smtp_ex, mitm, hosts, dns, http_ex, domains,
                         dead_hosts, icmp, http_ex])

    # Closing file
    f.close()
    print("CSV file saved successfully.")

class DatasetAutomation:
    def __init__(self):
        extract()
