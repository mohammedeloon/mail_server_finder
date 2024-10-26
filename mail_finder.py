import pandas as pd
import sublist3r
import dns.resolver

file_path = 'mail_send.csv'
mails = pd.read_csv(file_path)
mails['domain_name'] = mails['smtp_email'].apply(lambda x: x.split('@')[1] if '@' in x else None)
mails['mail_server_name'] = None
mails['status'] = ''


def find_mail_server(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        mail_server = str(mx_records[0].exchange)
        return mail_server
    except Exception as e:
        return None


mails['mail_server_name'] = mails['domain_name'].apply(lambda x: find_mail_server(x) if x else None)
output_file = 'updated_mail_send.csv'
mails.to_csv(output_file, index=False)

print("Mail server information has been added and saved to", output_file)